from django.shortcuts import render

# Create your views here.



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

    print(allow)

    # 验证数据

    # 注册业务

    # 返回应答
    return render(request, 'register.html')