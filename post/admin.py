from django.contrib import admin

from .models import Post
from .models import Board
from .models import Topic

# Register your models here.

admin.site.register(Post)
admin.site.register(Board)
admin.site.register(Topic)
