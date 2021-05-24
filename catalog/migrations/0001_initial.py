# Generated by Django 3.2.3 on 2021-05-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoldID', models.CharField(max_length=250, verbose_name='ID продажи')),
                ('SoldTime', models.DateTimeField(verbose_name='Время продажи')),
                ('ProductCount', models.CharField(max_length=250, verbose_name='Кол-во проданных товаров')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=250, verbose_name='Название продукта')),
                ('ProductMaker', models.CharField(max_length=250, verbose_name='Производитель')),
                ('ProductBrand', models.CharField(max_length=250, verbose_name='Брэнд')),
                ('ProductPrice', models.CharField(max_length=250, verbose_name='Цена')),
                ('ProductCategory', models.CharField(choices=[('CP', 'Компьютеры'), ('MI', 'Бытовая техника'), ('IM', 'Инструменты'), ('CN', 'Комплектующие')], max_length=250, verbose_name='Категория')),
                ('ProductFeatures', models.TextField(choices=[('MI_L', 'Легкая техника'), ('MI_I', 'Встраиваемая техника'), ('CP_F', 'Готовые ПК'), ('LT', 'Ноутбуки'), ('IM_PORT', 'Портативные инструменты'), ('IM_HARD', 'Тяжелые инструменты'), ('IM_PERF', 'Переферия'), ('CN_CPU', 'ЦП'), ('CN_RAM', 'ОЗУ'), ('CN_GPU', 'Видеокарты'), ('CN_MB', 'Материнские платы'), ('CN_FAN', 'Охлаждение'), ('CN_ROM', 'Носители информации')], max_length=250, verbose_name='Под категория')),
                ('ProductDescription', models.TextField(verbose_name='Описание продукта')),
                ('ProductImage', models.CharField(max_length=250, verbose_name='Изображение')),
                ('ProductMetaTittle', models.CharField(max_length=250, verbose_name='Категория')),
                ('ProductMetaKeywords', models.TextField(verbose_name='Категория')),
                ('ProductMetaDescription', models.TextField(verbose_name='Категория')),
                ('AddTime', models.DateField(verbose_name='Дата')),
            ],
        ),
    ]