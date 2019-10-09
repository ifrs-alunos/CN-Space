import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treasure.settings')
django.setup()

from desenho.models.animation import Animacao

# anim = Animacao.objects.all()
# teste = Animacao(2,'oie', 'oie', [])
# teste.nomee = 'teste'

# print(anim)