
from django.db import models

class Tag(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Director(models.Model):
    class Meta:
        verbose_name = 'Директория'
        verbose_name_plural = 'Директории'
    director = models.CharField(max_length=155, verbose_name='имя')

    def __str__(self):
        return self.director

class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    img = models.ImageField(upload_to='Movie', null=True)
    title = models.CharField(max_length=255, verbose_name='названия')
    descriptions = models.TextField(verbose_name='Описания')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэги')

    def __str__(self):
        return self.title

class Movie_commits(models.Model):
    class Meta:
        verbose_name = 'Коментарий'
