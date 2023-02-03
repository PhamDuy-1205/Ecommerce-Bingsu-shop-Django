from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=200)
    Code = models.CharField(max_length=200)
    ParentId = models.BigIntegerField(default=0)
    Img1 = models.ImageField(default = "", upload_to="uploads/Category/")
    

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'Category'
