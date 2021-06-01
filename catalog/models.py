from datetime import datetime
from PIL import Image
from django.db import models


# Create your models here.


class Catalog(models.Model):
    COMPUTERS = 'CP'
    MACHINES = 'MI'
    INSTRUMENTS = 'IM'
    COMPONENTS = 'CN'

    CATEGORY = [
        (COMPUTERS, 'Компьютеры'),
        (MACHINES, 'Бытовая техника'),
        (INSTRUMENTS, 'Инструменты'),
        (COMPONENTS, 'Комплектующие')
    ]

    MACHINES_LIGHT = 'MI_L'
    MACHINES_INC = 'MI_I'
    COMPUTERS_FULL = 'CP_F'
    LAPTOP = 'LT'
    INSTRUMENTS_PORTABLE = 'IM_PORT'
    INSTRUMENTS_PERF = 'IM_PERF'
    INSTRUMENTS_HARD = 'IM_HARD'
    COMPONENTS_CPU = 'CN_CPU'
    COMPONENTS_RAM = 'CN_RAM'
    COMPONENTS_GPU = 'CN_GPU'
    COMPONENTS_MB = 'CN_MB'
    COMPONENTS_FAN = 'CN_FAN'
    COMPONENTS_ROM = 'CN_ROM'

    CATEGORY_DEEP = [
        (MACHINES_LIGHT, 'Легкая техника'),
        (MACHINES_INC, 'Встраиваемая техника'),
        (COMPUTERS_FULL, 'Готовые ПК'),
        (LAPTOP, 'Ноутбуки'),
        (INSTRUMENTS_PORTABLE, 'Портативные инструменты'),
        (INSTRUMENTS_HARD, 'Тяжелые инструменты'),
        (INSTRUMENTS_PERF, 'Переферия'),
        (COMPONENTS_CPU, 'ЦП'),
        (COMPONENTS_RAM, 'ОЗУ'),
        (COMPONENTS_GPU, 'Видеокарты'),
        (COMPONENTS_MB, 'Материнские платы'),
        (COMPONENTS_FAN, 'Охлаждение'),
        (COMPONENTS_ROM, 'Носители информации')
    ]

    ProductId = models.AutoField('ID товара', primary_key=True)
    ProductName = models.CharField('Название продукта', max_length=250)
    ProductMaker = models.CharField('Производитель', max_length=250)
    ProductBrand = models.CharField('Брэнд', max_length=250)
    ProductPrice = models.CharField('Цена', max_length=250)
    ProductCategory = models.CharField('Категория', choices=CATEGORY, max_length=250)
    ProductFeatures = models.TextField('Под категория', choices=CATEGORY_DEEP, max_length=250)
    ProductDescription = models.TextField('Описание продукта')
    ProductImage = models.ImageField('Изображение', null=True, blank=True, upload_to='product_images',
                                     default='product_images/no-image.jpg')
    ProductMetaTittle = models.CharField('MetaTittle', max_length=250)
    ProductMetaKeywords = models.TextField('MetaKeywords')
    ProductMetaDescription = models.TextField('MetaDescription')
    AddTime = models.DateTimeField('Дата', default=datetime.now, blank=True)
    ProductIsrail = models.BooleanField('Товар в наличии', default=True)

    def __str__(self):
        return self.ProductName


class Cart(models.Model):
    ProductIdSOld = models.JSONField('ID товара: Кол-во')
    ProductNameSold = models.CharField('Название продукта', max_length=250, default=0)
    SoldTime = models.DateTimeField('Время продажи')
    # ProductCount = models.CharField('Кол-во проданных товаров', max_length=250)

    def __str__(self):
        return self.ProductNameSold


class Checkout(models.Model):
    CustomerName = models.CharField('Имя', max_length=250)
    CustomerEmail = models.EmailField('Почта', default='')
    CustomerPhone = models.CharField('Телефон', max_length=12)
    CustomerPlace = models.TextField('Адрес', default='')
    CustomerCity = models.CharField('Город', max_length=250)
    CustomerZip = models.CharField('Индекс', max_length=6)
    # Payment Info
    CustomerCardName = models.CharField('Имя на карте', max_length=250)
    CustomerCardNumber = models.CharField('Номер карты', max_length=250)
    CustomerCardExp = models.CharField('Дата окончания', max_length=5)
    CustomerCardCVV = models.CharField('CVV-код', max_length=3)
    # Order summary
    OrderSummary = models.CharField('ID продажи', max_length=250)

    def __str__(self):
        return self.OrderSummary
