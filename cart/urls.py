from django.urls import path
from . import views as v
from . import checkout as c
from . import order as o
from . import whishlist as w


app_name = 'cart'
urlpatterns = [
    
    path('',v.add_to_cart,name='add_to_cart'),
    path('quantity',v.quantity,name='quantity'),
    path('view-cart',v.cart,name='cart'),
    path('price-change',v.price_change,name='price_change'),
    path('size-change',v.size_change,name='size_change'),
    path('delete-cart-items',v.deleted_cart_items,name='deleted_cart_items'),
    path('wishlist/', w.wishlist, name='wishlist'),
    path('wislist/add-to-wislist/<int:product_id>/', w.add_to_wishlist, name='add-to-wishlist'),
    path('wislist/remove-from-wislist/<int:product_id>/', w.remove_from_wishlist, name='remove-from-wishlist'),
    
    path('checkout',c.checkout,name='checkout'),
    path('delivery-address',c.delivery_address,name='delivery_address'),
    path('edit-checkout-address',c.edit_checkout_address,name='edit_checkout_address'),
    path('delete-checkout-items',c.delete_checkout_items,name='delete_checkout_items'),
    path('add-checkout-new-address',c.add_checkout_new_address_form,name='add_checkout_new_address_form'),
    
    path('continue-order',o.continue_order,name='continue_order'),
    path('coupon',o.coupon,name='coupon'),
    
    
    
    
    
    
    
    
]