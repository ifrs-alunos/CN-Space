from django.forms import ModelForm 
from .models.article import Article 

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = '__all__'
   