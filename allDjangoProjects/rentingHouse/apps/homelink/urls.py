from django.urls import path
from .views import *

app_name = 'homelink'

urlpatterns = [
    path('', house_index, name='house_index'),
    path('spider/', house_spider, name='house_spider'),

]
