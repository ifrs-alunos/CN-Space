from django.db import models
from .person import Person

class Passport(models.Model):
	numkber = models.CharField(max_length=100, verbose_name='Passport Number')
	issue_date = models.DateField(verbose_name='Issue Date')
	expiration_date = models.DateField(verbose_name='Expiration Date')
	owner = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)