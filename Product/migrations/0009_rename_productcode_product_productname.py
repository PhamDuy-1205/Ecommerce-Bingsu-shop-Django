# Generated by Django 4.1.3 on 2022-12-12 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0008_alter_product_img1_alter_product_img2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ProductCode',
            new_name='ProductName',
        ),
    ]
