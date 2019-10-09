from django.db import models
from django.contrib.auth.models import User
from .animation import Animacao

class Personagem(models.Model):
	nome = models.CharField(max_length=200)
	caracterisiticas = models.CharField(max_length=800)
	animacao = models.ForeignKey(Animacao, on_delete=models.CASCADE)


	class Meta:
		pass

	# def __init__(self, nome, animacao, caracteristicas):
	# 	self.nome = nome
	# 	self.animacao = animacao
	# 	self.caracterisiticas = caracteristicas

	def get_nome(self):
		return self.nome

	def get_animacao(self):
		return self.animacao

	def get_caracteristicas(self):
		return self.caracteristicas