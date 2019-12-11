from django.shortcuts import render, redirect
from .models.animation import Animacao
from .models.person import Personagem


# Create your views here.



def animacao(request):
	animacoes = Animacao.objects.order_by('-nomee')
	context = { 'animacoes': animacoes}
	return render(request,'base.html', context)

def steven(request):
	context = {'animacao': animacao}
	return render(request,'desenho/teste.html', context)

def aventura(request):
	context = {'animacao': animacao}
	return render(request,'desenho/aventura.html', context)

def gumball(request):
	context = {'animacao': animacao}
	return render(request,'desenho/gumball.html', context)


