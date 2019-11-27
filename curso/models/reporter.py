from django.db import models

class Reporter(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	cpf = models.CharField(max_length=11)

	def __str__(self):
		return "%s : %s" % (self.name, self.email)