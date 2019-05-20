from django.db import models
# Create your models here.
from index.models import *

class HouseInfo(models.Model):
    title = models.CharField(max_length=256, verbose_name='标题')
    bedroom = models.CharField(max_length=20, verbose_name='房厅')   # 几居室
    area = models.CharField(max_length=20, verbose_name='面积')      # 175㎡
    direction = models.CharField(max_length=20, verbose_name='朝向')  # 南
    floor = models.CharField(max_length=60, verbose_name='楼层')     # 18
    unit_price = models.IntegerField(verbose_name='租金')
    message = models.TextField(default='无', verbose_name='详细信息')
    img_address = models.CharField(max_length=255, verbose_name='图片地址')  # /static/renthouseImg
    userid = models.IntegerField(default=1, verbose_name='用户id')
    release_time = models.CharField(max_length=255, verbose_name='发布时间')  # 20天以前...
    isFabu = models.BooleanField(default=True, verbose_name='发布是否成功')

    add_date = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    village = models.ForeignKey('index.Village', on_delete=models.CASCADE, null=True, blank=True, verbose_name='地区')
    location = models.ForeignKey('index.Location', on_delete=models.CASCADE, null=True, blank=True, verbose_name='位置')

    comment = models.ManyToManyField('index.User', through='index.UserComment', related_name='comment')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'houseinfo'
        verbose_name = "租房"
        verbose_name_plural = verbose_name

    price_choice=(
        ('1', '<1000'),
        ('2', '1000-2000'),
        ('3', '2000-3000'),
        ('4', '3000-4000'),
        ('5', '4000-5000'),
        ('6', '5000-8000'),
        ('7', '>8000')
    )
