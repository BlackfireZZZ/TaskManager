from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')
    deadline = models.DateField('Дедлайн', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

