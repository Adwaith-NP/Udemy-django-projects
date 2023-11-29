from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path('',views.index,name = 'Index'),
    path('item/',views.item_l,name = "item"),
    path('detail/<int:item_id>/',views.detail,name = "detail"),
    path('add/',views.add_Item,name="add"),
    path('edit/<int:id>/',views.edit_item,name = "edit_item"),
    path('del/<int:id>/',views.item_delete,name = "del"),
    path('profile/',views.profile,name = 'profile')
]
