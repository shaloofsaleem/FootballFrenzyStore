from django.shortcuts import render
from accounts.views import *
from .forms import *
from .Admin_views import  *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def Adminlogin(request):
    if request.user.is_authenticated:
        return redirect(Adminhome)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request , email = email , password = password)
        print(user)
        if user is not None:
            user = User.objects.get(email=email)
            if user.is_admin == True:
                login(request , user)
            else:
                messages.error(request , 'User is not found')
                return redirect(Adminlogin)
        else:
            messages.error(request , 'User is not found')
            print('user is none')
    return render(request,'admin/admin-login.html')
@never_cache    
def Adminlogout(request):
    if request.user.is_authenticated:  
      logout(request)
      messages.success(request,'Logout Successfully!')
    return redirect(Adminlogin)    
def Add_Orderstuts(request):
    if request.method == "POST":
        form =OrderStatusModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(Add_Orderstuts)
        else:
            print('order not added')
            messages.info(request,'product not added')
    else:
        form =OrderStatusModel()
    return render(request,'admin/cart/stuts.html',{'form':form}) 

def Add_Category(request):
    if request.method == "POST":
        form =CatgoryModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(Add_Category)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form = CatgoryModel()
    return render(request,'admin/category/admin-category_create.html',{'form':form})      
def Add_Product(request):
    if request.method == "POST":
        form =ProductModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(Add_Product)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form =ProductModel()
    return render(request,'admin/Product/admin-product_Add.html',{'form':form}) 
  
def Add_Size(request):
    if request.method == "POST":
        form =SizeModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(View_Size)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form =SizeModel()
    return render(request,'admin/category/admin-size.html',{'form':form})   
def Add_Brand(request):
    if request.method == "POST":
        form =SizeModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(Add_Brand)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form =BrandModel()
    return render(request,'admin/category/admin-brand.html',{'form':form})        

def Add_Color(request):
    if request.method == "POST":
        form =ColorModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(Add_Color)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form=ColorModel()
    return render(request,'admin/category/admin-color.html',{'form':form}) 
def Add_SubProduct(request):
    if request.method == "POST":
        form =SubProductModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(View_Subprdt)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form =SubProductModel()
    return render(request,'admin/Product/admin-subproduct.html',{'form':form}) 

def Add_ProductQunt(request):
    if request.method == "POST":
        form =ProductQuntModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(View_Quantity)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form =ProductQuntModel()
    return render(request,'admin/Product/admin-product_quntity.html',{'form':form})    
def Add_Image(request):
    if request.method == "POST":
        form =ImageProductModel(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('data saved successfully')
            return redirect(Add_Image)
        else:
            print('product not added')
            messages.info(request,'product not added')
    else:
        form =ImageProductModel()
    return render(request,'admin/Product/admin-image.html',{'form':form})  
def Update_Size(request, id) :
    size = Size.objects.get(id=id)
    if request.method == 'POST' :
        form = SizeModel(request.POST, request.FILES, instance=size)   
        if form.is_valid() :
            form.save()
            return redirect(View_Size)    
    form = SizeModel(instance=size)
    context = {'form' : form}
    return render(request, 'admin/category/admin-size.html', context)     
def Update_Color(request, id) :
    color = Color.objects.get(id=id)
    if request.method == 'POST' :
        form = ColorModel(request.POST, request.FILES, instance=color)   
        if form.is_valid() :
            form.save()
            return redirect(View_Color)    
    form =ColorModel(instance=color)
    context = {'form' : form}
    return render(request, 'admin/category/admin-color.html', context)             
def Update_Brand(request, id) :
    brand = Brand.objects.get(id=id)
    if request.method == 'POST' :
        form = BrandModel(request.POST, request.FILES, instance=brand)   
        if form.is_valid() :
            form.save()
            return redirect(View_Brand)    
    form = BrandModel(instance=brand)
    context = {'form' : form}
    return render(request, 'admin/category/admin-brand.html', context)
def Update_Quantity(request, id) :
    quantity = ProductQuantity.objects.get(id=id)
    if request.method == 'POST' :
        form = ProductQuntModel(request.POST, request.FILES, instance=quantity)   
        if form.is_valid() :
            form.save()
            return redirect(View_Quantity)    
    form = ProductQuntModel(instance=quantity)
    context = {'form' : form}
    return render(request, 'admin/Product/admin-product_quntity.html', context)  
def Update_Category(request, id) :
    category = Category.objects.get(id=id)
    if request.method == 'POST' :
        form = CatgoryModel(request.POST, request.FILES, instance=category)   
        if form.is_valid() :
            form.save()
            return redirect(View_Category)    
    form = CatgoryModel(instance=category)
    context = {'form' : form}
    return render(request, 'admin/category/admin-category_create.html', context)
def Update_Produect(request, id) :
    category = Product.objects.get(id=id)
    if request.method == 'POST' :
        form = ProductModel(request.POST, request.FILES, instance=category)   
        if form.is_valid() :
            form.save()
            return redirect(View_Product)    
    form = ProductModel(instance=category)
    context = {'form' : form}
    return render(request, 'admin/Product/admin-product_Add.html', context) 
def Update_Subprodt(request, id) :
    image = SubProductAttribute.objects.get(id=id)
    form = SubProductModel(instance=image)   
    if request.method == 'POST' :
        form = SubProductModel(request.POST, request.FILES, instance=image)   
        if form.is_valid() :
            form.save()
            return redirect(View_Subprdt)    
    context = {'form' : form}
    return render(request, 'admin/Product/admin-subproduct.html', context)
def Update_Image(request, id) :
    image = SubProductAttributeImages.objects.get(id=id)
    if request.method == 'POST' :
        form = ImageProductModel(request.POST, request.FILES, instance=image)   
        if form.is_valid() :
            form.save()
            return redirect(View_Image)    
    form = ProductModel(instance=image)
    context = {'form' : form}
    return render(request, 'admin/Product/admin-image-list.html', context)   
def Category_delete(request, id) :
    if request.method == 'GET' :
        category_id = Category.objects.get(pk=id)
        category_id.delete()
    return redirect(View_Category)
def Product_delete(request, id) :
    if request.method == 'GET' :
        product_id = Product.objects.get(pk=id)
        product_id.delete()
    return redirect(View_Product) 
def Image_delete(request, id) :
    if request.method == 'GET' :
        image_id = SubProductAttributeImages.objects.get(pk=id)
        image_id.delete()
    return redirect(View_Image) 
def Quantity_delete(request, id) :
    if request.method == 'GET' :
        quant_id = ProductQuantity.objects.get(pk=id)
        quant_id.delete()
    return redirect(View_Quantity)  
def Brand_delete(request, id) :
    if request.method == 'GET' :
        brand_id = Brand.objects.get(pk=id)
        brand_id.delete()
    return redirect(View_Brand) 
def Color_delete(request, id) :
    if request.method == 'GET' :
        color_id = Color.objects.get(pk=id)
        color_id.delete()
    return redirect(View_Color)
def Size_delete(request, id) :
    if request.method == 'GET' :
        size_id = Size.objects.get(pk=id)
        size_id.delete()
    return redirect(View_Color)
def View_Category(request):
    category = Category.objects.all()
    context = {"category": category}
    return render(request, "admin/category/admin-category_list.html", context)      
def View_Product(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, "admin/Product/admin-product_list.html", context)
def View_Image(request):
    image = SubProductAttributeImages.objects.all()
    context = {"image": image}
    return render(request, "admin/Product/admin-image-list.html", context)
def View_Subprdt(request):
    sub = SubProductAttribute.objects.all()
    context = {"sub": sub}
    return render(request, "admin/Product/admin-subproduct-list.html", context)
def View_Quantity(request):
    quanty = ProductQuantity.objects.all()
    context = {"quanty": quanty}
    return render(request, "admin/Product/admin-product_quntity-list.html", context)    
def View_Brand(request):
    brand = Brand.objects.all()
    context = {"brand": brand}
    return render(request, "admin/category/admin-brand_list.html", context) 
def View_Size(request):
    size = Size.objects.all()
    context = {"size": size}
    return render(request, "admin/category/admin-size_list.html", context)
def View_Color(request):
    color = Color.objects.all()
    context = {"color":color}
    return render(request, "admin/category/admin-color_list.html", context)

def View_Order(request):
    order = Order.objects.all()
    print(order)
    context = {"order": order}
    return render(request, "admin/cart/order list.html", context)
def View_OrderStuts(request):
    orders = OrderStatus.objects.all()
    context = {"orders": orders}
    return render(request, "",context)
def View_Cart(request):
    cart = Cart.objects.all()
    print(cart)
    context = {"cart": cart}
    return render(request, "",context)
