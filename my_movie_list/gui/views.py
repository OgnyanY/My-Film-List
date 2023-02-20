from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Movie, Series, UserProfile
from django.contrib import messages
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user)
            profile.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    user_profile = None
    if hasattr(request.user, 'userprofile'):
        user_profile = request.user.userprofile
    watched_movies = user_profile.movies_watched.all() if user_profile else []
    plan_to_watch_movies = user_profile.movies_plan_to_watch.all() if user_profile else []
    watched_series = user_profile.series_watched.all() if user_profile else []
    plan_to_watch_series = user_profile.series_plan_to_watch.all() if user_profile else []
    return render(request, 'home.html',
                  {'watched_movies': watched_movies, 'plan_to_watch_movies': plan_to_watch_movies,
                   'watched_series': watched_series, 'plan_to_watch_series': plan_to_watch_series})


@login_required
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})


@login_required
def series_detail(request, pk):
    series = get_object_or_404(Series, pk=pk)
    return render(request, 'series_detail.html', {'series': series})


@login_required
def add_movie_to_watched(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user_profile = request.user.userprofile
    user_profile.movies_plan_to_watch.remove(movie)
    user_profile.movies_watched.add(movie)
    messages.success(
        request, f"{movie.title} has been added to your watched list.")
    return redirect('home')


@login_required
def add_movie_to_plan_to_watch(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user_profile = request.user.userprofile
    user_profile.movies_watched.remove(movie)
    user_profile.movies_plan_to_watch.add(movie)
    messages.success(
        request, f"{movie.title} has been added to your plan to watch list.")
    return redirect('home')


@login_required
def add_series_to_watched(request, pk):
    series = get_object_or_404(Series, pk=pk)
    user_profile = request.user.userprofile
    user_profile.series_plan_to_watch.remove(series)
    user_profile.series_watched.add(series)
    messages.success(
        request, f"{series.title} has been added to your watched list.")
    return redirect('home')


@login_required
def add_series_to_plan_to_watch(request, pk):
    series = get_object_or_404(Series, pk=pk)
    user_profile = request.user.userprofile
    user_profile.series_watched.remove(series)
    user_profile.series_plan_to_watch.add(series)
    messages.success(
        request, f"{series.title} has been added to your plan to watch list.")
    return redirect('home')


@login_required
def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET.get('q', '')
        movies = Movie.objects.filter(Q(title__icontains=query))
        series = Series.objects.filter(Q(title__icontains=query))
        return render(request, 'search_results.html', {'movies': movies, 'series': series, 'query': query})
    else:
        return redirect('home')


@login_required
def remove_movie_from_watched(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user_profile = request.user.userprofile
    user_profile.movies_watched.remove(movie)
    messages.success(
        request, f"{movie.title} has been removed from your watched list.")
    return redirect('home')


@login_required
def remove_movie_from_plan_to_watch(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user_profile = request.user.userprofile
    user_profile.movies_plan_to_watch.remove(movie)
    messages.success(
        request, f"{movie.title} has been removed from your plan to watch list.")
    return redirect('home')


@login_required
def remove_series_from_watched(request, pk):
    series = get_object_or_404(Series, pk=pk)
    user_profile = request.user.userprofile
    user_profile.series_watched.remove(series)
    messages.success(
        request, f"{series.title} has been removed from your watched list.")
    return redirect('home')


@login_required
def remove_series_from_plan_to_watch(request, pk):
    series = get_object_or_404(Series, pk=pk)
    user_profile = request.user.userprofile
    user_profile.series_plan_to_watch.remove(series)
    messages.success(
        request, f"{series.title} has been removed from your plan to watch list.")
    return redirect('home')
