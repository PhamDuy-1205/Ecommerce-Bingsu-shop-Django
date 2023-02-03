# Generated by Django 4.1.3 on 2022-12-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0016_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Discount',
            field=models.DecimalField(decimal_places=2, default=0.1, max_digits=3),
        ),
    ]