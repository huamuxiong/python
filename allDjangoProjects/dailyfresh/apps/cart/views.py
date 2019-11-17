from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from goods.models import GoodsSKU
from django_redis import get_redis_connection

from utils.mixin import LoginRequiredMixin


class CartAddView(View):
    """添加购物车"""
    def post(self, request):
        user = request.user
        if not user.is_authenticated:
            # 用户未登录
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收数据
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 验证数据正确性
        if not all([sku_id, count]):
            return JsonResponse({'res':1, 'errmsg': '数据不完整'})

        # 验证商品的数量格式是否正确
        try:
            count = int(count)
        except:
            return JsonResponse({'res':2, 'errmsg': '商品数目出错'})

        # 验证商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res':3, 'errmsg': '商品不存在'})

        # 业务处理
        conn = get_redis_connection('default')
        cart_key = 'cart_%d'%user.id

        # 先获取看redis中是否存在，不存在返回None
        cart_count = conn.hget(cart_key, sku_id)
        if cart_count:
            # 请求的与本来有的相加
            count += int(cart_count)

        # 验证库存
        if count > sku.stock:
            return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})

        # 设置redis中购物车的值
        conn.hset(cart_key, sku_id, count)

        # 计算用户购物车商品的条数
        total_count = conn.hlen(cart_key)

        # 返回应答
        return JsonResponse({'res': 5, 'total_count': total_count, 'message': '添加成功'})


class CartInfoView(LoginRequiredMixin, View):
    """显示购物车"""
    def get(self, request):
        # 获取登陆的用户信息
        user  =request.user
        # 获取用户购物车信息
        conn = get_redis_connection('default')
        cart_key = 'cart_%d'%user.id
        cart_dict = conn.hgetall(cart_key)

        skus = []
        total_count = 0
        total_price = 0

        for sku_id, count in cart_dict.items():
            count = int(count.decode('utf-8'))
            sku = GoodsSKU.objects.get(id=sku_id)
            amount = sku.price*count
            sku.amount = amount
            sku.count = count
            skus.append(sku)

            total_count += count
            total_price += amount

        context = {'total_count': total_count,
                   'total_price': total_price,
                   'skus': skus}

        # 使用模板
        return render(request, 'cart.html', context)


class CartUpdateView(View):
    """更新购物车"""
    def post(self, request):
        # 验证用户是否登陆
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        # 接收数据
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 验证数据的完整性
        if not all([sku_id, count]):
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        # 验证添加的商品数量
        try:
            count = int(count)
        except Exception as e:
            return JsonResponse({'res':2, 'errmsg': '商品数目出错'})

        # 验证商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res':3, 'errmsg': '商品不存在'})

        # 链接redis
        conn = get_redis_connection('default')
        cart_key = 'cart_%d'%user.id

        # 验证商品的库存
        if count > sku.stock:
            return JsonResponse({'res':4, 'errmsg':'商品库存不足'})

        # 更新redis
        conn.hset(cart_key, sku_id, count)

        # 计算总件数
        total_count = 0
        vals = conn.hvals(cart_key)
        for val in vals:
            total_count += int(val)

        # 返回应答
        return JsonResponse({'res':5, 'total_count':total_count, 'message': '更新成功'})


class CartDeleteView(View):
    """删除购物车记录"""
    def post(self, request):
        # 验证登陆
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登录'})

        # 接收参数
        sku_id = request.POST.get('sku_id')

        # 验证参数
        if not sku_id:
            return JsonResponse({'res':1, 'errmsg': '无效的商品id'})

        # 验证商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '商品不存在'})

        # 链接redis
        conn = get_redis_connection('default')
        cart_key = 'cart_%d'%user.id

        # 删除购物车中的该商品记录
        conn.hdel(cart_key, sku_id)

        # 计算总商品数
        total_count = 0
        vals = conn.hvals(cart_key)
        for val in vals:
            total_count += int(val)
        # 返回应答
        return JsonResponse({'res': 3, 'total_count': total_count, 'message': '删除成功'})