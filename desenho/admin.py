from django.contrib import admin
from .models import Animacao
from .models import Personagem

# Register your models here.
admin.site.register(Animacao)
admin.site.register(Personagem)