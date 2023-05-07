from django.urls import path
from . import views

from web.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="home"),
    path("account",  views.account, name="account"),
    path("about", views.about, name="about"),
    path("about-film", views.about_film, name="about-film"),
    path("registration", views.registration, name="registration"),
    path("login", views.log_in, name="logn"),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
