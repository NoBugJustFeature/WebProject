from django.contrib import admin
from .models import Movie
from .models import Comment

admin.site.register([Movie,
                     Comment,])
