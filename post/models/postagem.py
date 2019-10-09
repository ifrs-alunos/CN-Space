from post.models.base import *
from django.contrib.auth.models import User
from conta.models.usuario import Usuario

class Postagem(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	data = models.DateField()
	legenda = models.CharField(max_length=200)
	numero_curtidas = models.CharField(max_length=900)
	numero_comentarios = models.CharField(max_length=900)
	#comentarios = []
	#tags = []

	class Meta:
		pass

	def get_legenda(self):
		return self.legenda

	def get_numero_comentarios(self):
		return self.numero_comentarios

	# def get_comentarios(self):
	# 	return self.comentarios

	# def get_tags(self):
	# 	return self.tags
		