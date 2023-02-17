from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    
]
