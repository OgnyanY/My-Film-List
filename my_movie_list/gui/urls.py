from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login2'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:pk>/add-to-watched/',
         views.add_movie_to_watched, name='add_movie_to_watched'),
    path('movies/<int:pk>/add-to-plan-to-watch/',
         views.add_movie_to_plan_to_watch, name='add_movie_to_plan_to_watch'),
    path('movies/<int:pk>/remove-from-watched/',
         views.remove_movie_from_watched, name='remove_movie_from_watched'),
    path('movies/<int:pk>/remove-from-plan-to-watch/',
         views.remove_movie_from_plan_to_watch, name='remove_movie_from_plan_to_watch'),


    path('series/<int:pk>/', views.series_detail, name='series_detail'),
    path('series/<int:pk>/add-to-watched/',
         views.add_series_to_watched, name='add_series_to_watched'),
    path('series/<int:pk>/add-to-plan-to-watch/',
         views.add_series_to_plan_to_watch, name='add_series_to_plan_to_watch'),
    path('series/<int:pk>/remove-from-watched/',
         views.remove_series_from_watched, name='remove_series_from_watched'),
    path('series/<int:pk>/remove-from-plan-to-watch/',
         views.remove_series_from_plan_to_watch, name='remove_series_from_plan_to_watch'),


    path('search/', views.search, name='search'),
]
