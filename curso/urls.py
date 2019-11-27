from django.urls import path 

from django.contrib import admin 
from django.urls import path, include
from . import views 

app_name = 'curso'

urlpatterns = [
	# ex: /course/]
	path('', views.index, name='index'),
	path('article/create', views.create, name='article_create'),
	#path('article/list', views.list_articles, name='article_list'),
	path('article/edit/<int:article id>', views.edit, name='article_edit'),
	path('article/delete/<int:article_id>', views.delete, name='article_delete'),
	
	]