from django.db import models
import random
import os
from category.models import *
from autoslug import AutoSlugField



# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    # print(base_name,' basename') #20210623_181743.jpg  basename
    ext = os.path.splitext(base_name)
    # print(ext,' extention')  #('20210623_181743', '.jpg')  extention
    return ext

def upload_image_path(instance, filename):
    # print(filename,' filename')
    new_filename = random.randint(1,3910209312)
    # print(new_filename,' random')  # like -> 2727979836  random
    ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    # print(final_filename,' final_filename')  #2727979836('20210623_181743', '.jpg')  final_filename
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

#***************************home page***************************************
class Slider(models.Model):
   image= models.ImageField(upload_to=upload_image_path, null=True, blank=True,)
   title=models.CharField(max_length=200)
   Name=models.CharField(max_length=300)
    
   def __str__(self):
        return self.Name


class Banner_area(models.Model):
    title=models.CharField(max_length=200)
    image= models.ImageField(upload_to=upload_image_path, null=True, blank=True,)
    def __str__(self):
        return self.title

class  Section (models.Model):       
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
#*************************** category choice ********************************


#*************************** category choice ********************************

CHOICES = [
    ('1', 'Man'),
    ('2', 'Woman'),
    ('3', 'Kids'),
]

#*************************** product table  ********************************

class Product(models.Model):
    category        =   models.ForeignKey(Category,null=True, blank=True,on_delete=models.CASCADE,related_name='product_reference_sub_category')
    product_brand   =   models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='product_reference_brand')
    main_category   =   models.CharField(max_length=255,choices=CHOICES,blank=True,null=True)
    sku             =   models.CharField(max_length=355,blank=True,unique=True)
    product_name    =   models.CharField(max_length=255)
    slug            =   AutoSlugField(populate_from='product_name',unique_with=('sku'),max_length=255,unique=True,null=True )
    unit_price      =   models.DecimalField(decimal_places=2,max_digits=8)
    description     =   models.TextField(blank=True,null=True)
    product_totel_stoke = models.IntegerField(blank=True,null=True)
    is_active       =   models.BooleanField(default=True)
    created_date    =   models.DateTimeField(auto_now_add=True)
    # created_id      =   models.ForeignKey(User,on_delete=models.CASCADE,related_name='Products_created_id')
    # created_ip      =   models.GenericIPAddressField()
    modified_date   =   models.DateTimeField(auto_now=True)
    # modified_id     =   models.ForeignKey(User,on_delete=models.CASCADE,related_name='Products_modified_id')
    # modified_ip     =   models.GenericIPAddressField()
    # record_status   =   models.CharField(max_length=255,default='created')  
      

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Product'
        ordering = ('-created_date',)
        
        



class SubProductAttribute(models.Model):
    product        = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='sub_product_reference_main_product')
    images           = models.ImageField(upload_to=upload_image_path, null=True, blank=True,)
    images2           = models.ImageField(upload_to=upload_image_path, null=True, blank=True,)
    sub_product_totel_stoke = models.IntegerField(blank=True,null=True)
    offerprice       =   models.DecimalField(decimal_places=2,max_digits=8)
    offer_persentage     =   models.FloatField(blank=True,null=True)
    offer_expiry_date    =  models.DateTimeField(blank=True,null=True)
    is_active    =   models.BooleanField(default=True)
    section         = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return '{} {}'.format(self.product.product_name,self.pk)

    class Meta:
        verbose_name_plural = 'sub Product Attribute'


    def save(self, *args, **kwargs):
        self.offer_persentage = round((100-(self.offerprice / self.product.unit_price)*100),2)
        return super().save(*args, **kwargs)

    def get_absolute_url(self): 
        return reverse('product:single_Productdeatail', args=[self.product.slug,self.pk])



    

class SubProductAttributeImages(models.Model):
    product_attribute = models.ForeignKey(SubProductAttribute,on_delete=models.CASCADE,related_name='sub_product_images_reference_sub_product')
    title   = models.CharField(max_length=255,blank=True)
    images  = models.ImageField(upload_to=upload_image_path, null=True, blank=True,)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'sub product attribute image'




class ProductQuantity(models.Model):
    product     =   models.ForeignKey(SubProductAttribute,on_delete=models.CASCADE,related_name='Product_Quantity_referece_offer_product')
    product_size =  models.ForeignKey(Size,on_delete=models.CASCADE,related_name='attribute_size_reference_sub_product')
    product_color = models.ForeignKey(Color,on_delete=models.CASCADE,related_name='attribute_color_reference_sub_product')
    quantity    =   models.IntegerField(default=1)
    stock        =   models.IntegerField(default=1)
    is_active   =   models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Product Quantity'

    def __str__(self):
        return '{} ({})'.format(self.product,self.product.product.product_name)

    def save(self, *args, **kwargs):
        self.stock = self.quantity
        return super().save(*args, **kwargs)
    

