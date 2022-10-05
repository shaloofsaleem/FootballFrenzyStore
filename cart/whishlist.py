from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from django .contrib import messages
from. models import *
from accounts.models  import*
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def wishlist(request):
  try:
    wishlist_items =  Whishlist.objects.filter(user=request.user).order_by('-created_date')
    # wishlist_count = wishlist_items.count()
  except:
    wishlist_items = None
    # wishlist_count= 0
  print(wishlist_items)
  context = {
    'wishlist_items': wishlist_items,
    # 'wishlist_count': wishlist_count
  }
  print(wishlist_items)
  return render(request, 'user/wishlist/wishlist.html', context)


@login_required(login_url='accounts:login')
def add_to_wishlist(request, product_id):
  url=request.META.get('HTTP_REFERER')
  in_wishlist =  Whishlist.objects.filter(user=request.user, product_id= product_id).exists()
  if in_wishlist:
    return redirect(url)
  else:
     Whishlist.objects.create(
      user = request.user,
      product_id = product_id
    )
  return redirect(url)


@login_required(login_url='accounts:login')
def remove_from_wishlist(request, product_id):
  in_wishlist = Whishlist.objects.filter(user=request.user, product_id= product_id).exists()
  if in_wishlist:
    wishlist_item = Whishlist.objects.get(user=request.user, product_id=product_id)
    wishlist_item.delete()
    return redirect('wishlist')
  else:
    return redirect(wishlist)