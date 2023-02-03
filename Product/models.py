from django.db import models
from Category.models import Category

# Create your models here.

class Product(models.Model):
    ProductName = models.CharField(max_length = 500)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    Description = models.TextField()
    Img1 = models.ImageField(default = "", upload_to="uploads/Product/")
    Img2 = models.ImageField(default = "", upload_to="uploads/Product/")
    Img3 = models.ImageField(default = "", upload_to="uploads/Product/")
    Img4 = models.ImageField(default = "", upload_to="uploads/Product/")
    CategoryId = models.ForeignKey(Category, on_delete = models.CASCADE)
    Discount = models.DecimalField(max_digits = 3, decimal_places = 2, default=0)

    def __str__(seft):
        return seft.ProductName

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter (category=category_id)
        else:
            return Product.get_all_products();

    class Meta:
        db_table = 'Product'


