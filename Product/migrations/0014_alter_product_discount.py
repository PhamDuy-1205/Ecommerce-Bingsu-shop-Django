# Generated by Django 4.1.3 on 2022-12-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0013_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Discount',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10),
        ),
    ]
