# Generated by Django 4.1.3 on 2022-11-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Code', models.CharField(max_length=20)),
                ('ParentId', models.BigIntegerField()),
            ],
        ),
    ]