from django.urls import path
from . views import *

urlpatterns = [
    path('',index, name='index'),
    path('references',reference_view,name='reference_view'),
    path('chat',chat_view,name='chat_view')

]