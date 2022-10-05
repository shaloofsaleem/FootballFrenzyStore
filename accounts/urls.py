from django.urls import path
from . import views as v
from . import verifiaction_email as verification
from . import verify_otp as otp
from . import account_deatails as a
app_name = 'accounts'


urlpatterns = [
    path('login',v.user_login,name='login'),
    path('registration',v.user_registration,name='registration'),
    path('activate/<uidb64>/<token>',verification.activate_email,name='activate_email'),
    path('check_mail',v.check_mail,name='check_mail'),
    path('otp-verify/<int:phone_no>/<int:uid>/<int:verification_user>',otp.otp_verify_code,name='otp_verify_code'),
    path('resent-otp',otp.resent_otp,name='resent_otp'),
    path('logout',v.user_logout,name='logout'),
    path('forget-password',v.forget_password,name='forget_password'),
    path('Reset-password-validate/<uidb64>/<token>',verification.Reset_password_validate,name='Reset_password_validate'),
    path('Reset-password/<int:uid>',v.Reset_password,name='Reset_password'),
    
    path('',a.accounts,name='accounts'),
    path('user-infermations',a.user_infermations,name='user_infermations'),
    path('user-address',a.user_address,name='user_address'),
    path('delete-user-address',a.delete_address,name='delete_address'),
    path('edit-user-address',a.edit_address,name='edit_address'),

    
    
    
    
    
    
    
    
    
]