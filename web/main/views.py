from django.shortcuts import render
from .models import Movies
from .models import Comments



def index(request):
    movies = Movies.objects.all()
    return render(request, "main/index.html", {"movies": movies})

def account(request):
    if request.user.is_authenticated:
        return render(request, "main/account.html")
    else:
        return render(request, "main/login.html")

def about(request):
    return render(request, "main/about.html")

def about_film(request):
    movie = Movies.objects.get(href=request.GET.get("movie"))
    comments = Comments.objects.filter(film_title=movie.href)
    return render(request, "main/about-film.html", {"movie": movie,
                                                    "comments": comments})