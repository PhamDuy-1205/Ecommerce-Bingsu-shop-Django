# Generated by Django 4.1.3 on 2022-11-14 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_alter_product_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Img1',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='Img2',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='Img3',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='Img4',
            field=models.ImageField(upload_to=''),
        ),
    ]
