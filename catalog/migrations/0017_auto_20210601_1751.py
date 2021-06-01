# Generated by Django 3.2.3 on 2021-06-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_catalog_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='ProductIdSOld',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ProductNameSold',
        ),
        migrations.AddField(
            model_name='cart',
            name='ProductCountSold',
            field=models.CharField(default=0, max_length=250, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='cart',
            name='ProductIdSold',
            field=models.CharField(default=0, max_length=250, verbose_name='ID товара'),
        ),
        migrations.AddField(
            model_name='cart',
            name='UserNameSold',
            field=models.CharField(default='', max_length=250, verbose_name='Имя пользователя'),
        ),
    ]
