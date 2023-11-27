from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import userLogin

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userLogin(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"welcome {username}")
            return redirect('food:Index')
    form = userLogin()
    return render(request,"users/register.html",{'form':form})
    
