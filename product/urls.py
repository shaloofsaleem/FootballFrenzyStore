from django.urls import path
from . import views as a
from . import user_product_section as u
app_name = 'product'


urlpatterns = [
    path('',u.landing_page,name='landing_page'),
    path('??/<int:pk>/<slug:product_name>/<int:genter>',u.all_categories,name="allcategories"),
    path('?/filter-data',u.filter_data,name='filter_data'),
    path('?/list-filter-data',u.list_filter_data,name='list_filter_data'),
    path('<slug:product_slug>/<int:single_Productdeatail_pk>',u.single_Productdeatail,name="single_Productdeatail"),
    path('all_product/',u.Product_view,name="all_product"),
    path('category/<int:id>/<slug:slug>',u.category_products,name="category_products"),
    path('search/', a.search, name='search'),
    path('base',u.base)
 
    
]