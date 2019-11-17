
import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django_redis import get_redis_connection
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired
# from celery_tasks.tasks import send_register_active_email
from goods.models import GoodsSKU
from celery_tasks.tasks import send_register_active_email
from .models import User, Address
from order.models import OrderInfo,OrderGoods

# GET 127.0.0.1:8000/user/register
def register(request):
    """注册页面"""
    return render(request, 'register.html')


# POST 127.0.0.1:8000/user/register
def regiseter_handle(request):
    """注册业务逻辑"""
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 验证数据
    if not all([username, password, email]):
        return render(request, 'register.html', {'err_msg': '数据不完整'})

    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'register.html', {'err_msg': '请同意协议'})

    try:
        user = User.objects.get(username=username)
    except Exception as e:
        user = None
    if user:
        return render(request, 'register.html', {'err_msg': '用户名已注册'})

    # 注册业务
    # user = User()
    # user.username = username
    # user.password = password
    # user.email = email
    # user.save()

    user = User.objects.create_user(username=username, password=password, email=email)
    # 是否激活修改为0
    user.is_active = False
    user.save()

    # 返回应答, 跳转到首页
    return redirect(reverse('goods:index'))


# 127.0.0.1:8000/user/register
class RegisterView(View):
    def get(self, request):
        """注册页面"""
        return render(request, 'register.html')

    def post(self, request):
        """注册业务逻辑处理"""
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 验证数据
        if not all([username, password, email]):
            return render(request, 'register.html', {'err_msg': '数据不完整'})

        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'err_msg': '请同意协议'})

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            user = None
        if user:
            return render(request, 'register.html', {'err_msg': '用户名已注册'})

        user = User.objects.create_user(username=username, password=password, email=email)
        # 是否激活修改为0
        user.is_active = False
        user.save()

        # 发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/3
        # 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密

        # 加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY, 600)
        token = serializer.dumps({'confirm': user.id}).decode()

        # 发送邮件
        # subject = '天天生鲜注册'
        # message = ''
        # sender = settings.EMAIL_FROM
        # receiver = [email]
        # html_message = '<a href="http://127.0.0.1:8000/user/active/%s">点击</a>'%(token)
        #
        # send_mail(subject, message, sender, receiver, html_message=html_message)

        send_register_active_email.delay(email, username, token)

        # 返回应答, 跳转到首页
        return redirect(reverse('goods:index'))


# 127.0.0.1:8000/user/active/<id>
class ActiveView(View):
    """账号激活"""
    def get(self, request, token):
        serializer = Serializer(settings.SECRET_KEY, 600)
        try:
            info = serializer.loads(token)
            user_id = info['confirm']
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 激活成功，跳转到登陆界面
            return redirect(reverse('user:login'))

        except SignatureExpired as e:

            return HttpResponse("账户激活链接已过期")


# 127.0.0.1:8000/user/login
class LoginView(View):
    """登陆"""
    def get(self, request):
        """登陆界面"""
        # 是否记住了用户名
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'login.html', locals())

    def post(self, request):
        # 接收前端数据
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 验证数据合法性
        if not all([username, password]):
            return render(request, 'login.html', {'err_msg': '数据不完整'})

        # 验证数据库
        # user = User.objects.get(username=username, password=password)
        user = authenticate(username=username, password=password)
        # authenticate 在django2.1版本之后加入了验证is_active，都为真时才返回True，否则返回None
        # 业务逻辑处理
        if user is not None:

            # 记录用户的登陆状态，session封装
            login(request, user)

            # 获取要跳转的页面，没有则跳转主页
            next_url = request.GET.get('next', reverse('goods:index'))
            response = redirect(next_url)

            # 判断是否要记住密码
            remember = request.POST.get('remember')
            if remember == 'on':
                # 添加到cookie
                response.set_cookie('username', username, max_age=7*24*3600)
            else:
                response.delete_cookie('username')

            return response

        else:
            return render(request, 'login.html', {'err_msg': '用户名或密码错误或账户未激活'})


# 127.0.0.1:8000/user/logout
class LogoutView(View):
    """退出登陆"""
    def get(self, request):
        # 使用django认证系统的logout清除session数据
        logout(request)

        # 跳转至首页
        return redirect(reverse('goods:index'))


# 127.0.0.1:8000/user/
class UserInfoView(LoginRequiredMixin, View):
    """用户中心---信息页"""
    def get(self, request):
        user = request.user
        # address = Address.objects.get(user=user, is_default=True)
        address = Address.objects.get_default_address(user)

        # 链接redis
        con = get_redis_connection("default")

        history_key = "history_%d" % user.id
        sku_ids = con.lrange(history_key, 0, 4)  # [2,3,1]
        goods_li = []
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_li.append(goods)

        # 组织上下文
        context = {'page': 'user',
                   'address': address,
                   'goods_li': goods_li}

        # 除了你给模板文件传递的模板变量之外，django框架会把request.user也传给模板文件
        return render(request, 'user_center_info.html', context)


# 127.0.0.1:8000/user/order/
class UserOrderInfoView(LoginRequiredMixin, View):
    """用户中心---订单页"""
    def get(self, request, page):
        # 获取用户的订单信息
        user =request.user
        # if not user.is_authenticated:
        #     return None
        orders = OrderInfo.objects.filter(user=user).order_by('-create_time')

        # 遍历获取到的商品的信息
        for order in orders:
            # 根据order_id查询订单信息
            order_skus = OrderGoods.objects.filter(order_id=order.order_id)

            # 遍历order_skus计算商品小计
            for order_sku in order_skus:
                amount = order_sku.count*order_sku.price
                # 动态给order_sku添加amount属性，保存订单商品的小计
                order_sku.amount = amount

            # 动态给order添加属性，保存订单状态标题
            order.order_status = OrderInfo.ORDER_STATUS[order.order_status]
            # 动态给order添加属性，保存订单商品的信息
            order.order_skus = order_skus

        # 分页
        paginator = Paginator(orders, 1)

        # 获取第page页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        # 获取第page页的实例对象
        order_page = paginator.page(page)

        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        # 组织上下文
        context = {'order_page': order_page,
                   'pages': pages,
                   'page': 'order'}

        # 使用模板
        return render(request, 'user_center_order.html', context)


# 127.0.0.1:8000/user/address
class UserAddressView(LoginRequiredMixin, View):
    """用户中心----地址页"""
    def get(self, request):
        """显示"""
        # 获取登录用户对应User对象
        user = request.user
        address = Address.objects.get_default_address(user)
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        #
        # except:
        #     address = None
        return render(request, 'user_center_site.html', {'page': 'address', 'address': address})

    def post(self, request):
        """添加地址"""
        # 接收地址信息
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 验证合法性
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg':'数据不完整'})

        # 校验手机号
        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', phone):
            return render(request, 'user_center_site.html', {'errmsg': '手机格式不正确'})

        # 业务处理：地址添加
        # 如果用户已存在默认收货地址，添加的地址不作为默认收货地址，否则作为默认收货地址
        # 获取登录用户对应User对象
        user = request.user
        address = Address.objects.get_default_address(user)
        # try:
            # address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None
        if address:
            is_default = False
        else:
            is_default = True

        Address.objects.create(
            user=user,
            receiver=receiver,
            addr=addr,
            zip_code=zip_code,
            phone=phone,
            is_default=is_default
        )

        # 返回结果
        return redirect(reverse('user:address'))

