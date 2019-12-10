from accounts.models.base import *
from django.contrib.auth.models import User 

class Cadastro(BaseModel):
	username = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	email= models.EmailField()
	password = models.CharField(max_length=100)
	class Meta:
		pass

	#def __init__(self,username, nickname, email, password):
		#self.username = username
		#self.nickname = nickname
		#self.email = email
		#self.password = password
