from django.urls import path
from . import orders_placed as v
from . import rezorpay as r
from . import paypal as p
from . import invoice as i

app_name = 'payment'
urlpatterns = [
    path('text-genarator',v.cash_on_delivery_code_genarator,name='cash_on_delivery_code_genarator'),
    path('cash-on-delivery-order-confrim/<str:product_order_session_id>/',v.cash_on_delivery_order_confrim,name='cash_on_delivery_order_confrim'),
    path('order-placed/<str:order_id>/<str:payment_id>/<str:order_status_id>',v.order_placed,name='order_placed'),
    path('order-deatails',v.order_deatails,name='order_deatails'),
    
    path('cancel-order',v.cancel_order,name='cancel_order'),
    path('search-order',v.search_order,name='search_order'),
    path('filter-orders',v.filter_orders,name='filter_orders'),
    path('order-placed-history/orderid=<str:id>&<int:orderpk>&itemid=<int:itemid>&statusid=<int:sid>',v.order_placed_history,name='order_placed_history'),
    
    path('razorpay-payment/<str:product_order_id>/',r.razorpay_payment,name='razorpay_payment'),
    path('paypal',p.paypal,name='paypal'),
    
    path('invoice&order_id=<int:order_id>&order_status=<int:orderstatus>',i.invoice,name='invoice'),
    
    
    
    
    

       
       
]