from django.db import models

# Create your models here.


class AuthDb(models.Model):
    Login = models.CharField('Логин', max_length=50)
    Password = models.CharField('Пароль', max_length=50)
    EmailField = models.EmailField('Почта')
    Post = models.CharField('Должность', max_length=50)
    FirstName = models.CharField('Имя', max_length=120)
    SecondName = models.CharField('Фамилия', max_length=120)
    IsAdmin = models.BooleanField('Администратор')

    def __str__(self):
        return self.Login
