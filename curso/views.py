from django.shortcuts import render, get_object_or_404, redirect 
from .models.article import Article 
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def index(request):
	articles = Article.objects.order_by('-pub_date')[:2]
	context = {'articles': articles}
	return render(request, 'curso/index.html', context)

@login_required
@permission_required('curso.publish_article', raise_exception = True)
def publish(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	try:
		# Seu codigo para publicar artigos
		return redirect('curso:index')

	except:
		#Aqui podem ser armazenadas em log informacoes relevantes
		context = {}
		return render(request, 'curso/index.html', context)


@login_required
@permission_required('curso.view_article', raise_exception = True)
def list_articles(request):
	articles = Article.objects.order_by('-pub_date')[:2]
	context = {'articles': articles}
	return render(request, 'curso/index.html', context)



def create(request):
	message = ''
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			message = 'HAS BEEN SUCCESFULLY SAVED'

	else:
		form = ArticleForm()

	context = {'form': form,
				'message': message,
				}

	return render(request, 'curso/article.html', context)

def edit(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	try:
		if request.method == "POST":
			form = ArticleForm(request.POST, instance = article)
			if form.is_valid():
				form.save()
				message = "HAS BEEN SUCCESSFULLY EDITED"
				context = {
					"form": form,
					"message": message,
				}
				return redirect('curso:index')
		else:
			form = ArticleForm(instance = article)
			context = {"form": form,
						"action": "edit",
						"article_id": article_id,
			}
			return render(request, "curso/article.html", context)

	except:
		#Aqui podem ser armazenadas em log informacoes relevantes
		context = {}
		return render(request, "curso/index.html", context)

def delete(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	try:
		article.delete()
		return redirect('curso:index')
	except:
		context = {}
		return render(request, "curso/index.html", context)