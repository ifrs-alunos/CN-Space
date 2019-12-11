from django.shortcuts import render, get_object_or_404, redirect 
#from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
#from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required, permission_required
#from django import forms
from django.contrib.auth.models import User
#from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm, UserEditForm
from django.template import RequestContext
from django.contrib.auth.forms import UserChangeForm




#class SignUp(generic.CreateView):
	#form_class = NewUserForm
	#sucess_url = reverse_lazy('login')
	#template_name = 'registration/register.html'


def register(request):
	message = ""
	if request.method == 'POST':
		form_class = NewUserForm(request.POST)
		if form_class.is_valid():
			form_class.save()
			message = 'HAS BEEN SUCCESFULLY SAVED'
			return redirect('login')

	else:
		form_class = NewUserForm(request.POST)

	context = {'form_class': form_class,
				'message': message, }

	return render(request, 'accounts/register.html', context)

def login_request(request):

	if request.method == 'POST':

		form_class = AuthenticationForm(request, data=request.POST)

		if form_class.is_valid():
			username = form_class.cleaned_data.get('username')
			password = form_class.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')

			else:
				messages.info(request, 'Three credits remain in your account.')
				#return(render,'accounts/login.html',{'form_class':form_class})
		else:
			messages.info(request, 'Three credits remain in your account.')
	form_class = AuthenticationForm()
	return render (request, 'accounts/login.html',{'form_class':form_class})


def logout_request(request):
	logout(request)
	messages.info(request, "Deslogado com sucesso")
	return redirect("login")

#def profile(request):
	#args = {'user': request.user}
	#return render(request, "accounts/profile.html", args)


def profile(request):
	if request.method == "POST":
		form_class = UserEditForm(request.POST, instance=request.user)
		if form_class.is_valid():  
			form_class.save()
			return redirect ('/accounts/profile')

	else:
		form_class = UserEditForm(instance=request.user)
		args = {'form_class': form_class}
		#return render(request, 'accounts/profile.html')

	context = {'form_class': form_class}
	return render(request, 'accounts/profile.html', context)