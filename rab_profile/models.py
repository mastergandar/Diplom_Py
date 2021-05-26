from django.db import models

# Create your models here.


class Dashboard(models.Model):

    SalePrice = models.TextField('Цена')
    DataTime = models.DateField('Дата')
    SaleRev = models.CharField('Покупка', max_length=250)

    def __str__(self):
        return self.SalePrice
