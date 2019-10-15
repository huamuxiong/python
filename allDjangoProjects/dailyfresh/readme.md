### 创建django项目

```python
django-admin startproject dailyfresh
```

### 创建app

```python
cd dailyfresh
python manage.py startapp user
python manage.py startapp order
python manage.py startapp goods
python manage.py startapp cart
```

### 打开settings配置文件，添加应用app，添加模板文件目录templates以及静态文件目录static，配置数据库为mysql，中文，实现地区

```python
# 如果应用多的话，一般会放在apps python包下
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 修改
INSTALLED_APPS = [
	...
	'user',  # 用户模块
	'order',  # 订单模块
	'goods',  # 商品模块
	'cart'  # 购物车模块
]

# 修改
TEMPLATES = [
	{	
		...
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		...
	}
]

# 添加


# 修改
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh',  # 数据库的名称
        'HOST': '192.168.1.6',  # 这个是我的ubuntu的ip
        'USER': 'root',
        'PASSWORD': 'root3306',
        'PORT': 3306
    }
}

# 修改
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

```

### 配置富文本编辑器

安装

```
pip install django-tinymce
```

添加应用，settings.py

```
INSTALLED_APPS = [
	...
	'tinymce',  # 富文本编辑器
]
```

窗口大小主题配置, settings.py

```
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}
```

### 数据库的迁移

```
python manage.py makemigrations
python manage.py migrate
```

### 运行项目

```
python manage.py runserver
```

### 发送邮件激活账户

参考链接CSDN：https://blog.csdn.net/linzi1994/article/details/83044109

官网：https://pypi.org/project/itsdangerous/#description

常用方法：

```python
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer('aaabbbccc')
>>> token = s.dumps({'id': 1}).decode()  # 加密
>>> token
'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU2OTI0ODM1MCwiZXhwIjoxNTY5MjUxOTUwfQ.eyJpZCI6MX0.xY51KdfJaJ7jqeTULIe84arAT_VPI_8lYUAZvRMbCpQ47Gn
xQoC_jvwf0KmSM4fmPIYZVLYoGmuXecX3ZqS-7w'
>>> s.loads(token)  # 解密
{'id': 1}
```

### 异步任务

拷贝整个项目到ubuntu，进入manage.py同级目录中，启动任务

```bash
celery -A celery_tasks.tasks worker -l info
```



## 常见问题

1. #### mysqlclient版本问题

```
...Lib\site-packages\django\db\backends\mysql\base.py
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.9.3(或其他版本)
```

解决办法：进入base.py文件，将如下代码注释

```
if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```

2. #### decode问题 

```

 File "D:\software\Anaconda3\envs\dailyfresh\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_exec
uted_query
    query = query.decode(errors='replace')
AttributeError: 'str' object has no attribute 'decode'
```

解决办法：进入operations.py文件的146行，修改如下：

```
query = query.encode('utf-8').decode(errors='replace')
即：先添加一个encode('utf-8')
```

3. #### mysql拒绝连接数据库1044错误

```
ERROR 1044: Access denied for user: 'root'@'192.168.1.6' to database 'dialyfresh'
```

解决办法：

设置ubuntu的绑定地址为ip：192.168.1.6

打开mysql配置文件

```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

默认绑定的是本地地址127.0.0.1，更改ip地址并保存退出

```
bind-address = 192.168.1.6
```

重启mysql服务

```
sudo service mysql restart
```

```
grant all privileges on dialyfresh.* to 'root'@'192.168.1.4' identified by 'root3306' with grant option;
```

其中：192.168.1.4是客户端ip，即我的windows ip

授权

```
flush privileges;
```

关掉并重新打开django shell，再次运行即可

4. #### views.py中使用class类来处理业务逻辑时遇到的问题

```
RuntimeError at /user/register
You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining POST data. Change your form to point to 127.0.0.1:8000/user/register/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.
```

解决办法：其实上文中已经给出了答案，如下：

```
Change your form to point to 127.0.0.1:8000/user/register/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.
```

在’/user/register‘处出现’RuntimeError‘错误

有两种解决办法：

一、在/user/register后添加一个斜杠’/‘，

二、在settings.py中添加一句话：APPEND_SLASH=False（这里使用的是第二种）

5. #### url自定义参数问题

django2.x版本以后提出了新的url用法path

如：先有基本地址：127.0.0.1:8000/user/active/<id>,其中id是动态变化的，那么在urls中定义如下

```python
url("^user/active/(?P<id>.*)/$", active),  # url写法
path("user/active/<str:id>", active),  # path写法
```

path用法：`<type:arg>`

Django2.0自带的PathConveter包括：

- str：匹配除了路径分隔符（/）之外的非空字符串，如果没有转换器，默认使用str作为转换器。
- int：匹配0及正整数。
- slug：匹配字母、数字以及横杠、下划线组成的字符串。
- uuid：匹配格式化的uuid，如 **075194d3-6885-417e-a8a8-6c931e272f00**。
- path：匹配任何非空字符串，包含了路径分隔符（/）

参考地址CSDN：https://www.cnblogs.com/wangdongpython/p/10865442.html

官网地址：https://docs.djangoproject.com/en/2.2/topics/http/urls/

6. #### windows链接ubuntu18.04的redis服务出错

```
Cannot connect to redis://192.168.1.6:6379/8:
```

问题描述：拒绝链接到redis服务

解决办法：

因为是在windows上连接ubuntu上的redis，所以ip改成ubuntu的ip，即192.168.1.6，但是redis默认绑定的是本地ip，即127.0.0.1，所以在windows上是连不上ubuntu上的redis的

修改redis的配置文件/etc/redis/redis.conf

```
bind: 0.0.0.0
protected-mode no
```

重启redis-server服务

```
service redis-server restart
```

7. #### windows上运行celery报错的问题

```
ValueError: not enough values to unpack (expected 3, got 0)
```

这个问题就是因为windows在执行celery异步任务时经常出现的错误。

解决办法：

安装`eventlet`

```
pip install eventlet
```

使用`eventlet`来启动`celery`任务

```
celery -A <mymodule> worker -l info -P eventlet
```

这里就是：

```
celery -A celery_tasks.tasks worker -l info -P eventlet
```

8. #### 登陆装饰器跳转认证

自定义的登陆页面链接为`/user/login/`

但是使用`login_require`装饰器的话默认是`/accounts/login/`

```
http://127.0.0.1:8000/accounts/login/?next=/user/
```

解决办法：

修改配置文件`settings.py`，改成自己的

```
LOGIN_URL = '/user/login'
```

