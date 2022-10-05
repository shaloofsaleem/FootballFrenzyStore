from django.shortcuts import render,get_object_or_404,redirect
from cart.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt

from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.core.cache import cache
CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)
from datetime import timedelta
import base64
from django.utils import timezone
from cart.order import get_client_ip
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
import json


def paypal_payment(request):
    body=json.loads(request.body)
    print(body)
    return render (request,'user/order/paypal.html')