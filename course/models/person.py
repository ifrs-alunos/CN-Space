from django.db import models 

class Person(models.Model):
	name = models.CharField(max_length=100, verbose_name='Full Name')
	bith_date =  models.DateField(verbose_name='Birth Name')
	cpf = models.CharField(max_length=100, verbose_name='CPF Number')