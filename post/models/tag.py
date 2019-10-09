from post.models.base import *
from django.contrib.auth.models import User
from .postagem import Postagem


class Tag(BaseModel):
	name = models.CharField(max_length=50)
	postagemm = models.ManyToManyField(Postagem)

	def __str__(self):
		return '{}\n'.format(self.name)

	def get_name(self):
		return self.name