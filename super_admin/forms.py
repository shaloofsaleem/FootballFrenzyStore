from cart.models import *
from .models import *
from django import forms
from category.models import*
from product.models import *




class CatgoryModel(forms.ModelForm):
    class Meta:
        model=Category
        fields= "__all__"
class SizeModel(forms.ModelForm):
    class Meta:
        model=Size
        fields="__all__"    
class BrandModel(forms.ModelForm):
    class Meta:
        model=Brand
        fields="__all__"            
class ColorModel(forms.ModelForm):
    class Meta:
        model=Color
        fields="__all__" 
class SliderModel(forms.ModelForm):
    class Meta:
        model=Slider    
        fields= "__all__"
class Banner_areaModel(forms.ModelForm):
    class Meta:
        model=Banner_area    
        fields= "__all__"                
class  SectionModel(forms.ModelForm):
    class Meta:
        model= Section   
        fields= "__all__"  
class ProductModel(forms.ModelForm):
    class Meta:
        model=Product     
        exclude = ['slug']
class SubProductModel(forms.ModelForm):
    class Meta:
        model=SubProductAttribute     
        fields= "__all__"
class ImageProductModel(forms.ModelForm):
    class Meta:
        model=SubProductAttributeImages     
        fields= "__all__"
class ProductQuntModel(forms.ModelForm):
    class Meta:
        model=ProductQuantity     
        fields= "__all__"
                
class CartModel(forms.ModelForm):
    class Meta:
        model=Cart
        fields= "__all__"                
        
       
class OrderStatusModel(forms.ModelForm):
    class Meta:
        model=OrderStatus
        fields= "__all__"           
class OrdereModel(forms.ModelForm):
    class Meta:
        model=Order
        fields= "__all__"           