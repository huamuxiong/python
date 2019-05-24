import os

from django.contrib.auth.hashers import make_password, check_password
import json
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .base import *

# Create your views here.

@csrf_exempt
def login_views(request):
    if request.method == 'POST':
        '''post提交登录信息,验证是否登录成功
          获取上一级页面url
          失败: 留在登录页面
          成功: 写入session
              判断有无记住密码:
                    有: 写入cookie
                    无: pass
          跳转url
       '''
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(username=username)
            if user:
                if check_password(password, user.password):
                    if user.isActive == 0:
                        return render(request, 'login.html', {'error_msg': '账号被冻结,请联系管理员'})
                    request.session['is_login'] = 1
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    next_url = request.COOKIES.get('next_url')
                    resp = redirect(next_url)
                    if 'next_url' in request.COOKIES:
                        resp.delete_cookie('next_url')
                    if request.POST.get('remember'):
                        times = 60 * 60 * 24 * 365
                        resp.set_cookie('user_id', user.id, times)
                        resp.set_cookie('username', user.username, times)
                    return resp
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
        except:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
    else:
        '''get获取登录地址
          获取上一级页面url
          判断登录状态 is_login
          无is_login, 判断cookie
                有cookie, 写入session, 跳转url
                无cookie, 跳login.html
          有is_login, 跳转url
       '''
        next_url = get_url(request.META.get('HTTP_REFERER', '/'))
        if 'is_login' in request.session:
            return redirect(next_url)
        else:
            if 'user_id' in request.COOKIES:
                request.session['is_login'] = 1
                request.session['user_id'] = request.COOKIES.get('user_id')
                request.session['username'] = request.COOKIES.get('username')
                return redirect(next_url)
            else:
                '''将登录url写入cookie'''
                resp = render(request, 'login.html')
                resp.set_cookie('next_url', next_url)
                return resp

def index_views(request):
    '''主页'''
    if 'is_login' in request.session:
        user_id = int(request.session.get('user_id'))
        username = request.session.get('username')
        user = Users.objects.get(id=user_id)
    redwood_list = RedWood.objects.all()
    return render(request, 'index.html', locals())

def register_views(request):
    '''
    注册
    :param request: /register/
    :return: get返回页面，post提交注册
    '''
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        # 查询邮箱或用户名是否存在
        users = Users.objects.filter(Q(email=email) | Q(username=username))
        if users:
            data = {"result": 0}  # 已存在
        else:
            password = request.POST.get('password')
            password = make_password(password)  # 密码加密
            headimg = 'images/user/moren.jpg'  # 添加默认头像
            try:
                # 将注册信息添加到数据库的user表中
                obj = Users(email=email, username=username, password=password, headimg=headimg)
                obj.save()
                data = {"result": 1}  # 注册成功
            except:
                data = {"result": 2}  # 注册失败
        return HttpResponse(json.dumps(data))
    else:
        return render(request, 'register.html')

def logout_views(request):
    '''
    退出登录
    :param request: /logout/
    :return: url
    '''
    url = get_url(request.META.get('HTTP_REFERER')[21:])
    if 'is_login' in request.session:
        request.session.flush()
        resp = redirect(url)
        resp.delete_cookie('user_id')
        resp.delete_cookie('username')
        return resp
    return redirect(url)

def jiaju_list_views(request, *args, **kwargs):
    '''家具城列表页'''
    # 获取url 地址, 主要是两个参数
    current_url = request.path
    # 将所有的查询条件封装成一个字典,  首先创建一个空字典
    q = {}
    # 查询上架的所有家具
    q['state'] = 1

    # 自定义搜索 title
    searchTitle = request.GET.get('searchTitle', '')
    if searchTitle:
        q['title__contains'] = searchTitle
    # 获取两个参数
    style = int(kwargs.get('style1'))
    if style > 0:
        q['type'] = style

    price_id = int(kwargs.get('price1'))
    if price_id == 0:
        pass
    else:
        price1 = price(price_id)  # 根据传过来的租金id 获取到对应的列表
        if len(price1) == 1:
            # 第一个和最后一个
            if price1[0] == 2000:
                q['price__lt'] = price1[0]
            else:
                q['price__gte'] = price1[0]
        else:
            # 除了第一个和最后一个
            q['price__range'] = price1
    # 条件搜索部分
    style2 = map(lambda x: {"id": x[0], "name": x[1]}, RedWood.style_choice)
    style_list = list(style2)
    price2 = map(lambda x: {"id": x[0], "name": x[1]}, RedWood.price_choice)
    price_list = list(price2)

    # 查询家具
    jiaju_list = RedWood.objects.filter(**q).order_by('-create_time')
    page = request.GET.get('page')
    page_obj = fenye(jiaju_list, page, 10)  # 调用分页
    if 'is_login' in request.session:
        user_id = int(request.session.get('user_id'))
        username = request.session.get('username')
        user = Users.objects.get(id=user_id)
    return render(request, 'jiaju.html', locals())

def jiaju_info_views(request, id):
    '''家具详情页'''
    redwood = RedWood.objects.get(id=id)
    if 'is_login' in request.session:
        user_id = int(request.session.get('user_id'))
        username = request.session.get('username')
        user = Users.objects.get(id=user_id)
        # 加入浏览记录
        try:
            userhistory = UserHistroy.objects.get(redwood_id=id, user_id=user_id)
            userhistory.delete()
        except:
            pass
        finally:
            UserHistroy.objects.create(redwood_id=id, user_id=user_id)
    try:
        # 是否已关注
        collect = UserCollect.objects.get(redwood_id=id, user_id=user_id)
    except:
        pass
    # 加载评论
    url = request.get_full_path()
    hosts = request.get_host()

    comment_list = UserComment.objects.filter(redwood_id=id).order_by('-create_time')
    comment_count = comment_list.count()
    page = request.GET.get('page')
    page_obj = fenye(comment_list, page, 3)
    return render(request, 'jiaju_info.html', locals())

@csrf_exempt
def guanzhu_views(request):
    '''关注'''
    if request.method == 'POST':
        if 'is_login' in request.session:
            try:
                user_id = int(request.session.get('user_id'))
                id = request.POST.get('jiaju_id')
                collect = UserCollect()
                collect.user_id = user_id
                collect.redwood_id = id
                collect.save()
                data = {'result': 1, 'msg': '关注成功'}
            except:
                data = {'result': 2, 'msg': '关注失败'}
        else:
            data = {'result': 0, 'msg': '请先登陆'}
        return HttpResponse(json.dumps(data))
    else:
        # 直接输入关注的地址，跳转到主页
        return redirect('/')

def aboutus_views(request):
    '''关注我们'''
    if 'is_login' in request.session:
        user_id = int(request.session.get('user_id'))
        username = request.session.get('username')
        user = Users.objects.get(id=user_id)
    return render(request, 'aboutus.html', locals())

@csrf_exempt
def contactus_views(request):
    '''联系我们'''
    if request.method == 'GET':
        if 'is_login' in request.session:
            user_id = int(request.session.get('user_id'))
            username = request.session.get('username')
            user = Users.objects.get(id=user_id)
        return render(request, 'contact.html', locals())
    else:
        if 'is_login' in request.session:
            try:
                advice_info = UserAdvice()
                advice_info.user_id = request.session.get('user_id')
                advice_info.content = request.POST.get('jianyi')
                advice_info.nickname = request.POST.get('nickname')
                advice_info.save()
                data = {'flag': 1, 'msg': '留言成功'}
            except:
                data = {'flag': 2, 'msg': '留言失败，出现了什么问题'}
        else:
            data = {'flag': 0, 'msg': '亲，请先登录吧'}
        return HttpResponse(json.dumps(data))

@csrf_exempt
def user_info_views(request):
    '''个人中心'''
    if request.method == 'GET':
        url = get_url(request.META.get('HTTP_REFERER', '/'))
        if 'is_login' in request.session:
            user_id = int(request.session.get('user_id'))
            username = request.session.get('username')
            user = Users.objects.get(id=user_id)
            return render(request, 'userinfo.html', locals())
        return redirect(url)
    else:
        if 'is_login' in request.session:
            try:
                user = Users.objects.get(id=request.session.get('user_id'))
                user.email=request.POST.get('email')
                user.phone=request.POST.get('phone')
                user.gender=request.POST.get('gender')
                user.birthday=request.POST.get('birthday')
                user.save()
                data={'status': 1, 'msg': '修改成功'}
            except:
                data={'status': 0, 'msg': '修改失败'}
            return HttpResponse(json.dumps(data))
        else:
            return redirect('/')

@csrf_exempt
def user_history_views(request):
    '''个人中心--浏览记录'''
    if request.method == 'GET':
        url = get_url(request.META.get('HTTP_REFERER', '/'))
        if 'is_login' in request.session:
            user_id = int(request.session.get('user_id'))
            username = request.session.get('username')
            user = Users.objects.get(id=user_id)
            history_list = UserHistroy.objects.filter(user_id=user_id).order_by('-create_time')
            page = request.GET.get('page')
            page_obj = fenye(history_list, page, 3)  # 调用分页
            return render(request, 'user_history.html', locals())
        return redirect(url)
    else:
        # 清空浏览记录
        if 'is_login' in request.session:
            try:
                UserHistroy.objects.filter(user_id=request.session.get('user_id')).delete()
                data={'flag': 1, 'msg': '浏览记录已清空'}
            except:
                data={'flag': 0, 'msg': '操作失败！'}
            return HttpResponse(json.dumps(data))
        return redirect('/')

@csrf_exempt
def upload_avatar_views(request):
    '''上传头像'''
    if 'is_login' in request.session:
        # 查看数据库中的图片, 如果不是默认的。并且在本地存在则删除
        user = Users.objects.get(id=request.session.get('user_id'))
        # 改为upload之后就无法删除本地图片了，暂时不用了
        # if 'moren.jpg' not in user.headimg and os.path.exists(user.headimg.url):
        #     os.remove(user.headimg)
        # 接收上传的图片 FILES
        file_obj = request.FILES.get('avatar')
        # 图片后缀  如： jpg
        ext = file_obj.name.split('.')[-1]
        # 生成新的名称
        filename = fileNewName() + '.' + ext
        # 保存到本地
        file_path = os.path.join('images/user/' + filename).replace('\\', '/')
        with open(file_path, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)  # file.chunk() == file.read(), 只是更稳定，更快
        # 将本地地址保存到数据库中
        user.headimg = file_path
        user.save()
        return HttpResponse(file_path)
    return redirect('/')

@csrf_exempt
def reset_password_views(request):
    '''修改密码'''
    if request.method == 'POST':
        url = get_url(request.META.get('HTTP_REFERER', '/'))
        if 'is_login' in request.session:
            try:
                user = Users.objects.get(id=request.session.get('user_id'))
                user.password = make_password(request.POST.get('password'))
                user.save()
                data={'result': 1, 'msg': '密码修改成功'}
            except:
                data={'result': 0, 'msg': '操作失败'}
            return HttpResponse(json.dumps(data))
        return redirect('/')
    else:
        if 'is_login' in request.session:
            username = request.session.get('username')
            user = Users.objects.get(id=request.session.get('user_id'))
            return render(request, 'userResetPwd.html', locals())
        return redirect('/')

@csrf_exempt
def user_collect_views(request):
    '''收藏'''
    if request.method == 'POST':
        if 'is_login' in request.session:
            try:
                collect_id = request.POST.get('collectid')
                user_id =request.session.get('user_id')
                UserCollect.objects.get(user_id=user_id, id=collect_id).delete()
                data={'flag': 1, 'msg': '已取消关注'}
            except:
                data={'flag': 0, 'msg': '操作失败！'}
            return HttpResponse(json.dumps(data))
        return redirect('/')
    else:
        if 'is_login' in request.session:
            username = request.session.get('username')
            user = Users.objects.get(id=request.session.get('user_id'))
            collect_list = UserCollect.objects.filter(user_id=user.id).order_by('-create_time')
            page = request.GET.get('page')
            page_obj = fenye(collect_list, page, 3)
            return render(request, 'user_collect.html', locals())
        return redirect('/')

@csrf_exempt
def user_advice_views(request):
    '''个人中心--申诉建议'''
    if request.method == 'GET':
        if 'is_login' in request.session:
            username = request.session['username']
            user_id = request.session.get('user_id')
            user = Users.objects.get(id=user_id)
            advice_list = UserAdvice.objects.filter(user_id=user_id).order_by('-create_time')
            page = request.GET.get('page')
            page_obj = fenye(advice_list, page, 5)
            return render(request, 'user_advice.html', locals())
        return redirect('/')
    else:
        if 'is_login' in request.session:
            id = request.POST.get('id')
            user_id = request.session.get('user_id')
            try:
                useradvice = UserAdvice.objects.get(id=id, user_id=user_id).delete()
                data={'result': 1, 'msg': '删除成功'}
            except:
                data={'result': 0, 'msg': '操作失败！'}
            return HttpResponse(json.dumps(data))
        return redirect('/')

@csrf_exempt
def user_comment_views(request):
    '''个人中心---我的评论'''
    if request.method == 'GET':
        if 'is_login' in request.session:
            username = request.session.get('username')
            user = Users.objects.get(id=request.session.get('user_id'))
            comment_list = UserComment.objects.filter(user_id=request.session.get('user_id')).order_by('-create_time')
            comment_count = comment_list.count()
            page = request.GET.get('page')
            page_obj = fenye(comment_list, page, 5)
            return render(request, 'user_comment.html', locals())
        return redirect('/')
    else:
        if 'is_login' in request.session:
            id = request.POST.get('id')
            try:
                UserComment.objects.get(id=id, user_id=request.session.get('user_id')).delete()
                data = {'result': 1, 'msg': '删除评论成功'}
            except:
                data = {'result': 0, 'msg': '删除失败'}
            return HttpResponse(json.dumps(data))
        return redirect('/')

def news_information_views(request):
    '''新闻资讯'''
    if 'is_login' in request.session:
        username = request.session['username']
        user = Users.objects.get(id=request.session.get('user_id'))
    news_list = NewsInformation.objects.all().order_by('-create_time')
    page = request.GET.get('page')
    page_obj = fenye(news_list, page, 20)
    news_list2 = NewsInformation.objects.all().order_by('create_time')
    return render(request, 'newsinformation.html', locals())

def news_info_views(request):
    '''新闻资讯详情页'''
    if 'is_login' in request.session:
        username = request.session['username']
        user = Users.objects.get(id=request.session.get('user_id'))
    id = request.GET.get('id')
    new = NewsInformation.objects.get(id=id)
    return render(request, 'newsinfo.html', locals())

@csrf_exempt
def comment_views(request):
    '''评论功能的实现'''
    if request.method == 'GET':
        if 'is_login' in request.session:
            redwood = RedWood.objects.get(id=request.GET.get('id'))
            return render(request, 'comment.html', locals())
        return redirect('/error/')
    else:
        if 'is_login' in request.session:
            try:
                comment = UserComment()
                comment.content=request.POST.get('comment')
                comment.satisfied=request.POST.get('satisfied_id')
                comment.redwood_id=request.POST.get('jiaju_id')
                comment.user_id=request.session.get('user_id')
                comment.save()
                data={'flag': 1, 'msg': '评论成功'}
            except:
                data={'flag': 0, 'msg': '评论失败'}
            return HttpResponse(json.dumps(data))
        return redirect('/')

@csrf_exempt
def del_comment_views(request):
    '''删除详情页的评论'''
    next_url = request.META.get('HTTP_REFERER', '/')
    if 'is_login' in request.session:
        user_id =request.session.get('user_id')
        id = request.POST.get('id')
        try:
            UserComment.objects.get(id=id, user_id=user_id).delete()
            data = {'result': 1, 'msg': '删除评论成功'}
        except:
            data = {'result': 0, 'msg': '删除失败'}
        return HttpResponse(json.dumps(data))
    return redirect(next_url)

def error_views(request):
    '''错误页面'''
    return render(request, 'error.html')

def get_url(url):
    '''url 处理'''
    if '127.0.0.1:8000' in url:
        if url[21:] == '/login/' or url[21:] == '/register/' or url[21:] == '/error/' or 'user' in url:
            url = '/'
    elif url == '/login/' or url == '/register/' or url == '/error/' or 'user' in url:
        url = '/'
    return url