from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from accounts.views import *
from django.contrib.auth import get_user_model
from category.models import *
from cart.models import *
from payment.models import *


#Create your views here.
@never_cache
@login_required(login_url= 'adminn')
def Adminhome(request):
    order= Order.objects.filter(is_active=True).count()
    product_count = Product.objects.all().count()
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
        'product_count':product_count
    }
    return render(request,'admin/admin-home.html', context)
@never_cache
@staff_member_required
@login_required(login_url= 'adminn')
def Users(request):
    Users = get_user_model()
    if 'key' in request.GET:
        key = request.GET['key']
        users = Users.objects.filter(email__icontains=key)
    else:
        users = Users.objects.all()
    return render(request, 'admin/user.html', {'user': users})

@staff_member_required
@login_required(login_url= 'adminn')
def UsersSearch(request): 
    if 'key' in request.GET:
        key = request.GET['key']
        Users = get_user_model()
        users = Users.objects.all(email__icontains=key)
    else:
        users=None
    return render(request, 'admin/user.html', {'user': users})


@login_required(login_url= 'adminn')
def block_user(request, pk):
    user = User.objects.get(pk = pk)
    user.is_active = False
    user.save()
    return redirect(Users)


@login_required(login_url= 'adminn')
def unblock_user(request, pk):
    user = User.objects.get(pk = pk)
    user.is_active = True
    user.save()
    return redirect(Users)
       
   