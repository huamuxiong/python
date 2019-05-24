from django.db import models

# Create your models here.

class RedWood(models.Model):
    '''家具表'''
    style_choice = ((1, '传统中式'), (2, '新中式'), (3, '中式风格'))

    state_choice = ((0, '下架'), (1, '上架'))

    price_choice = (('1', '<2000'),('2', '2000-4000'),('3', '4000-6000'),('4', '6000-8000'),
                    ('5', '8000-10000'),('6', '10000-20000'),('7', '>20000'))

    title = models.CharField(max_length=255, verbose_name='标题')
    price = models.FloatField(max_length=10, verbose_name='价格')
    type = models.IntegerField(choices=style_choice, default=0, verbose_name='风格')
    img = models.ImageField(upload_to='images/redwood/')
    state = models.IntegerField(choices=state_choice, default=1, verbose_name='状态')

    comment = models.ManyToManyField('Users', through='UserComment', related_name='user_comment')
    history = models.ManyToManyField('Users', through='UserHistroy', related_name='user_history')
    collection = models.ManyToManyField('Users', through='UserCollect', related_name='user_collect')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')

    class Meta:
        db_table = 'redwood'
        verbose_name = '家具'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Users(models.Model):
    '''用户信息表'''
    gender_choice = ((1, '男'), (2, '女'))
    username = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    email = models.EmailField(max_length=30, verbose_name='邮箱')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='手机')
    gender = models.IntegerField(choices=gender_choice, default=1, verbose_name='性别')
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='出生年月')
    headimg = models.ImageField(upload_to='images/user/', verbose_name='头像')
    isActive = models.BooleanField(default=1, verbose_name='激活状态')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class UserComment(models.Model):
    '''评论表'''
    satisfied_choice=((1, '好评'), (2, '中评'), (3, '差评'))
    satisfied = models.IntegerField(choices=satisfied_choice, verbose_name='满意度')
    content = models.TextField(verbose_name='评论内容')

    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    redwood = models.ForeignKey(RedWood, on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

class UserHistroy(models.Model):
    '''浏览记录表'''
    redwood = models.ForeignKey(RedWood, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'history'
        verbose_name = '浏览记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.redwood.title

class UserCollect(models.Model):
    '''收藏表'''
    redwood = models.ForeignKey(RedWood, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'collection'
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.redwood.title

class UserAdvice(models.Model):
    '''用户建议申诉表'''
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    content = models.TextField(verbose_name='内容')
    reversion = models.TextField(verbose_name='回复', null=True, blank=True)

    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='申诉时间')

    class Meta:
        db_table = 'advice'
        verbose_name = '用户建议'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

class NewsInformation(models.Model):
    '''新闻资讯表'''
    type_choice = ((0, '网上摘的'), (1, '管理员发布的'))
    title = models.CharField(max_length=255, verbose_name='新闻标题')
    content = models.TextField(verbose_name='新闻内容')
    author = models.CharField(max_length=30, verbose_name='新闻发布者')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='新闻发布时间')

    class Meta:
        db_table='news'
        verbose_name='新闻资讯'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
