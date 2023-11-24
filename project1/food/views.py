from django.http import HttpResponse
from django.shortcuts import render
from food.models import item
from django.template import loader
# Create your views here.

def index(request):
    items_list = item.objects.all()
    # template = loader.get_template('food/index.html')
    context = {
        'item_list':items_list
    }
    return render(request,'food/index.html',context)

def item_l(request):
    return HttpResponse("the page for item")

def detail(request,item_id):
    details = item.objects.get(pk = item_id)
    context = {
        'item_detail':details,
    }
    return render(request,'food/detail.html',context)
