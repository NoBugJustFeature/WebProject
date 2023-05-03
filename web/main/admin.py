from django.contrib import admin
from .models import Movies
from .models import Comments

admin.site.register([Movies,
                     Comments,])
