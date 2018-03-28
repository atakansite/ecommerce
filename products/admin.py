from django.contrib import admin

from django.contrib import admin

from products.models import Products
from products.models import MainCategory
from products.models import SubCategory

class ProductsAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}

class MainCategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}

class SubCategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)