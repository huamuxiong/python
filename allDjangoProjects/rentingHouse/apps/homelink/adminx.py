import xadmin

from .models import HouseInfo


class HouseInfoAdmin(object):
    list_display = ['title', 'village', 'location', 'unit_price', 'release_time', 'isFabu']
    search_fields = ['title']
    list_filter = ['title', 'isFabu', 'village', 'location']

    ordering = ['-id']
    exclude = ['img_address', 'userid', 'add_date', 'release_time']
    # readonly_fields = ['village', 'location']

    list_editable = ['isFabu']


xadmin.site.register(HouseInfo, HouseInfoAdmin)
