from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='No description available')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    year = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='No description available')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    year_release = models.PositiveSmallIntegerField(
        default=0, null=True, blank=True)
    year_completion = models.PositiveSmallIntegerField(null=True, blank=True)
    STATUS_CHOICES = [
        ('O', 'On going'),
        ('C', 'Completed'),
    ]
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='Completed')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    movies_watched = models.ManyToManyField(Movie, related_name='watched_by')
    movies_plan_to_watch = models.ManyToManyField(
        Movie, related_name='plan_to_watch_by')
    series_watched = models.ManyToManyField(Series, related_name='watched_by')
    series_plan_to_watch = models.ManyToManyField(
        Series, related_name='plan_to_watch_by')

    def __str__(self):
        return self.user.username
