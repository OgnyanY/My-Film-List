from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Movie, Series, UserProfile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.movies_url = reverse('movie_detail', args=[1])
        self.series_url = reverse('series_detail', args=[1])
        self.user = User.objects.create_user(
            username='testuser', password='1234test')
        self.movie = Movie.objects.create(title='Test Movie', rating=7.5)
        self.series = Series.objects.create(title='Test Series', rating=8.0)
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_home_view(self):
        self.client.login(username='testuser', password='1234test')
        response = self.client.get(self.home_url)

        self.assertTemplateUsed(response, 'home.html')

    def test_movie_detail_view(self):
        self.client.login(username='testuser', password='1234test')
        response = self.client.get(self.movies_url)

        self.assertTemplateUsed(response, 'movie_detail.html')

    def test_series_detail_view(self):
        self.client.login(username='testuser', password='1234test')
        response = self.client.get(self.series_url)

        self.assertTemplateUsed(response, 'series_detail.html')

    def test_add_movie_to_watched_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.movies_watched.add(self.movie)

        self.assertIn(self.movie, self.user_profile.movies_watched.all())

    def test_add_movie_to_plan_to_watch_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.movies_plan_to_watch.add(self.movie)

        self.assertIn(self.movie, self.user_profile.movies_plan_to_watch.all())

    def test_add_series_to_watched_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.series_watched.add(self.series)

        self.assertIn(self.series, self.user_profile.series_watched.all())

    def test_add_series_to_plan_to_watch_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.series_plan_to_watch.add(self.series)

        self.assertIn(
            self.series, self.user_profile.series_plan_to_watch.all())

    def test_remove_movie_from_watched_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.movies_watched.add(self.movie)
        self.user_profile.movies_watched.remove(self.movie)

        self.assertNotIn(self.movie, self.user_profile.movies_watched.all())

    def test_remove_movie_from_plan_to_watch_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.movies_plan_to_watch.add(self.movie)
        self.user_profile.movies_plan_to_watch.remove(self.movie)

        self.assertNotIn(
            self.movie, self.user_profile.movies_plan_to_watch.all())

    def test_remove_series_from_watched_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.series_watched.add(self.series)
        self.user_profile.series_watched.remove(self.series)

        self.assertNotIn(self.series, self.user_profile.series_watched.all())

    def test_remove_series_from_plan_to_watch_view(self):
        self.client.login(username='testuser', password='1234test')
        self.user_profile.series_plan_to_watch.add(self.series)
        self.user_profile.series_plan_to_watch.remove(self.series)
        self.assertNotIn(
            self.series, self.user_profile.series_plan_to_watch.all())
