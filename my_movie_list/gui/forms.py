from django import forms
from .models import MovieList, Movie


class MovieListForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ['name']


class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    year = forms.IntegerField()
    rating = forms.FloatField()

    class Meta:
        model = Movie
        fields = ['title', 'year', 'rating']
