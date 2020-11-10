from django.contrib import admin
from .models import Products
# Register your models here.


@admin.register(Products)
class adminproducts(admin.ModelAdmin):
    list_display = ['id','title','desc','price','pics','tym','utym','offer']