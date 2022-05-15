from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.CharField('Описание', max_length=50)


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
