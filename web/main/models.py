from django.db import models
from django.contrib.auth.models import User
from web.settings import MEDIA_ROOT


class Movie(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to=MEDIA_ROOT)
    address_href = models.CharField("Ссылка", max_length=50, help_text = "Ссылка, которая отображается в адресной строке")
    trailer_href = models.CharField("Ссылка на трейлер", max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comment = models.TextField("Комментарий")

    def __str__(self):
        return self.comment