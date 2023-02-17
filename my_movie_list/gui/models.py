from django.db import models
from django.contrib.auth.models import User


class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=0)
    rating = models.FloatField()
    movie_list = models.ForeignKey(
        MovieList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
