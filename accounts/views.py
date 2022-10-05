from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import ReistrationForm,LoginForm,ResetPasswod
from .models import User
from .verify_otp import send_otp
# Create your views here.

# email send django library functions
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from django.db.models import Sum
from cart.models import Cart
from product.models import ProductQuantity

import requests


def check_mail(request):
    return render(request,'user/accounts/email-check.html')

def user_registration(request,*args,**kwrgs):
    if request.method == 'POST':
        choice = request.POST['option']
        form = ReistrationForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            phone_no=form.cleaned_data['phone_no']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            password=form.cleaned_data['password']
            user=User.objects.create_user(email=email,phone_no=phone_no,first_name=first_name,last_name=last_name,password=password)
            user.save()
            if choice == 'email':
                current_site = get_current_site(request)
                mail_subject = "Please active your account"
                massage = render_to_string('user/accounts/verification-email.html',
                    {
                    'user':user,
                    'domain'  : current_site,
                    # user pk encode 
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    # user token genarete
                    'token': default_token_generator.make_token(user),
                })
                to_email=email
                send_email = EmailMessage(mail_subject,massage,to=[to_email])
                send_email.send()
                return redirect('accounts:check_mail')
            else:
                verification_user=send_otp(phone_no,user)
                return redirect('accounts:otp_verify_code',phone_no=phone_no,uid=user.pk,verification_user=verification_user)
        else:
            messages.warning(request,'Form not submition try again...')
            return redirect('accounts:registration')
                
    form = ReistrationForm()
    return render(request,'user/accounts/registration.html',{'form':form})



def user_login(request,*args,**kwrgs):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                
                if 'cartdata' in request.session:
                    session_data=request.session['cartdata']
                    for key,val in session_data.items():
                        cart=Cart()
                        cart.user=request.user
                        product_quantity = ProductQuantity.objects.get(pk=int(key))
                        cart.product_quantity=product_quantity
                        cart.product=product_quantity.product
                        cart.session_id=request.session.session_key
                        cart.unit_price=product_quantity.product.product.unit_price
                        cart.product_qty=val['product_qty']
                        cart.product_price=val['price']
                        cart.totel_qty_price=val['sub_totel_price']
                        cart.save()
                    del request.session['cartdata']
                
                data=Cart.objects.filter(user=request.user,is_active=True).aggregate(Sum('product_qty'))
                length_product=data['product_qty__sum']
                request.session['length_product']=length_product
                
                # redirect paths location 
                url =request.META.get('HTTP_REFERER')
                # http://127.0.0.1:8000/accounts/login 
                try:
                    query = requests.utils.urlparse(url).query
                    # next=/accounts/
                    print(query,'**********************************')
                    params=dict(x.split('=') for x in query.split('&'))
                    # {'next': '/accounts/'}
                    print(params,'**********************************')
                    if 'next' in params:
                        nextPage = params['next']
                        return redirect(nextPage)        
                except:
                    return redirect('product:landing_page')
          
            else :
                messages.warning(request,'Incorrect Username or Password')
                return redirect('accounts:login') 
    form= LoginForm()
    return render(request,'user/accounts/login.html',{'form':form})


@login_required(login_url='accounts:login')
def user_logout(request,*args,**kwrgs):
    logout(request)
    return redirect('accounts:login') 



def forget_password(request,*args,**kwrgs):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user =User.objects.get(email__exact=email)
            current_site = get_current_site(request)
            mail_subject = "Reset Your Password"
            massage = render_to_string('user/accounts/reset-password-email.html',
                {
                'user':user,
                'domain'  : current_site,
                # user pk encode 
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # user token genarete
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            send_email = EmailMessage(mail_subject,massage,to=[to_email])
            send_email.send()
            return redirect('accounts:check_mail')
        else:
            messages.warning(request,'Email Not Exists , try another email')
            return redirect('accounts:forget_password')         
    return render(request,'user/accounts/forget-password.html')


def Reset_password(request,uid):
    if request.method == 'POST':
        form=ResetPasswod(request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            user=User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
    form=ResetPasswod()
    return render(request,'user/accounts/reset-password.html',{'form':form})