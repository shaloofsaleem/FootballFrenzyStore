from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from accounts.views import *

from category.models import *


#Create your views here.
@login_required(login_url='home')    
@never_cache
def Adminhome(request):
    return render(request,'admin/admin-home.html')
@never_cache
def Users(request):
    if request.user.is_admin:
        search_key = request.GET.get('key')  if request.GET.get('key') != None  else ''
        users = User.objects.filter(email__istartswith=search_key,)
        return render(request, 'admin/user.html', {'user': users})
    else:
        return redirect('User')  


@login_required(login_url= 'admin-login')

def block_user(request, pk):
    user = User.objects.get(pk = pk)
    user.is_active = False
    user.save()
    return redirect(Users)


@login_required(login_url= 'admin-login')
def unblock_user(request, pk):
    user = User.objects.get(pk = pk)
    user.is_active = True
    user.save()
    return redirect(Users)
       
   