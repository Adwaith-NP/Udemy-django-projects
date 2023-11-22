from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'Index'),
    path('item/',views.item_l,name = "item"),
]
