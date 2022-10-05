from django import template
from django.shortcuts import render,get_object_or_404
from category.models import *
from .models import *
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse,JsonResponse
from django.template.loader import render_to_string

def base(request):
    categorys=Category.objects.all()
    brands=Brand.objects.all()
    context={
        'category':categorys,
        'brand':brands,
    }
    return render(request,'user/base-layout.html',context)
    
    


def landing_page(request):
    slider=Slider.objects.all().order_by('-id')[0:3]
    banner=Banner_area.objects.all().order_by('-id')[0:3]
    product=SubProductAttribute.objects.filter(section__title="THE NEW ARRIVALS")
    category=Category.objects.all()
    brand=Brand.objects.all()
    print(product)
    context={
        'category':category,
        'slider':slider,
        'banner':banner,
        'product':product,
        'brand':brand,
    }
    return render(request,'user/landing-page/max-min.html',context)



def all_categories(request,*args,**kwargs):
    category = get_object_or_404(Category,pk=kwargs.get('pk')) 
    genter= kwargs.get('genter')
    try:
        if category.level == 0:
            product=SubProductAttribute.objects.select_related(
            'product','product__category',).filter(product__is_active=True,product__main_category=genter,product__category__parent_id=category.id)
            subcategory= Category.objects.filter(parent_id=category)
            brands= Brand.objects.filter(brand_category=category)
            size= Size.objects.filter(category=category)
            main_category = category.pk
        else:
            product=SubProductAttribute.objects.select_related(
            'product','product__category',).filter(product__is_active=True,product__main_category=genter,product__category=category)
            subcategory= Category.objects.filter(parent_id=category.parent_id)
            brands= Brand.objects.filter(brand_category=category.parent_id)
            size= Size.objects.filter(category=category.parent_id)
            main_category = category.parent_id
        color= Color.objects.all()
        paginator = Paginator(product, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except SubProductAttribute.DoesNotExist:
        raise Http404()
    context =   {
        'maincategory':main_category,
        'subcategory':subcategory,
        'products' : page_obj,
        'brands': brands,
        'size':size,
        'color':color,
    }
    return render(request,'user/products/products.html',context)



def filter_data(request):
    try:
        categories=request.GET.getlist('subcategory[]')
        brands=request.GET.getlist('brand[]')
        sizes=request.GET.getlist('size[]')
        color=request.GET.getlist('color[]')
        main_category=request.GET['category_id']
        allProduct=SubProductAttribute.objects.select_related(
            'product','product__category',).filter(product__is_active=True,product__category__parent_id=main_category)
        
        if len(categories)>0:
            allProduct=allProduct.filter(product__category__id__in=categories)
        if len(brands)>0:
            allProduct=allProduct.filter(product__product_brand__id__in=brands)
        if len(sizes)>0:
            sizeproduct=ProductQuantity.objects.filter(product_size__id__in=sizes)
            product = [ c.product for c in sizeproduct]
            product = [ c.id for c in product]
            allProduct=allProduct.filter(id__in=product)
        if len(color)>0:
            sizeproduct=ProductQuantity.objects.filter(product_color__id__in=color)
            product = [ c.product for c in sizeproduct]
            product = [ c.id for c in product]
            allProduct=allProduct.filter(id__in=product)
    except:
        pass    
    template =render_to_string('user/products/filter-data.html',{'data':allProduct})
    return JsonResponse({'data':template})  



def list_filter_data(request):
    try:
        categories=request.GET.getlist('subcategory[]')
        brands=request.GET.getlist('brand[]')
        sizes=request.GET.getlist('size[]')
        color=request.GET.getlist('color[]')
        main_category=request.GET['category_id']
        allProduct=SubProductAttribute.objects.select_related(
            'product','product__category',).filter(product__is_active=True,product__category__parent_id=main_category)
        
        if len(categories)>0:
            allProduct=allProduct.filter(product__category__id__in=categories)
        if len(brands)>0:
            allProduct=allProduct.filter(product__product_brand__id__in=brands)
        if len(sizes)>0:
            sizeproduct=ProductQuantity.objects.filter(product_size__id__in=sizes)
            product = [ c.product for c in sizeproduct]
            product = [ c.id for c in product]
            allProduct=allProduct.filter(id__in=product)
        if len(color)>0:
            sizeproduct=ProductQuantity.objects.filter(product_color__id__in=color)
            product = [ c.product for c in sizeproduct]
            product = [ c.id for c in product]
            allProduct=allProduct.filter(id__in=product)
    except:
        pass    
    template =render_to_string('user/products/list-filter.html',{'data':allProduct})
    return JsonResponse({'data':template})  



def single_Productdeatail(request,*args,**kwargs):
    # del request.session['cartdata']
    # del request.session['length_product']
    product=SubProductAttribute.objects.get(pk=kwargs.get('single_Productdeatail_pk'))
    productimages=SubProductAttributeImages.objects.filter(product_attribute__pk=kwargs.get('single_Productdeatail_pk'))
    related_product=SubProductAttribute.objects.filter(product__slug=kwargs.get('product_slug')).exclude(pk=kwargs.get('single_Productdeatail_pk'))
    product_qwantity  = ProductQuantity.objects.filter(product=product) 
    context={
        'product':product,
        'image':productimages,
        'related':related_product,
        'product_qwantity':product_qwantity,
        
    }
    return render(request,'user/single-product-section/single-product.html',context)


def Product_view(request):
    product=SubProductAttribute.objects.all()
    productimages=SubProductAttributeImages.objects.all()
    related_product=SubProductAttribute.objects.all()
    product_qwantity  = ProductQuantity.objects.all()
    p = Paginator(product, 5)  # creating a paginator object
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnIntege:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    category=Category.objects.all()
    brand=Brand.objects.all()
    color=Color.objects.all()
    Colorid=request.GET.get('color')
    Brandid=request.GET.get('brand')
    if Colorid:
        product=SubProductAttribute
    context={
        'product':product,
        'page_obj': page_obj,
        'image':productimages,
        'related':related_product,
        'product_qwantity':product_qwantity,
        'category':category,
        'brand': brand,
        'color':color,
        
        
    }
    return render(request,'user/All Product/product.html',context)

def category_products(request,slug,id): 
    product=SubProductAttribute.objects.filter(product__id=id)
    category=Category.objects.all()
    brand=Brand.objects.all()
    color=Color.objects.all()
    context={
        'product':product,
        'category':category,
        'brand': brand,
        'color':color
    }
    
    return render (request,'user/All Product/category_product.html',context)
    
    