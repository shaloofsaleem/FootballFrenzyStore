from .models import Whishlist


def wishlist_counter(request):
    wishlist_counter=0
    wishlist = Whishlist.objects.filter(user=request.user.id)
    wishlist_counter = wishlist.count()
    return dict(wishlist_counter = wishlist_counter)

    
   