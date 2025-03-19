from django.contrib import admin
from django.contrib.admin import ModelAdmin

from Product.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass