# Generated by Django 4.1.3 on 2022-12-18 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_product_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount',
            new_name='Discount',
        ),
    ]
