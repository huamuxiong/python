from django.contrib import admin
from .models import OrderGoods
# Register your models here.

class OrderGoodsAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderGoods, OrderGoodsAdmin)
