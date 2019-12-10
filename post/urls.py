from django.urls import path 

from django.contrib import admin 
from django.urls import path, include
from . import views 

app_name = 'post'

urlpatterns = [
	# ex: /course/]
	path('', views.index, name='index'),
	path('board/topics/<int:board_id>/', views.topics, name='board_topics'),
	path('board/create/<int:board_id>/', views.create, name='board_create'),
	path('topic/posts/<int:topic_id>', views.posts, name='topic_posts'),
	path('topic/reply/<int:topic_id>', views.reply, name='topic_reply'),


	#path('article/create', views.create, name='article_create'),

	#path('article/edit/<int:article_id>', views.edit, name='article_edit'),
	#path('article/delete/<int:article_id>', views.delete, name='article_delete'),
	#path('article/publish/<int:article_id>', views.publish, name='article_publish'),
	
	]