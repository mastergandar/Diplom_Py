# Generated by Django 3.2.3 on 2021-05-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20210530_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='ProductId',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, verbose_name='ID товара'),
        ),
    ]