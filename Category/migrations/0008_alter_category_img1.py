# Generated by Django 4.1.3 on 2022-12-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0007_alter_category_parentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Img1',
            field=models.ImageField(default='', upload_to='uploads/Category/'),
        ),
    ]
