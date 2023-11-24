from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path('',views.index,name = 'Index'),
    path('item/',views.item_l,name = "item"),
    path('detail/<int:item_id>/',views.detail,name = "detail"),
]
