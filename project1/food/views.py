from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from food.models import item
# from django.template import loader
from food.form import addItem
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.

# def index(request):
#     items_list = item.objects.all()
#     # template = loader.get_template('food/index.html')
#     context = {
#         'item_list':items_list
#     }
#     return render(request,'food/index.html',context)

#Class based index view

class index(ListView):
    model = item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item_l(request):
    return HttpResponse("the page for item")

# def detail(request,item_id):
#     details = item.objects.get(pk = item_id)
#     context = {
#         'item_detail':details,
#     }
#     return render(request,'food/detail.html',context)

# Class based detail view

class detail(DetailView):
    model = item
    template_name = 'food/detail.html'


# def add_Item(request):
#     form = addItem(request.POST or None)
    
#     if form.is_valid():
#         form.save()
#         return redirect('food:Index')
#     return render(request,'food/add.html',{'form':form})

# Class based Create view

class add_Item(CreateView):
    model = item
    fields = ['item_name','item_desc','item_price','item_img']
    template_name = 'food/add.html'
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def edit_item(request,id):
    item_details = item.objects.get(pk = id)
    form = addItem(request.POST or None,instance=item_details)
    
    if form.is_valid():
        form.save()
        return redirect('food:Index')
    return render(request,'food/add.html',{'form':form})

def item_delete(request,id):
    
    item_details = item.objects.get(pk = id)
    if item_delete != None:
        item_details.delete()
        return redirect('food:Index')
    return render(request,'food/detail.html')

@login_required
def profile(request):
    return render(request,'food/profile.html')
