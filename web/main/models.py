from django.db import models
from web.settings import MEDIA_ROOT


class Movies(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to=MEDIA_ROOT)
    href = models.CharField("Ссылка", max_length=50)
    trailer_href = models.CharField("Ссылка на трейлер", max_length=100)

    def __str__(self):
        return self.title

class Comments(models.Model):
    film_title = models.CharField("Название фильма", max_length=50)
    comment = models.TextField("Комментарий")
    username = models.CharField("Логин пользователя", max_length=50)
    film_href = models.CharField("Ссылка", max_length=50)

    def __str__(self):
        return self.film_title