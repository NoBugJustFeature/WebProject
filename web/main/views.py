from django.shortcuts import render
from .models import Movies


def index(request):
    movies = Movies.objects.all()
    return render(request, "main/index.html", {"movies": movies})

def account(request):
    return render(request, "main/account.html")

def about(request):
    return render(request, "main/about.html")

def about_film(request):
    movie = request.GET.get("movie")
    return render(request, "main/about-film.html", {"movie": movie})