from conta.models.base import *
from django.contrib.auth.models import User 

class Cadastro(BaseModel):
	username = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	#email=
	#password = 

	class Meta:
		pass

	def __init__(self,username, nickname):
		self.username = username
		self.nickname = nickname