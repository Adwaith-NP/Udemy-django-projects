from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path('',views.index.as_view(),name = 'Index'),
    path('item/',views.item_l,name = "item"),
    path('detail/<int:pk>/',views.detail.as_view(),name = "detail"),
    path('add/',views.add_Item.as_view(),name="add"),
    path('edit/<int:id>/',views.edit_item,name = "edit_item"),
    path('del/<int:id>/',views.item_delete,name = "del"),
    path('profile/',views.profile,name = 'profile')
]
