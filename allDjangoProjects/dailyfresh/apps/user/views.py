from django.shortcuts import render

# Create your views here.



# 127.0.0.1:8000/user/register
def register(request):
    """注册页面"""
    return render(request, 'register.html')