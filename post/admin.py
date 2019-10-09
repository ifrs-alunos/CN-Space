from django.contrib import admin
from .models import Comentario
from .models import Postagem
from .models import Tag

# Register your models here.
admin.site.register(Comentario)
admin.site.register(Postagem)
admin.site.register(Tag)
