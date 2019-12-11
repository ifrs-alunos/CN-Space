from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 



class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	apelido = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "apelido", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		user.apelido = self.cleaned_data["last_name"]

		if commit:
			user.save()
		return user 

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username' )