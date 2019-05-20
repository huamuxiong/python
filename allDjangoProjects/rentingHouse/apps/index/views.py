
import json
import os

from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.views.generic.base import View

from index.models import *
from homelink.models import *
from index.base import *
from .util import send_register_email
from index.forms import ContactUsForm

# 登录
@csrf_exempt
def login_views(request):
    '''
    登录验证，get请求页面，post验证登录
    :param request: username，password，remember
    :return: 源地址，login.html，index.html
    '''
    if request.method == 'GET':
        # 获取请求源地址，没有的话设置默认为根目录'/ '
        url = request.META.get('HTTP_REFERER', '/')
        if url[21:] == '/register/' or url[21:] == 'modifypwd' or 'userinfo' in url or 'reset' in url:
            url = '/'
        # 判断session中是否存在id和username，存在则直接返回源地址，否则判断cookie
        if 'isLogin' in request.session:
            return redirect(url)
        else:
            # 判断cookie中是否存在id和cookie，存在的话直接将值存入session，否则返回到登录页面
            if 'id' in request.COOKIES and 'username' in request.COOKIES:
                user_id = request.COOKIES['user_id']
                username = request.COOKIES['username']
                user = User.objects.get(id=user_id)
                request.session['user_id'] = user.id
                request.session['username'] = username
                request.sessino['headPortrait'] = user.headPortrait
                try:
                    agent = UserAgent.objects.get(userAgent_id=user_id)
                    # isJingjiren = agent.isActive
                except:
                    # isJingjiren = 2
                    pass
                # request.session['isJingjiren'] = isJingjiren
                return redirect(url)
            else:
                resp = render(request, 'login.html')
                # 将源地址保存进cookie中
                if url[21:] == '/login/' or 'reset' in url or url[21:] == '/register/' or url[21:] == '/zhiding/' or url[21:] == 'modifypwd' or '/userinfo/' in url[21:]:
                    url = '/'
                else:
                    url = url
                resp.set_cookie('url', url)
                return resp
    else:
        # post请求
        # 接收post传递过来的值
        username = request.POST['username']
        password = request.POST['password']
        # 验证登录是否成功
        try:
            user = User.objects.get(username=username)
            if user:
                checkpwd = check_password(password, user.password)
                # 登录成功后讲id和username存入session
                if checkpwd:
                    if user.isActive == 0:
                        return render(request, 'login.html', {'error_msg': '账号尚未激活', 'username': username, 'password': password})
                    user_id = user.id
                    headPortrait = user.headPortrait
                    try:
                        agent = UserAgent.objects.get(userAgent_id=user_id)
                    except:
                        pass
                    request.session['user_id'] = user_id
                    request.session['username'] = username
                    request.session['isLogin'] = 1
                    request.session['headPortrait'] = headPortrait
                    # 如果有记住密码，将数据保存至cookies
                    # 首先将url从cookies中取出来
                    url = request.COOKIES.get('url', '/')
                    resp = redirect(url)
                    # 如果url存在于cookies中的话，将url从cookies中删除
                    if 'url' in request.COOKIES:
                        resp.delete_cookie('url')
                    # 记住密码，将id和username的cookie值设置保存的时间
                    if 'remember' in request.POST:
                        times = 60 * 60 * 24 * 365  # 设置保存的时间为 1 年，单位是秒
                        resp.set_cookie('user_id', user_id, times)
                        resp.set_cookie('username', username, times)
                    return resp
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})
        except:
            return render(request, 'login.html', {'error_msg': '用户名或密码错误'})

# 退出
def logout_views(request):
    url = request.META.get('HTTP_REFERER', '/')
    if url[21:] == '/login/' or url[21:] == '/register/' or url[21:] == '/userinfo/' or 'userinfo' in url:
        url = '/'
    if 'isLogin' in request.session:
        del request.session['isLogin']
        del request.session['user_id']
        del request.session['username']
        del request.session['headPortrait']
    return redirect(url)

# 验证码激活  这个用类来实现，可以用下边的函数实现，就当做是练习类了
class ActiveUserView(View):
    def get(self, request, active_code):
        all_codes = EmailPro.objects.filter(code=active_code)
        if all_codes:
            for recode in all_codes:
                email = recode.email
                user = User.objects.get(email=email)
                user.isActive=True
                user.save()
            return redirect('/login/')
        else:
            return render(request, 'code_fail.html')

# 找回密码
class ForgetUserPasswdView(View):
    def get(self, request):
        return render(request, 'forget.html')

    def post(self, request):
        email = request.POST.get('email', '')
        user = User.objects.filter(email=email)
        if user:
            send_register_email(email, 'forget')
            return render(request, 'send_success.html', {'email_addr': email})
        else:
            return render(request, 'forget.html', {'err_msg': '邮箱未注册', 'email': email})

# 重置密码页面
class ResetPwdView(View):
    def get(self, request, active_code):
        all_codes = EmailPro.objects.filter(code=active_code)
        if all_codes:
            for recode in all_codes:
                email = recode.email
                return render(request, 'forget_reset_pwd.html', {'email': email})
        else:
            return render(request, 'code_fail.html')
        return render(request, 'login.html')

# 提交修改的密码
class ModifyPasswdView(View):
    def post(self, request):
        pwd1 = request.POST.get('password1', '')
        pwd2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        if pwd1 != pwd2:
            return render(request, 'forget_reset_pwd.html', {'err_msg': '两次密码不一致','pwd1': pwd1, 'pwd2': pwd2, 'email': email})
        user = User.objects.filter(email=email)[0]
        user.password = make_password(pwd1)
        user.save()
        return redirect('/login/')

# 注册
@csrf_exempt
def register_views(request):
    '''
    注册功能
    :param request: 参数
    :return: json 数据
    '''
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        # 查询邮箱或用户名是否存在
        users = User.objects.filter(Q(email=email) | Q(username=username))
        if users:
            data = {"result": 0}  # 已存在
        else:
            password = request.POST.get('password')
            password = make_password(password)  # 密码加密

            # 将注册信息添加到数据库的user表中
            obj = User(email=email, username=username, password=password, isActive=False)
            obj.save()
            data = {"result": 1}  # 注册成功
            send_register_email(email, 'register')

        return HttpResponse(json.dumps(data))

# 主页
def index_views(request):
    # session是否存在
    if 'isLogin' in request.session:
        username = request.session['username']
        user_id = request.session['user_id']
        headPortrait = request.session['headPortrait']
        try:
            agent = UserAgent.objects.get(userAgent_id=user_id)
        except:
            pass
    # 房源信息
    houseinfos = HouseInfo.objects.all()
    # 地区信息
    villages = Village.objects.all()
    return render(request, 'index.html', locals())

# 申请指定购房
@csrf_exempt
def zhidinggf_views(request):
    if 'isLogin' in request.session:
        user_id = request.session['user_id']

        villageid = request.POST.get('villageid')
        # villageid = int(villageid)
        xiangxiaddr = request.POST.get('xiangxiaddr', '')
        if not xiangxiaddr:
            xiangxiaddr = '您未填写详细地址'
        # 指定购房类型: 租房,新房,二手房
        gftype = request.POST.get('gftype')
        # housetype = houseType(gftype)

        telephone = request.POST.get('telephone')

        dic = {
            'addressinfo': xiangxiaddr,
            'housetype': gftype,
            'telephone': telephone,
            'userS_id': request.session['user_id'],
            'villageS_id': villageid
        }
        SpecifyThePurchase.objects.create(**dic)

        data = {'flag': 1}
    else:
        data = {'flag': 0}
    return HttpResponse(json.dumps(data))

@csrf_exempt
def zhiding_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            villages = Village.objects.all()
            return render(request, 'zhiding.html', locals())
        else:
            return render(request, 'error.html')
    else:
        dic = {
            "userS_id": request.session['user_id'],
            "villageS_id": request.POST.get('village_id'),
            "location":  request.POST.get('location_id'),
            "addressinfo":  request.POST.get('address'),
            "housetype":  request.POST.get('type'),
            "telephone":  request.POST.get('telephone')
        }
        try:
            SpecifyThePurchase.objects.create(**dic)
            data = {'flag': 1}
        except:
            data = {'flag': 0}
        return HttpResponse(json.dumps(data))

@csrf_exempt
def zhiding2_views(request, **kwargs):
    if 'isLogin' in request.session:
        id = kwargs['id']
        specify = SpecifyThePurchase.objects.get(Q(id=id) & Q(userS_id=request.session['user_id']))
        villages = Village.objects.all()
        locations = Location.objects.filter(villageLocation_id=specify.villageS_id)
        return render(request, 'zhiding2.html', locals())

# 指定购房获取位置信息---二级联动
@csrf_exempt
def locationValue_views(request):
    village_id = request.POST.get('village_id')
    locations = Location.objects.filter(villageLocation_id=village_id)
    data = serializers.serialize('json', locations)
    return HttpResponse(data)

# 租房详情
def pro_zu_info_views(request, id):
    # 获取该房源的id号
    zidinfo = HouseInfo.objects.get(id=id)
    agent_list = UserAgent.objects.filter(villageAgent_id=zidinfo.village_id, isActive=1)

    if 'isLogin' in request.session:
        username = request.session['username']
        user_id = request.session['user_id']
        headPortrait = request.session['headPortrait']
        guanzhu = UserFocus.objects.filter(userF_id=user_id, houseF_id=id)
        UserHistory.objects.create(userH_id=user_id, houseH_id=id)
    comment_list = UserComment.objects.filter(house_id=id).order_by('-create_time')
    page = request.GET.get('page')
    page_obj = fenye(comment_list, page, 3)
    commentcount = comment_list.count()
    url = request.get_full_path()
    try:
        agent = UserAgent.objects.get(userAgent_id=user_id)
    except:
        pass
    return render(request, 'pro_zu_info.html', locals())

# 关注
@csrf_exempt
def guanzhu_views(request):
    if request.method == 'POST':
        if 'isLogin' in request.session:
            user_id = request.session['user_id']
            house_id = request.POST.get('houseid', '')
            # houseid = int(houseid)

            # house = HouseInfo.objects.filter(id=houseid).first()
            try:
                guanzhu = UserFocus.objects.get(Q(houseF_id=house_id) & Q(userF_id=user_id))
            except:
                guanzhu = ''
            if guanzhu:
                # 已关注, 不做任何操作
                data = {
                    "result": 2,
                }
            else:
                # 未关注,  将房源信息和用户信息保存至guanzhu表
                dic = {'userF_id': user_id, 'houseF_id': house_id}
                # user = User.objects.get(id=userid)
                # house = HouseInfo.objects.get(id=houseid)
                UserFocus.objects.create(userF_id=user_id, houseF_id=house_id)
                data = {
                    "result": 1,
                    "msg": "关注成功"
                }
        else:
            data = {
                "result": 0,
                "msg": "请先登录"
            }
        return HttpResponse(json.dumps(data))
    else:
        # 直接URL输入的话跳转到首页
        return redirect('/')

# 个人中心--个人资料信息页
def userinfo_views(request):
    '''
    get：点击用户名进入个人中心，如果没有登录，地址栏输入  .../userinfo  则跳到首页
    post：修改资料，返回成功或失败
    :param request:
    :return:
    '''
    if request.method == 'GET':
        url = request.META.get('HTTP_REFERER', '/')
        if 'isLogin' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            headPortrait = request.session['headPortrait']
            # isJingjiren = request.session['isJingjiren']
            user = User.objects.get(id=user_id)
            try:
                agent = UserAgent.objects.get(userAgent_id=user_id)
            except:
                pass
            return render(request, 'userinfo.html', locals())
        return redirect('/')
    else:
        pass

# 个人中心--修改个人资料
@csrf_exempt
def updateUserinfo_views(request):
    if 'isLogin' in request.session:
        gender = request.POST['gender']
        telephone = request.POST['telephone']
        birthday = request.POST['birthday']
        QQ = request.POST['QQ']
        signtrue = request.POST['signtrue']
        if gender == '男':
            gender == 'male'
        else:
            gender == 'female'
        user = User.objects.get(id=request.session.get('user_id'))
        user.gender = gender
        user.telephone = telephone
        user.birthday = birthday
        user.QQ = QQ
        user.signature = signtrue
        user.save()
        data = {
            'status': 1,
            'msg': '修改成功'
        }
        return HttpResponse(json.dumps(data))

# 个人中心--用户重置密码
def reset_pwd_views(request):
    if request.method == 'GET':
        url = request.META.get('HTTP_REFERER', '/')
        if 'isLogin' in request.session:
            user_id = request.session['user_id']
            username = request.session['username']
            headPortrait = request.session['headPortrait']
            # isJingjiren = request.session['isJingjiren']
            try:
                agent = UserAgent.objects.get(userAgent_id=user_id)
            except:
                pass
            return render(request, 'userResetPwd.html', locals())
        else:
            return redirect('/')
    else:
        password = request.POST['password']
        password = make_password(password)
        if 'isLogin' in request.session:
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            user.password = password
            user.save()
            data = {
                'result': 1,
                'msg': '密码修改成功'
            }
            return HttpResponse(json.dumps(data))

# 个人中心--关注页面, 取消关注
@csrf_exempt
def user_guanzhu_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            headPortrait = request.session['headPortrait']
            # isJingjiren = request.session['isJingjiren']
            try:
                agent = UserAgent.objects.get(userAgent_id=user_id)
            except:
                pass
            # 获取到该用户关注的所有house_id
            guanzhu_list = UserFocus.objects.filter(userF_id=user_id).order_by('-add_time')
            page = request.GET.get('page')
            page_obj = fenye(guanzhu_list, page, 3)
            return render(request, 'user_guanzhu.html', locals())
        return redirect('/')
    else:
        # 取消关注
        # 获取要取消的houseid以及该用户的userid
        houseid = request.POST.get('houseid')
        user_id = request.session['user_id']
        try:
            # 将houseid和userid对应的关注信息从UserGuanzhu中删除
            UserFocus.objects.get(Q(houseF_id=houseid) & Q(userF_id=user_id)).delete()
            data = {'flag': 1}
        except:
            data = {'flag': 0}
        return HttpResponse(json.dumps(data))

# 个人中心--我的足迹(只有租房的详细页面才可以)
@csrf_exempt
def user_history_views(request):
    if request.method == 'GET':
        # get  获取我的足迹
        if 'isLogin' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            headPortrait = request.session['headPortrait']
            try:
                agent = UserAgent.objects.get(userAgent_id=user_id)
            except:
                pass
            history_list = UserHistory.objects.filter(userH_id=user_id).order_by('-add_time')
            page = request.GET.get('page')
            page_obj = fenye(history_list, page, 5)
            return render(request, 'user_history.html', locals())
        return redirect('/')
    else:
        # post  清空我的足迹
        if 'isLogin' in request.session:
            user_id = request.session['user_id']
            try:
                UserHistory.objects.filter(userH_id=user_id).delete()
                data = {'flag': 1}
            except:
                data = {'flag': 0}
            return HttpResponse(json.dumps(data))
        else:
            return redirect('/')

# 个人中心--我的指定购房 - GET
def user_zhiding_views(request):
    if 'isLogin' in request.session:
        username = request.session['username']
        user_id = request.session['user_id']
        headPortrait = request.session['headPortrait']
        try:
            agent = UserAgent.objects.get(userAgent_id=user_id)
        except:
            pass

        zhidinggfs = SpecifyThePurchase.objects.filter(userS_id=user_id).order_by('-mod_time')
        zdhouses = list()
        for zdh in zhidinggfs:
            zdhouse = dict()
            housetype = houseType(zdh.housetype)
            location = Location.objects.get(id=zdh.location)
            zdhouse['id'] = zdh.id
            zdhouse['nickname'] = username
            zdhouse['village'] = zdh.villageS.name
            zdhouse['location'] = location.name
            zdhouse['addressinfo'] = zdh.addressinfo
            zdhouse['housetype'] = housetype
            zdhouse['telephone'] = zdh.telephone
            zdhouse['mod_time'] = zdh.mod_time
            zdhouses.append(zdhouse)
        return render(request, 'user_zhiding.html', locals())
    return redirect('/')  # 没有登录进入主页面

# 个人中心--删除我的指定购房一个信息
@csrf_exempt
def user_deleteZD_views(request):
    if 'isLogin' in request.session:
        user_id = request.session['user_id']
        zdid = request.POST.get('id')
        try:
            SpecifyThePurchase.objects.filter(Q(id=zdid) & Q(userS_id=user_id)).delete()
            data = {'flag': 1}
        except:
            data = {'flag': 0}
        return HttpResponse(json.dumps(data))
    else:
        return redirect('/')

# 个人中心--修改我的指定购房一个信息
@csrf_exempt
def user_updateZD_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            user_id = request.session['user_id']
            zdid = request.GET.get('id')
            try:
                zdhouses = SpecifyThePurchase.objects.get(Q(userS_id=user_id) & Q(id=zdid))
                data = {
                    'flag': 1,
                    'zdid': zdhouses.id,
                    'zdvillid': zdhouses.villageS_id,
                    'zdaddressinfo': zdhouses.addressinfo,
                    'zdhousetype': zdhouses.housetype,
                    'zdtelephone': zdhouses.telephone
                }
            except:
                data = {'flag': 0}
            return HttpResponse(json.dumps(data))
        else:
            return redirect('/')
    else:
        if 'isLogin' in request.session:
            id = request.POST.get('id')
            villageid = request.POST.get('villageid')
            xiangxiaddr = request.POST.get('xiangxiaddr')
            gftype = request.POST.get('gftype')
            telephone = request.POST.get('telephone')

            try:
                zdgf = SpecifyThePurchase.objects.get(id=id)
                zdgf.villageS_id = villageid
                zdgf.addressinfo = xiangxiaddr
                zdgf.housetype = gftype
                zdgf.telephone = telephone
                zdgf.save()
                data = {'flag': 1}
            except:
                data = {'flag': 2}
            return HttpResponse(json.dumps(data))
        else:
            redirect('/')

# 个人中心--更改指定购房
@csrf_exempt
def user_Supdate_views(request):
    '''
    更新指定购房操作
    :param request:
    :return:
    '''
    id = request.POST.get('id')
    try:
        specify = SpecifyThePurchase.objects.get(Q(userS_id=request.session['user_id']) & Q(id=id))
        specify.villageS_id = request.POST.get('village_id')
        specify.location = request.POST.get('location_id')
        specify.addressinfo = request.POST.get('address')
        specify.housetype = request.POST.get('type')
        specify.telephone = request.POST.get('telephone')
        specify.save()
        data = {'flag': 1}
    except:
        data = {'flag': 0}
    return HttpResponse(json.dumps(data))

# 个人中心--申请成为经纪人
@csrf_exempt
def user_shenqing_views(request):
    if request.method == 'GET':
        # get展示申请页
        if 'isLogin' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            headPortrait = request.session['headPortrait']
            try:
                agent = UserAgent.objects.get(userAgent_id=user_id)
            except:
                pass
            user = User.objects.get(id=user_id)
            village_list = Village.objects.all()
            return render(request, 'user_shenqing.html', locals())
        return redirect('/')
    else:
        # post 提交申请
        dic = {
            'relname': request.POST.get('realname'),
            'identity': request.POST.get('ID_card'),
            'workage': request.POST.get('workage'),
            'isTelephone': request.POST.get('is_showtel'),
            'message': request.POST.get('grtextarea', None),
            'img': request.POST.get('imgaddr', None),
            'userAgent_id': request.session['user_id'],
            'villageAgent_id': request.POST.get('bee_village')
        }
        try:
            UserAgent.objects.create(**dic)
            data = {'flag': 1}
            # request.session['isJingjiren'] = 0
        except:
            data = {'flag': 0}
        return HttpResponse(json.dumps(data))

# 个人中心--申请经纪人上传照片
def upload_zhaopian_views(request):
    # id = request.session['id']
    # user = JingjirenInfo.objects.filter(user_id=id)
    # headPortrait = (user[0].img)[1:]
    # if os.path.exists(headPortrait):
    #     os.remove(headPortrait)
    # 接收图片资源
    file_obj = request.FILES.get('avatar')
    # 获取图片的后缀
    ext = file_obj.name.split('.')[-1]
    # print(ext)  # jpg
    # 生成新的无重复的图片名称
    file = fileNewName()
    filename = str(file) + '.' + ext
    # print(filename)

    file_path = os.path.join('static/media/zhongjieImg', filename)
    file_path = file_path.replace('\\', '/')  # 把\转换成/
    # 将图片保存到指定的文件夹中
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    # 将图片保存到数据库中（更新操作）
    # jjrImg = JingjirenInfo.objects.get(user_id=id)
    # jjrImg.img = '/' + file_path
    # jjrImg.save()
    # user1 = JingjirenInfo.objects.get(user_id=id)
    # request.session['img'] = user1.img
    return HttpResponse(file_path)

# 个人中心--我的房源发布列表
def wodefabu_views(request):
    if 'isLogin' in request.session:
        username = request.session['username']
        user_id = request.session['user_id']
        headPortrait = request.session['headPortrait']
        try:
            agent = UserAgent.objects.get(userAgent_id=user_id)
            # 根据用户 id 查出该用户发布的房源信息
            fabu_list = Release.objects.filter(userR_id=user_id).order_by('-mod_time')
            page = request.GET.get('page')
            page_obj = fenye(fabu_list, page, 6)
            return render(request, 'wodefabu.html', locals())
        except:
            return redirect('/')
    return redirect('/')

# 个人中心--修改发布的房源的信息界面
def updateFabu_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            username = request.session['username']
            user_id = request.session['user_id']
            headPortrait = request.session['headPortrait']
            # isJingjiren = request.session['isJingjiren']

            houseid = request.GET.get('id')
            houseinfo = HouseInfo.objects.get(id=houseid)
            return render(request, 'updateFabu.html', locals())
    else:
        if 'isLogin' in request.session:
            user_id = request.session['user_id']

            houseid = request.POST.get('houseid')
            title = request.POST.get('title')
            area = request.POST.get('area')
            bedroom = request.POST.get('bedroom')
            direction = request.POST.get('direction')
            floor = request.POST.get('floor')
            unit_price = request.POST.get('unit_price')
            message = request.POST.get('message')

            try:
                house = HouseInfo.objects.get(id=houseid)  # 查询出id对应的房子数据
                house.title = title
                house.area = area
                house.bedroom = bedroom
                house.direction = direction
                house.floor = floor
                house.unit_price = unit_price
                house.message = message
                house.save()  # 更新数据
                data = {'status': 1}  # 修改成功
            except:
                data = {'status': 0}  # 修改失败
            return HttpResponse(json.dumps(data))

# 个人中心--删除发布的信息
@csrf_exempt
def deleteFabu_views(request):
    if 'isLogin' in request.session:
        user_id = request.session['user_id']
        houseid = request.POST.get('houseid')
        try:
            Release.objects.filter(Q(houseR_id=houseid) & Q(userR_id=user_id)).delete()
            HouseInfo.objects.filter(id=houseid).delete()
            data = {'status': 1}
        except:
            data = {'status': 0}
        return HttpResponse(json.dumps(data))

# 关于我们
def aboutus_views(request):
    if 'isLogin' in request.session:
        username = request.session['username']
        headPortrait = request.session['headPortrait']
        try:
            agent = UserAgent.objects.get(userAgent_id=request.session.get('user_id'))
        except:
            pass
    return render(request, 'aboutus.html', locals())

# 联系我们
@csrf_exempt
def contactus_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            username = request.session['username']
            headPortrait = request.session['headPortrait']
            try:
                agent = UserAgent.objects.get(userAgent_id=request.session.get('user_id'))
            except:
                pass
        return render(request, 'contact.html', locals())
    else:
        # request.user.is
        if 'isLogin' in request.session:
            user_id = request.session['user_id']
            dic = {
                'email': request.POST.get('email'),
                'advices': request.POST.get('advices'),
                'nickname': request.POST.get('nickname'),
                'userA_id': user_id
            }
            try:
                UserAdvice.objects.create(**dic)
                data = {'flag': 1}
            except:
                data = {'flag': 2}
        else:
            data = {'flag': 0}
        return HttpResponse(json.dumps(data))

# 发布
@csrf_exempt
def fabu_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            user_id = request.session['user_id']
            # isJingjiren = request.session['isJingjiren']
            try:
                jingjireninfo = UserAgent.objects.get(userAgent_id=user_id)
                villageid = jingjireninfo.villageAgent_id
                vname = jingjireninfo.villageAgent.name
                locations = Location.objects.filter(villageLocation_id=villageid)
                return render(request, 'fabu.html', locals())
            except:
                return redirect('/')
        return redirect('/')
    else:
        # 提交发布内容
        village = request.POST.get('village')
        village = Village.objects.get(name=village).id
        user_id = request.session['user_id']
        dic = {
            'title': request.POST.get('title'),
            'village_id': village,
            'location_id': request.POST.get('location'),
            'area': request.POST.get('area'),
            'bedroom': request.POST.get('bedroom'),
            'direction': request.POST.get('direction'),
            'floor': request.POST.get('floor'),
            'unit_price': int(request.POST.get('unit_price')),
            'message': request.POST.get('message'),
            'img_address': request.POST.get('img'),
            'release_time': getNowDateTime(),
            'userid': user_id,
            'isFabu': False
        }
        try:
            HouseInfo.objects.create(**dic)  # 将前台发布传的数据保存到数据库中
            houseinfo = HouseInfo.objects.filter(userid=user_id).order_by('-add_date').first()
            houseid = houseinfo.id
            fabu = {
                'userR_id': user_id,
                'houseR_id': houseid,
            }
            Release.objects.create(**fabu)
            data = {'result': 1}  # 发布成功
        except:
            data = {'result': 0}
        return HttpResponse(json.dumps(data))

# 发布房源上传图片
@csrf_exempt
def fabu_upload_views(request):
    file_obj = request.FILES.get('fileName')
    # 获取图片的后缀
    ext = file_obj.name.split('.')[-1]
    # print(ext)  # jpg
    # 生成新的无重复的图片名称
    file = fileNewName()
    filename = str(file) + '.' + ext

    file_path = os.path.join('static/renthouseImg', filename)
    file_path = file_path.replace('\\', '/')  # 把\转换成/
    # 将图片保存到指定的文件夹中
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    res = {'file_path': file_path}
    return HttpResponse(json.dumps(res))

# 上传头像
def upload_avatar_views(request):
    '''
    先查找数据库看是否有头像，如果有再看本地指定的文件夹，有则删除再上传,
    保证本地文件夹与数据库的统一
    （节省本地内存，后期考虑redis本地缓存数据库）
    :param request:
    :return:
    '''
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    headPortrait = user.headPortrait
    if headPortrait:
        headPortrait = (headPortrait)[1:] # 去掉 '/'
    if os.path.exists(headPortrait):
        os.remove(headPortrait)
    # 接收图片资源
    file_obj = request.FILES.get('avatar')
    # 获取图片的后缀
    ext = file_obj.name.split('.')[-1]
    # print(ext)  # jpg
    # 生成新的无重复的图片名称
    file = fileNewName()
    filename = str(file) + '.' + ext  # 添加后缀

    file_path = os.path.join('static/media', filename)
    file_path = file_path.replace('\\', '/')  # 把\转换成/
    # 将图片保存到指定的文件夹中
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    # 将图片保存到数据库中（更新操作）
    userImg = User.objects.get(id=user_id)
    userImg.headPortrait = '/' + file_path
    userImg.save()
    user1 = User.objects.get(id=user_id)
    request.session['headPortrait'] = user1.headPortrait
    return HttpResponse(file_path)

# 租房列表页
def pro_zu1_views(request, *args, **kwargs):
    '''
    方向d-分类class
    '''
    searchTitle = request.GET.get('searchTitle', '')
    searchLocation = request.GET.get('searchLocation', '')
    # print('searchText:', searchTitle)
    current_url = request.path
    q = {}  # 查询条件
    q['isFabu'] = 1  # 已经发布成功的
    # ---自定义搜索
    if searchTitle:
        q['title__contains'] = searchTitle  # 包含
    if searchLocation:
        try:
            id = Location.objects.get(name__contains=searchLocation).id  # 获取位置的id
            q['location_id'] = id
        except:
            pass
    # ---条件筛选查询
    # 获取url中的地区id
    location_id = int(kwargs.get('location_id'))
    # 获取数据库中对应的所有地区
    village_list = Village.objects.all().values('id', 'name')
    # 如果地区时0,默认获取海淀的所有位置,如果位置为0,什么也不用做(既默认显示全部),如果不为0, 则获取位置的id对应的数据
    if kwargs.get('village_id') == '0':
        location_list = Location.objects.filter(villageLocation_id=1).values('id', 'name')
        if kwargs.get('location_id') == '0':
            pass
        else:
            q['location_id__in'] = [location_id,]
    else:
        # 地区选择接收的village_id
        # 位置为0的时候
        if kwargs.get('location_id') == '0':
            obj = Village.objects.get(id=int(kwargs.get('village_id')))  # 获取地区id
            location_list = obj.village.all().values('id', 'name')  # 利用外键获取该地区下的所有位置
            id_list = list(map(lambda x:x['id'], location_list))  # 把所有的位置id 生成一个列表
            q['location_id__in'] = id_list  # 查询上述列表中的所有位置
        # 位置不为0的时候, 此时地区和位置都不为0
        else:
            obj = Village.objects.get(id=int(kwargs.get('village_id')))  # 获取地区id
            location_list = obj.village.all().values('id', 'name')  # 获取地区下的所有位置
            id_list = list(map(lambda x: x['id'], location_list))  # 生成id 列表
            q['location_id'] = location_id
            if int(kwargs.get('location_id')) in id_list:
                pass
            else:
                # 不在列表中,选择全部
                url_part_list = current_url.split('-')  # 切割字符串生成列表
                url_part_list[2] = '0'
                current_url = '-'.join(url_part_list)

    # 第三个分类 租金
    price_id = int(kwargs.get('price_id'))
    if price_id == 0:
        pass
    else:
        price1 = price(price_id)  # 根据传过来的租金id 获取到对应的列表
        if len(price1) == 1:
            # 第一个和最后一个
            if price1[0] == 1000:
                q['unit_price__lt'] = price1[0]
            else:
                q['unit_price__gte'] = price1[0]
        else:
            # 除了第一个和最后一个
            q['unit_price__range'] = price1

    ret = map(lambda x: {"id": x[0], "name": x[1]}, HouseInfo.price_choice)
    price_list = list(ret)
    # 取出相应的房子

    sort = request.GET.get('sort', '')
    if sort == 'uprice':
        house_list = HouseInfo.objects.filter(**q).order_by('-unit_price')
    elif sort == 'area':
        house_list = HouseInfo.objects.filter(**q).order_by('-area')
    else:
        house_list = HouseInfo.objects.filter(**q)


    page = request.GET.get('page')
    page_obj = fenye(house_list, page, 10)  # 调用分页



    if 'isLogin' in request.session:
        username = request.session.get('username')
        headPortrait = request.session.get('headPortrait')
        try:
            agent = UserAgent.objects.get(userAgent_id=request.session.get('user_id'))
        except:
            pass
    return render(request, 'pro_zu.html', locals())

# 新闻资讯
def news_information_views(request):
    if 'isLogin' in request.session:
        username = request.session['username']
        headPortrait = request.session['headPortrait']
        try:
            agent = UserAgent.objects.get(userAgent_id=request.session.get('user_id'))
        except:
            pass
    news_list1 = NewsInformation.objects.all().order_by('-create_time')
    page = request.GET.get('page')
    page_obj = fenye(news_list1, page, 20)
    news_list2 = NewsInformation.objects.all().order_by('create_time')
    return render(request, 'newsinformation.html', locals())

# 新闻详情页
def news_info_views(request, id):
    '''新闻资讯详情页'''
    if 'isLogin' in request.session:
        username = request.session['username']
        headPortrait = request.session['headPortrait']
        try:
            agent = UserAgent.objects.get(userAgent_id=request.session.get('user_id'))
        except:
            pass
    new = NewsInformation.objects.get(id=id)
    return render(request, 'newsinfo.html', locals())

# 个人中心--我的申诉建议
@csrf_exempt
def advice_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            username = request.session['username']
            headPortrait = request.session['headPortrait']
            user_id = request.session.get('user_id')
            user = User.objects.get(id=user_id)
            try:
                agent = UserAgent.objects.get(userAgent_id=user_id)
            except:
                pass
            try:
                advice_list = UserAdvice.objects.filter(userA_id=user_id).order_by('-add_time')
                page = request.GET.get('page')
                page_obj = fenye(advice_list, page, 5)
            except:
                pass
            return render(request, 'user_advice.html', locals())
        return redirect('/')
    else:
        if 'isLogin' in request.session:
            id = request.POST.get('id')
            user_id = request.session.get('user_id')
            try:
                useradvice = UserAdvice.objects.get(id=id, userA_id=user_id).delete()
                data={'result': 1, 'msg': '删除成功'}
            except:
                data={'result': 0, 'msg': '操作失败！'}
            return HttpResponse(json.dumps(data))
        return redirect('/')

# 评论
@csrf_exempt
def comment_views(request):
    if 'isLogin' in request.session:
        try:
            comment = UserComment()
            comment.content = request.POST.get('content')
            comment.satisfied = request.POST.get('satisfied')
            comment.house_id = request.POST.get('id')
            comment.user_id = request.session.get('user_id')
            comment.save()
            data = {'result': 1, 'msg': '评论成功'}
        except:
            data = {'result': 0, 'msg': '评论失败'}
        return HttpResponse(json.dumps(data))
    return redirect('/')

# 删除评论
@csrf_exempt
def del_comment_views(request):
    next_url = request.META.get('HTTP_REFERER', '/')
    if 'isLogin' in request.session:
        user_id = request.session.get('user_id')
        id = request.POST.get('id')
        try:
            UserComment.objects.get(id=id, user_id=user_id).delete()
            data = {'result': 1, 'msg': '删除评论成功'}
        except:
            data = {'result': 0, 'msg': '删除失败'}
        return HttpResponse(json.dumps(data))
    return redirect(next_url)

# 个人中心--我的评论
@csrf_exempt
def user_comment_views(request):
    if request.method == 'GET':
        if 'isLogin' in request.session:
            username = request.session.get('username')
            headPortrait = request.session['headPortrait']
            user = User.objects.get(id=request.session.get('user_id'))
            comment_list = UserComment.objects.filter(user_id=request.session.get('user_id')).order_by('-create_time')
            comment_count = comment_list.count()
            page = request.GET.get('page')
            page_obj = fenye(comment_list, page, 5)
            try:
                # 是否是经纪人
                agent = UserAgent.objects.get(userAgent_id=request.session.get('user_id'))
            except:
                pass
            return render(request, 'user_comment.html', locals())
        return redirect('/')
    else:
        if 'isLogin' in request.session:
            id = request.POST.get('id')
            try:
                UserComment.objects.get(id=id, user_id=request.session.get('user_id')).delete()
                data = {'result': 1, 'msg': '删除评论成功'}
            except:
                data = {'result': 0, 'msg': '删除失败'}
            return HttpResponse(json.dumps(data))
        return redirect('/')


# 申诉建议
class ContactUsView(View):
    def get(self, request):
        if 'isLogin' in request.session:
            username = request.session['username']
            headPortrait = request.session['headPortrait']
            user_id = request.session.get('user_id')
            try:
                agent = UserAgent.objects.get(userAgent_id=user_id)
            except:
                pass
        return render(request, 'contact.html', locals())

class ContactUsSubmitView(View):
    @csrf_exempt
    def post(self, request):
        contactus_form = ContactUsForm(request.POST)
        if contactus_form.is_valid():
            contactus = contactus_form.save(commit=True)
            if contactus:
                print('ok')
            data = {'status': 'success'}
        else:
            data = {'status': 'fail', 'msg': contactus_form.errors}
        return HttpResponse(json.dumps(data))


# 404
def page_not_found(request, exception):
    return render(request, '404.html')

# 500
def page_error(request):
    return render(request, '500.html')
