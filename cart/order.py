from datetime import datetime
from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import User,UserAddress
from .models import *
from django.http import JsonResponse
from django.db.models import Sum
from django.utils import timezone
from django.template.loader import render_to_string

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def continue_order(request,*args,**kwargs):        
    address_id = request.POST.get('address_id', None)
    if 'order_id' in request.session:
        order=get_object_or_404(Order,pk=request.session['order_id'])
        order.user=request.user
        order.delivery_address=get_object_or_404(UserAddress,pk=address_id)
        order.order_confirmation_email=request.user.email
        products=Cart.objects.filter(user=request.user,is_active=True)
        totel_quantity=0
        totel_unit_price=0
        totel_offer_price=0
        for i in products:
            totel_quantity += i.product_qty
            totel_unit_price += i.totel_unit_price
            totel_offer_price += i.totel_qty_price
        order.totel_quantity=totel_quantity
        order.totel_unit_price=totel_unit_price
        order.totel_offer_price=totel_offer_price
        order.totel_payment_price=order.totel_offer_price
        order.ip=get_client_ip(request)
        order.offer_savings_price = totel_unit_price-totel_offer_price
        order.order_status='pending'
        order.save()
        for i in products:
            order.products.add(i.id)     
        cart_checkout_products=products.aggregate(Sum('product_qty'))
        totel_items_checkout=cart_checkout_products['product_qty__sum']
    else:
        order= Order()
        order.user=request.user
        order.delivery_address=get_object_or_404(UserAddress,pk=address_id)
        order.order_confirmation_email=request.user.email
        products=Cart.objects.filter(user=request.user,is_active=True)
        totel_quantity=0
        totel_unit_price=0
        totel_offer_price=0
        for i in products:
            totel_quantity += i.product_qty
            totel_unit_price += i.totel_unit_price
            totel_offer_price += i.totel_qty_price
        order.totel_quantity=totel_quantity
        order.totel_unit_price=totel_unit_price
        order.totel_offer_price=totel_offer_price
        order.totel_payment_price=order.totel_offer_price
        order.offer_savings_price = totel_unit_price-totel_offer_price
        order.order_status='pending'
        order.save()
        for i in products:
            order.products.add(i.id)
            
    cart_checkout_products=products.aggregate(Sum('product_qty'))
    totel_items_checkout=cart_checkout_products['product_qty__sum']
    totel_payment_price=order.totel_payment_price
    request.session['order_id']=order.id
    return JsonResponse({'data':True,'totel_items_checkout':totel_items_checkout,'totel_payment_price':totel_payment_price})



def coupon(request,*args,**kwargs): 
    Couponcode = request.POST.get('Couponcode', None)
    coupon=Coupon.objects.filter(coupon__exact=Couponcode,is_active=True)
    msg=''
    order={}
    status=False
    if coupon.exists():
            if coupon.filter(expiry_date__gte=timezone.now()):
                order=get_object_or_404(Order,pk=request.session['order_id'])
                if order.totel_offer_price > coupon[0].gtr_price:
                    pers = coupon[0].minus_pers
                    order.coupon_text=Couponcode
                    order.coupon=coupon[0]
                    order.coupon_price=order.totel_offer_price*pers
                    order.totel_payment_price=order.coupon_price
                    order.coupon_savings_price=order.totel_offer_price - order.coupon_price
                    order.coupen_active=True
                    order.save()
                    status=True
                    print('msg')
                    print(request.session['order_id'])
                else:
                    msg='coupen apply greater {} amount , sorry .....'.format(coupon[0].gtr_price)
                    print(msg)
                    status=False
            else:
                msg='coupon expired'  
                print(msg)
                status=False 
    else:
        msg='sorry, coupon not exists, use another'  
        print(msg)
        status=False
    template =render_to_string('user/order/order-totel.html',{'order':order})
    return JsonResponse({'data':status,'msg':msg,'template':template,})
    