# Generated by Django 3.2.3 on 2021-05-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210524_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=250, verbose_name='Имя')),
                ('CustomerEmail', models.EmailField(default='', max_length=254, verbose_name='Почта')),
                ('CustomerPhone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('CustomerPlace', models.TextField(default='', verbose_name='Адрес')),
                ('CustomerCity', models.CharField(max_length=250, verbose_name='Город')),
                ('CustomerZip', models.CharField(max_length=6, verbose_name='Индекс')),
                ('CustomerCardName', models.CharField(max_length=250, verbose_name='Имя на карте')),
                ('CustomerCardNumber', models.CharField(max_length=250, verbose_name='Номер карты')),
                ('CustomerCardExp', models.CharField(max_length=5, verbose_name='Дата окончания')),
                ('CustomerCardCVV', models.CharField(max_length=3, verbose_name='CVV-код')),
                ('OrderSummary', models.CharField(max_length=250, verbose_name='ID продажи')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ProductCount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='SoldID',
        ),
        migrations.AlterField(
            model_name='cart',
            name='ProductIdSOld',
            field=models.JSONField(verbose_name='ID товара: Кол-во'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='ProductImage',
            field=models.ImageField(upload_to='product_images/', verbose_name='Изображение'),
        ),
    ]