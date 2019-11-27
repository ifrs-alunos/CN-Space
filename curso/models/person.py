from django.db import models

class Person(models.Model):
	"""docstring for Person"""
	name = models.CharField(max_length=100, verbose_name='Full Name')
	birth_date = models.DateField(verbose_name='Birth Date')
	cpf = models.CharField(max_length=11, verbose_name='CPF Number')

		