# -*- coding: utf-8 -*-

from index.models import EmailPro
from random import Random
from django.core.mail import send_mail
from rentingHouse.settings import EMAIL_FROM


# 随机生成字符串
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type='register'):
    email_recode = EmailPro()
    code = random_str(16)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type  =send_type
    email_recode.save()

    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = 'leyton租房网站注册激活链接'
        email_body = '请点击下方的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)
    else:
        email_title = 'leyton租房网站密码重置链接'
        email_body = '请点击下方的链接重置账号密码：http://127.0.0.1:8000/reset/{0}'.format(code)
    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    if send_status:
        pass


