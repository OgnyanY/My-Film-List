from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    path('<int:pk>/', views.movie_list_detail, name='movie_list_detail'),
    path('create/', views.create_movie_list, name='create_movie_list'),
    path('<int:pk>/create/', views.create_movie, name='create_movie'),
    path('lists/', views.movie_list, name='movie_list'),
    path('<int:pk>/delete/', views.delete_movie_list, name='delete_movie_list'),
    path('<int:pk>/delete/<int:movie_pk>/',
         views.delete_movie, name='delete_movie'),
    path('<int:pk>/edit/<int:movie_pk>/', views.edit_movie, name='edit_movie'),

]
