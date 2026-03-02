from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Сюжет")
    rating = models.IntegerField(verbose_name="Рейтинг фильма", choices=[(i, i) for i in range(1,11)])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец фильма")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
