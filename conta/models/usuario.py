from conta.models.base import *
from django.contrib.auth.models import User 

class Usuario(BaseModel):
	username = models.CharField(max_length=100)
	nickname = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=8)

	class Meta:
		pass

	def __str__(self):
		return '{}\n{}\n{}\n{}'.format(self.username, self.nickname, self.email, self.password)