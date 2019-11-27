from post.models.base import *
from django.contrib.auth.models import User
from conta.models.usuario import Usuario
from .postagem import Postagem

class Comentario(BaseModel):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
	texto = models.CharField(max_length=900)

	class Meta:
		pass

	def get_texto(self):
		return self.texto

	