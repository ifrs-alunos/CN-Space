from django.db import models
from post.models.base import *
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .topic import Topic

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
	updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

	
		
