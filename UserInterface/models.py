from django.db import models


class User(models.Model):
    username = models.CharField('Логин', max_length=50)
    email = models.EmailField('Email')
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'