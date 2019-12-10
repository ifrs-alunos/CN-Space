
from django.contrib import admin 
from django.urls import path, include
from . import views 


app_name = 'accounts'

urlpatterns = [
	# ex: /course/]
	#path('register/', views.SignUp.as_view(), name='signup'),
	#path('register/', views.create, name='create'),
   	#path('cadastro/create', views.create, name='cadastro_create'),
   	path('register/', views.register, name='register'),
   	path('logout/', views.logout_request, name='logout'),
   	path('login/', views.login_request, name="login"),


] 

