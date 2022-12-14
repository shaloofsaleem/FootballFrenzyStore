from django.urls import path
from .import views
from .import Admin_views


urlpatterns = [
    path('adminn',views.Adminlogin,name='adminn'),
    path('user/',Admin_views.Users,name="user"),
    path('invoice/',views.View_invoice,name="invoice"),
    
    # path('user/search/',Admin_views.UsersSearch,name="user-search"),
    path('user-management/block/<str:pk>/', Admin_views.block_user , name='block-user'),
    path('user-management/unblock/<str:pk>/', Admin_views.unblock_user , name='unblock-user'),
    path('',Admin_views.Adminhome,name='home'),
    path('logout',views.Adminlogout,name='logout'), 
    path('category/',views.View_Category,name="category"),
    # path('carts/',views.View_Cart,name="carts"),
     path('Orders/',views.View_OrderStuts,name="Orders"),
    # path('i/',views.View_Order,name="invoice"),
    path('quanty/',views.View_Quantity,name="quanty"),
    path('subprodt/',views.View_Subprdt,name="subprodt"),
    path('image/',views.View_Image,name="image"),
    path('color/',views.View_Color,name="color"),
    path('brand/',views.View_Brand,name="brand"),
    path('product/',views.View_Product,name="product"),
    path('size/',views.View_Size,name="size"),
    path('category_create/',views.Add_Category,name="category_create"),
    path('product_add/',views.Add_Product,name="product_add"),
    path('subproduct_add/',views.Add_SubProduct,name="subproduct_add"),
    path('proqunt_add/',views.Add_ProductQunt,name="proqunt_add"),
    path('image_add/',views.Add_Image,name="image_add"),
    path('color_add/',views.Add_Color,name="color_add"),
    path('size_add/',views.Add_Size,name='size_add'),
    path('brand_add/',views.Add_Brand,name='brand_add'),
    path('stuts_add/',views.Add_Orderstuts,name='stuts_add'),
    path('sizupdate/<int:id>',views.Update_Size,name="sizupdate"),
    path('colupdate/<int:id>',views.Update_Color,name="colupdate"),
    path('catupdate/<int:id>',views.Update_Category,name="catupdate"),
    path('prodpdate/<int:id>',views.Update_Produect,name="produpdate"),
    path('subupdate/<int:id>',views.Update_Subprodt,name="subupdate"),
    path('qupdate/<int:id>',views.Update_Quantity,name="qupdate"),
    path('qdelete/<int:id>',views.Quantity_delete,name="qdelete"),
    path('brandupdate/<int:id>',views.Update_Brand,name="brandpdate"),
    path('imageupdate/<int:id>',views.Update_Brand,name="imageupdate"),
    path('imagedelete/<int:id>',views.Image_delete,name="imagedelete"),
    path('catdelete/<int:id>',views.Category_delete,name="catdelete"),
    path('proddelete/<int:id>',views.Product_delete,name="proddelete"),
    path('brandelete/<int:id>',views.Brand_delete,name="branddelete"),
    path('coldelete/<int:id>',views.Color_delete,name="coldelete"),
    path('sizdelete/<int:id>',views.Size_delete,name="sizdelete"),
    
    
] 