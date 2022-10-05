from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Slider)
admin.site.register(Banner_area)
admin.site.register(Section)
@admin.register(Product)
class ProductCategoryAdmin(admin.ModelAdmin):
        list_display = [
        'category','sku','product_name','main_category','unit_price','created_date','modified_date'
        ]
       
        # list_filter = ['is_active','record_status','modified_date']
        
@admin.register(SubProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
        list_display = ['product','sub_product_totel_stoke','offerprice','offer_expiry_date','is_active']

@admin.register(SubProductAttributeImages)
class ProductAttributeImagesAdmin(admin.ModelAdmin):
        list_display = ['product_attribute','title','images']



@admin.register(ProductQuantity)
class ProductQuantityAdmin(admin.ModelAdmin):
        list_display = ['product','product_size','product_color','quantity','is_active']

