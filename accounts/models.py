from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser):
    email               = models.EmailField(max_length=100,unique=True)
    phone_no            = models.CharField(max_length=50)
    first_name          = models.CharField(max_length=50)
    last_name           = models.CharField(max_length=50)
    gender              = models.CharField(max_length=20,null=True,blank=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=False)
    is_superadmin       = models.BooleanField(default=False)
    created_date        =   models.DateTimeField(auto_now_add=True)
    modified_date       =   models.DateTimeField(auto_now=True)
    record_status       =   models.CharField(max_length=255,default='created')
    objects =UserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['phone_no','first_name', 'last_name']
    
    def __str__(self) :
        return self.email
    
    def has_perm(self,prem,obj=None):
        return True
    
    def has_module_perms(self,app_lable):
        return True
    
    def fullname(self):
        return f"".format(self.first_name,self.last_name)


class VerificationUser(models.Model):
    user                = models.ForeignKey(User,on_delete=models.CASCADE,related_name='verifiaction_user')
    otp                 = models.IntegerField(blank=True,null=True)
    otp_verification    = models.BooleanField(default=False)
    email_verification  = models.BooleanField(default=False)
    otp_attempt         = models.IntegerField(default=0)
    otp_sent_date       = models.DateTimeField(auto_now=True)
    verification_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

class UserAddress(models.Model):
    user                = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_address')
    name                = models.CharField(max_length=250)
    phone_no            = models.CharField(max_length=50)
    pincode             =   models.CharField(max_length=250)
    locality            =   models.CharField(max_length=250)
    address             =   models.TextField()
    city_district_town  =   models.CharField(max_length=250)
    state               = models.CharField(max_length=250)
    landmark            =   models.CharField(max_length=250,blank=True,null=True)
    alt_phone_no        = models.IntegerField(blank=True,null=True)
    address_type        =  models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'User Address'