from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from accounts.views import *
from django.contrib.auth import get_user_model
from category.models import *
from cart.models import *
from payment.models import *


#Create your views here.
@login_required(login_url='home')    
@never_cache
def Adminhome(request):
    order= Order.objects.filter(is_active=True).count()
    sale = Payment.objects.filter(payment_complete_status=True)
    complete=Payment.objects.filter(payment_complete_status=True).count()
    shiping=OrderStatus.objects.filter(Shipped=True).count()
    User = get_user_model()
    user= User.objects.filter(is_active=True).count()
    total_sales=0
    for i in sale:
        total_sales+= i.payment_price
        print(total_sales)
    context={
        'ordercount':order,
        'total_sales':total_sales,
        'complete': complete,
        'shiping' :shiping,
        'user':user,
    }
    return render(request,'admin/admin-home.html', context)
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
       
   