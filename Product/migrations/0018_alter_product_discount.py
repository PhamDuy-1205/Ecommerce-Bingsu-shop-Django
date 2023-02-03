# Generated by Django 4.1.3 on 2023-01-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0017_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]