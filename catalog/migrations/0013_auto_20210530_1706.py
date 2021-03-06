# Generated by Django 3.2.3 on 2021-05-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_catalog_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='id',
        ),
        migrations.AlterField(
            model_name='catalog',
            name='ProductId',
            field=models.CharField(default=0, max_length=250, primary_key=True, serialize=False, verbose_name='ID товара'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='ProductImage',
            field=models.ImageField(blank=True, default='product_images/no-image.jpg', null=True, upload_to='product_images', verbose_name='Изображение'),
        ),
    ]
