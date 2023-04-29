from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "main/index.html")

def account(request):
    return render(request, "main/account.html")

def about(request):
    return render(request, "main/about.html")
