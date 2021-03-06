# Generated by Django 3.2.3 on 2021-06-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20210601_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerCardCVV',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerCardExp',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerCardName',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerCardNumber',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerCity',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerEmail',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerName',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerPhone',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerPlace',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='CustomerZip',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='OrderSummary',
        ),
        migrations.AddField(
            model_name='checkout',
            name='ProductCountCheckout',
            field=models.CharField(default=0, max_length=250, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='ProductIdCheckout',
            field=models.CharField(default=0, max_length=250, verbose_name='ID товара'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='SoldTime',
            field=models.DateTimeField(null=True, verbose_name='Время продажи'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='UserNameCheckout',
            field=models.CharField(default='', max_length=250, verbose_name='Имя пользователя'),
        ),
    ]
