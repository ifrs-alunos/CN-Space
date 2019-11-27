from django.contrib import admin
from .models.person import Person
from .models.passport import Passport
from .models.reporter import Reporter
from .models.article import Article
from .models.magazine import Magazine
# Register your models here.

admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Magazine)