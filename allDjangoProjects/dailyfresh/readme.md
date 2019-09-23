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









