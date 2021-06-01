# Generated by Django 3.2.3 on 2021-05-29 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210526_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='AddTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='ProductImage',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Изображение'),
        ),
    ]
