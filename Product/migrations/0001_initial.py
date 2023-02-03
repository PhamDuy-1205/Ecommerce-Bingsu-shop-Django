# Generated by Django 4.1.3 on 2022-11-14 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductCode', models.CharField(max_length=20)),
                ('Price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Title', models.CharField(max_length=300)),
                ('Size', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Img1', models.TextField()),
                ('Img2', models.TextField()),
                ('Img3', models.TextField()),
                ('Img4', models.TextField()),
                ('CategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Category.category')),
            ],
        ),
    ]
