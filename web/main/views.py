from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Movies, Comments
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm


def index(request):
    movies = Movies.objects.all()
    return render(request, "main/index.html", {"movies": movies})

def log_in(request):
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                messages.success(request, "Вы вошли в аккаунт")
                return redirect(account)
            
        message = "Неправильный логин или пароль"
            
    form = LoginForm()
    return render(request, 'main/login.html', {'form': form, "message": message})

def account(request):
    if request.method == 'POST':
        logout(request)
        return redirect(account)

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        comments = Comments.objects.filter(username=request.user.username)
        return render(request, "main/account.html", {"user":user, "comments": comments})
    else: 
        return redirect(log_in)
    
def registration(request):
    if request.user.is_authenticated:
        return redirect(account)

    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_active = False
            new_user.save()
            return render(request, 'main/registration_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
        return render(request, 'main/registration.html', {'user_form': user_form})

def about(request):
    return render(request, "main/about.html")

def about_film(request):
    movie = Movies.objects.get(href=request.GET.get("movie"))
    comments = Comments.objects.filter(film_title=movie.title)
    return render(request, "main/about-film.html", {"movie": movie,
                                                    "comments": comments})