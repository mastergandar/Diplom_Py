# Generated by Django 3.2.3 on 2021-05-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ProductIdSOld',
            field=models.CharField(default=0, max_length=250, verbose_name='ID товара'),
        ),
    ]