from django.urls import re_path, path
from inventoryManager import views

urlpatterns = [
    re_path(r'^', views.itemAPI),
    re_path(r'^item/(?P<item_id>\d+)/$', views.deleteItem, name='delete_item')
]