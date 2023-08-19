from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(ReferenceStation)
class AdminReferenceStation(admin.ModelAdmin):
    list_display = ['station_name','station_location']

@admin.register(Chat)
class AdminChat(admin.ModelAdmin):
    list_display = ['message','date']
