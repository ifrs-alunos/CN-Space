from django.urls import path 
from django.contrib import admin 
from . import views 

app_name = 'desenho'

urlpatterns = [

	path('animacao',views.animacao,name='animacao'),
	path('animacao/steven', views.steven, name='animacao_steven'),
	path('animacao/aventura', views.aventura, name='animacao_aventura'),
	path('animacao/gumball', views.gumball, name='animacao_gumball'),
]
