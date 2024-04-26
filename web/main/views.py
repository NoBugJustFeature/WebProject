from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Movie, Comment
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, CommentForm

from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    movies = Movie.objects.all()
    return render(request, "main/index.html", {"movies": movies})


def registration(request):
    if request.user.is_authenticated:
        return redirect(account)
    
    message = None
    user_form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(account)
        message = form.errors

        
    return render(request, 'main/registration.html', {'user_form': user_form, 'message': message})


def log_in(request):
    message = None
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                messages.success(request, "Вы вошли в аккаунт")
                return redirect(account)
            
        message = "Неправильный логин или пароль"
    return render(request, 'main/login.html', {'form': login_form, "message": message})


def account(request):
    if request.method == 'POST':
        logout(request)
        return redirect(account)

    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        comments = Comment.objects.filter(user=user)
        return render(request, "main/account.html", {"user":user, "comments": comments})
    else: 
        return redirect(log_in)


def about(request):
    return render(request, "main/about.html")


def about_film(request):
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comm = comment.save(commit=False)
            print(request.user)
            user = request.user
            comm.user = user if user else "Guest"
            comm.movie = Movie.objects.get(address_href=request.GET.get("movie"))
            comm.save()
            return HttpResponseRedirect(f'about-film?movie={request.GET.get("movie")}')
    
    movie = Movie.objects.get(address_href=request.GET.get("movie"))
    comments = Comment.objects.filter(movie=movie)
    leave_comment = CommentForm()
    return render(request, "main/about-film.html", {"movie": movie,
                                                    "comments": comments,
                                                    "leave_comment": leave_comment})