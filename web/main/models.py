from django.db import models
from web.settings import MEDIA_ROOT


class Movies(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to=MEDIA_ROOT)
    href = models.CharField("Ссылка", max_length=50)

    def __str__(self):
        return self.title
