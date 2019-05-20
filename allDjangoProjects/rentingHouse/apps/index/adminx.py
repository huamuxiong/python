# -*- coding: utf-8 -*-
__author__ = 'leyton'
__date__ = '2019/2/23 0023 23:09'

import xadmin

from .models import *


class UserAdmin(object):

    list_display = ['username', 'email', 'regTime', 'birthday', 'isActive']
    search_fields = ['username', 'email']
    list_filter = ['regTime', 'birthday', 'isActive']

    list_editable = ['isActive', 'birthday']


class VillageAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_filter = ['name']

    list_editable = ['name']

    ordering = ['id']
    relfield_style = 'fk-ajax'


class LocationAdmin(object):
    list_display = ['id', 'vname', 'name']
    search_fields = ['villageLocation__name', 'name']
    list_filter = ['villageLocation__name', 'name']

    list_editable = ['name']
    ordering = ['id']
    relfield_style = 'fk-ajax'

    def vname(self, obj):
        return '%s' % obj.villageLocation.name
    vname.short_description = '地区'

class UserAgentAdmin(object):
    list_display = ['username', 'relname', 'gender', 'birthday', 'isActive']
    search_fields = ['relname']
    list_filter = ['userAgent__id']

    list_editable = ['isActive']

    def username(self, obj):
        return '%s' % obj.userAgent.username
    username.short_description = '用户名'

    def gender(self, obj):
        gender = obj.userAgent.gender
        if gender == 'male':
            gender = '男'
        else:
            gender = '女'
        return '%s' % gender
    gender.short_description = '性别'

    def birthday(self, obj):
        return '%s' % obj.userAgent.birthday
    birthday.short_description = '生日'

class SpecifyThePurchaseAdmin(object):
    list_display = ['username', 'village', 'addressinfo', 'housetype', 'telephone', 'add_time']
    search_fields = ['userS__username', 'villageS__name', 'addressinfo', 'housetype']
    list_filter = ['userS__id', 'villageS__name', 'housetype']
    #
    def username(self, obj):
        return '%s' % obj.userS.username
    username.short_description = '用户名'

    def village(self, obj):
        return '%s' % obj.villageS.name
    village.short_description = '地区'

class UserHistoryAdmin(object):
    list_display = ['userH', 'houseH', 'add_time']
    search_fields = ['userH__username', 'houseH__title']
    list_filter = ['userH__username', 'houseH__title']

class UserAdviceAdmin(object):
    list_display = ['nickname', 'email', 'advices', 'reversion', 'add_time']
    search_fields = ['userA__username', 'email', 'advices']
    list_filter = ['userA__username', 'email']
    list_editable = ['reversion']
    style_fields = {"advices":"ueditor"}

    def username(self, obj):
        return '%s' % obj.userA.username
    username.short_description = '用户名'

class ReleaseAdmin(object):
    list_display = ['userR', 'houseR', 'add_time']
    search_fields = ['userR__username']

class NewsInformationAdmin(object):
    pass

class UserCommentAdmin(object):
    pass

xadmin.site.register(UserComment, UserCommentAdmin)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(Village, VillageAdmin)
xadmin.site.register(Location, LocationAdmin)
xadmin.site.register(UserAgent, UserAgentAdmin)
xadmin.site.register(NewsInformation, NewsInformationAdmin)
xadmin.site.register(SpecifyThePurchase, SpecifyThePurchaseAdmin)
xadmin.site.register(UserHistory, UserHistoryAdmin)
xadmin.site.register(UserAdvice, UserAdviceAdmin)
xadmin.site.register(Release, ReleaseAdmin)