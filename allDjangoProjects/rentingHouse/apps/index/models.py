
from DjangoUeditor.models import UEditorField

from django.db import models
from homelink.models import HouseInfo


# 邮箱--用来激活账号
class EmailPro(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '邮箱注册'), ('forget', '忘记密码')), verbose_name='发送类型')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')

    class Meta:
        db_table='emailpro'
        verbose_name='邮箱验证码'
        verbose_name_plural=verbose_name


# 用户基本信息表
class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='male',
                              verbose_name='性别')
    email = models.EmailField(verbose_name='电子邮箱')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    telephone = models.CharField(max_length=12, verbose_name='手机号', null=True, blank=True)
    QQ = models.CharField(max_length=12, verbose_name='qq号', null=True, blank=True)
    headPortrait = models.CharField(max_length=200, default='/static/images/guanyu.jpg', verbose_name='头像路径')
    signature = models.TextField(verbose_name='个人签名', null=True, blank=True)
    regTime = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')  # 获取当前系统时间
    isActive = models.BooleanField(default=1, verbose_name='账号是否激活')

    # 多对多,  关注
    userFo = models.ManyToManyField(HouseInfo, through='UserFocus', related_name='guanzhu')

    # 多对多,  浏览记录
    userHi = models.ManyToManyField(HouseInfo, through='UserHistory', related_name='history')

    def __repr__(self):
        return "<User: %r>" % self.username

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        unique_together = ('username', 'email', 'telephone', 'QQ')

# 地区表
class Village(models.Model):
    name = models.CharField(max_length=30, verbose_name='地区名称')  # 海淀

    class Meta:
        db_table = 'village'
        verbose_name = '地区'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# 位置表
class Location(models.Model):
    name = models.CharField(max_length=30, verbose_name='位置名称')

    villageLocation = models.ForeignKey(Village, on_delete=models.CASCADE, verbose_name='地区', related_name='village')


    def __unicode__(self):
        return '%s' % self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'location'
        verbose_name = '地区位置'
        verbose_name_plural = verbose_name

# 经纪人表
class UserAgent(models.Model):
    relname = models.CharField(max_length=30, verbose_name='真实姓名')
    identity = models.CharField(max_length=30, verbose_name='身份证信息')
    workage = models.IntegerField(verbose_name='工作年限')
    isTelephone = models.BooleanField(default=1, verbose_name='是否显示联系方式')
    img = models.CharField(max_length=255, default='/static/media/zhongjieImg/guoxiangyu.jpg', verbose_name='经纪人照片')
    message = models.TextField(verbose_name='个人描述')

    isActive = models.BooleanField(verbose_name='审核是否通过', default=0)

    userAgent = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户名')
    villageAgent = models.ForeignKey(Village, on_delete=models.CASCADE, verbose_name='地区')

    class Meta:
        db_table = 'agent'
        verbose_name = '经纪人信息'
        verbose_name_plural = verbose_name
        unique_together = ('userAgent',)

    def __repr__(self):
        return "<UserAgent: %r>" % self.id

# 关注
class UserFocus(models.Model):
    userF = models.ForeignKey(User, on_delete=models.CASCADE)
    houseF = models.ForeignKey(HouseInfo, on_delete=models.CASCADE)

    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'focus'
        verbose_name = '关注'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.userF.username

# 用户指定购房表
class SpecifyThePurchase(models.Model):
    userS = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    villageS = models.ForeignKey(Village, on_delete=models.CASCADE, verbose_name='地区')
    location = models.IntegerField(verbose_name='位置')
    housetype = models.CharField(max_length=30, choices=(('zufang', '租房'), ('xinfang', '新房'), ('ershoufang', '二手房')), default='zufang', verbose_name='找房类型')
    addressinfo = models.CharField(max_length=50, verbose_name='详细地址')
    telephone = models.CharField(max_length=11, verbose_name='联系方式')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='指定时间')
    mod_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'specifythepurchase'
        verbose_name = '指定购房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s-%s-%s' % (self.userS.username, self.villageS.vname, self.telephone)

    def __repr__(self):
        return "<SpecifyThePurchase: %r>" % self.userS.id

# 用户浏览记录
class UserHistory(models.Model):
    # userid = models.IntegerField(verbose_name='用户id')
    # houseid = models.IntegerField(verbose_name='房源id')

    userH = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    houseH = models.ForeignKey(HouseInfo, on_delete=models.CASCADE, verbose_name='房源')

    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='浏览时间')

    def __repr__(self):
        return '<History: %r>' % self.houseH.title

    class Meta:
        db_table = 'history'
        verbose_name = '浏览记录'
        verbose_name_plural = verbose_name


# 用户建议表
class UserAdvice(models.Model):
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    email = models.EmailField(verbose_name='用户邮箱')
    # advices = models.CharField(max_length=255, verbose_name='用户建议')

    advices = UEditorField(verbose_name='用户建议', width=600, height=300, toolbars="full",
                          imagePath="advices/ueditor/%(datetime)s.%(extname)s",
                           filePath="advices/ueditor/%(datetime)s.%(extname)s", default='')
    reversion = models.TextField(verbose_name='回复', null=True, blank=True)

    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='提建议时间')

    userA = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    def __repr__(self):
        return '<UserAdvice: %r>' % self.nickname

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'advice'
        verbose_name = '申诉建议'
        verbose_name_plural = verbose_name

# 发布表
class Release(models.Model):
    # userid = models.IntegerField(verbose_name='用户id')
    # houseid = models.IntegerField(verbose_name='房子id')

    userR = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    houseR = models.ForeignKey(HouseInfo, on_delete=models.CASCADE, verbose_name='房源')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    mod_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __repr__(self):
        return '<Release: %r>' % self.houseR.title

    def __str__(self):
        return self.houseR.title

    class Meta:
        db_table = 'release'
        verbose_name = '用户发布信息'
        verbose_name_plural = verbose_name

class NewsInformation(models.Model):
    '''新闻资讯表'''
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

class UserComment(models.Model):
    '''评论表'''
    satisfied_choice=((1, '好评'), (2, '中评'), (3, '差评'))
    satisfied = models.IntegerField(choices=satisfied_choice, verbose_name='满意度')
    content = models.TextField(verbose_name='评论内容')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    house = models.ForeignKey(HouseInfo, on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content