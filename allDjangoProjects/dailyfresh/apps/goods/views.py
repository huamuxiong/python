from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import View
from django_redis import get_redis_connection
from order.models import OrderGoods
# Create your views here.


# 127.0.0.1:8000
from .models import GoodsSKU, GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner


# 127.0.0.1:8000
class IndexView(View):
    """主页"""
    def get(self, request):
        # 尝试从缓存中获取数据
        context = cache.get('index_page_data')

        if context is None:
            # 获取商品的种类信息
            types = GoodsType.objects.all()

            # 获取首页轮播商品信息
            goods_banners = IndexGoodsBanner.objects.all().order_by('index')

            # 获取首页促销活动信息
            promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

            for type in types:
                # 获取type种类首页分类商品的图片展示信息
                image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
                # 获取type种类首页分类商品的文字展示信息
                title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

                # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
                type.image_banners = image_banners
                type.title_banners = title_banners

            context = {'types': types,
                       'goods_banners': goods_banners,
                       'promotion_banners': promotion_banners}
            # 设置缓存
            # key  value timeout
            cache.set('index_page_data', context, 3600)

        # 显示购物车数量
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')  # 链接redis
            cart_key = 'cart_%d' % user.id  # 根据用户id获取购物车在redis中缓存的名字
            cart_count = conn.hlen(cart_key)  # 获取购物车的数量

        # 组织模板上下文
        context.update(cart_count=cart_count)

        return render(request, 'index.html', context)


# 127.0.0.1:8000/detail/<goods_id>
class DetailView(View):
    def get(self, request, goods_id):
        try:
            # 根据商品id查询该商品的详细信息
            sku = GoodsSKU.objects.get(id=goods_id)
        except GoodsSKU.DoesNotExist:
            # 商品不存在
            return redirect(reverse('goods:index'))

        # 获取商品分类
        types = GoodsType.objects.all()

        # 获取评价信息
        sku_orders = OrderGoods.objects.filter(sku=sku).exclude(comment='')

        # 获取同一个SPU的其他规格商品
        same_spu_skus = GoodsSKU.objects.filter(goods=sku.goods).exclude(id=goods_id)

        # 获取新品信息
        new_skus = GoodsSKU.objects.filter(type=sku.type).order_by('-create_time')

        # 购物车, 并添加浏览记录
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

            # 添加用户的历史记录
            conn = get_redis_connection('default')
            history_key = 'history_%d' % user.id
            # 移除列表中的goods_id
            conn.lrem(history_key, 0, goods_id)
            # 把goods_id插入到列表的左侧
            conn.lpush(history_key, goods_id)
            # 只保存用户最新浏览的5条信息
            conn.ltrim(history_key, 0, 4)

        context = {'sku': sku,
                   'types': types,
                   'sku_orders': sku_orders,
                   'new_skus': new_skus,
                   'same_spu_skus': same_spu_skus,
                   'cart_count': cart_count}
        return render(request, 'detail.html', context)


# 127.0.0.1:8000/list/type_id/page?sort=xxx
class ListView(View):
    def get(self, request, type_id, page):
        """
        列表页
        :param type_id: 分类 id
        :param page: 页码
        :param sort: 排序
        :return: list.html, context:数据
        """
        # 根据需求，需要获取以下数据
        # 全部商品分类（在base_detail_list.html）
        # 购物车（需要判断用户是否登陆，默认显示0，base_detail_list.html）
        # 新品推荐
        # 列表分类，即当前是哪个分类下的列表（新鲜水果，猪牛羊肉等）
        # 列表数据（三种排序：默认，价格，人气）
        # 列表分页

        # 根据type_id 获取该分类的信息
        try:
            type = GoodsType.objects.get(id=type_id)
        except Exception as e:
            # 种类不存在
            return redirect(reverse('goods:index'))

        # 全部分类
        types = GoodsType.objects.all()

        # 购物车
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            cart_count = conn.hlen(cart_key)

        # 新品推荐
        new_skus = GoodsSKU.objects.filter(type=type).order_by('-create_time')[:3]

        # 列表数据（三种排序：默认，价格，人气）
        # 获取sort参数,分别是default, price, hot
        sort = request.GET.get('sort')
        # 获取数据并根据用户选择进行排序
        if sort == 'price':
            skus = GoodsSKU.objects.filter(type=type).order_by('price')
        elif sort == 'hot':
            skus = GoodsSKU.objects.filter(type=type).order_by('-sales')
        else:
            sort = 'default'
            skus = GoodsSKU.objects.filter(type=type).order_by('-id')

        # 对数据进行分页,Paginator(list, per_page)
        paginator = Paginator(skus, 1)

        # 如果page不能转换为int类型，设置为 1
        try:
            page = int(page)
        except Exception as e:
            page = 1

        # 如果page大于总页数或小于 1，设置为 1
        if page > paginator.num_pages or page < 1:
            page = 1

        # 获取第page页的实例对象
        skus_page = paginator.page(page)

        # todo: 进行页码的控制，页面上最多显示 5 页
        # 1. 总页数小于5，页面显示所有的页码
        # 2. 当前页在前3页，显示1-5的页码
        # 3. 当前页是后3页，显示后5页的页码
        # 4. 其他情况，显示当前页，前后各2页

        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages+1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages-4, num_pages+1)
        else:
            pages = range(page-2, page+3)

        context = {
            'type': type,
            'types': types,
            'cart_count': cart_count,
            'new_skus': new_skus,
            'sort': sort,
            'skus_page': skus_page,
            'pages': pages

        }
        return render(request, 'list.html', context)
