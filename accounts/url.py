from django.urls import path
from django.contrib.auth import views as auth_view
from . views import *

urlpatterns = [
    path('accounts/signup',signup, name='signup'),
     path('accounts/login',login_view,name='login'),
    path('accounts/logout/',logout_view,name='logout')
]