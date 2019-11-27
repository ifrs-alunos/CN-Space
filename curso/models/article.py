from django.db import models
from .reporter import Reporter
from .magazine import Magazine

class Article(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateField() 
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
	magazines = models.ManyToManyField(Magazine)

	def __str__(self):
		return self.title