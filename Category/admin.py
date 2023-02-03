from django.contrib import admin
from Category.models import Category
from Product.models import Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)