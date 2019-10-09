from django.db import models
from django.contrib.auth.models import User



class Animacao(models.Model):
	nomee = models.CharField(max_length=200)
	sinopse = models.CharField(max_length=500)
	status = models.BooleanField(default=True)

	class Meta:
		pass


	# def __init__(self, nomee, sinopse, lista_de_personagens):

	# 	self.nomee = nomee
	# 	self.sinopse = sinopse
	# 	self.lista_de_personagens = lista_de_personagens

	def __str__(self):
		return '{}: {}'.format(self.nomee, self.sinopse)

	def get_nome(self):
		return self.nomee

	def get_sinopse(self):
		return self.sinopse

	def get_status(self):
		if self.status == True:
			return 'Ativo'
		else:
			return 'Inativo'
			

	def set_status(self):
		if self.status == True:
			self.status = False
		else:
			self.status = True





