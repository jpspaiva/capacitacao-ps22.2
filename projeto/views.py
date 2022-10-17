from multiprocessing import context
from django.shortcuts import render

from projeto.models import Inicio
from projeto.models import QuemSomos
from projeto.models import Servicos
from projeto.models import Portfolio
from projeto.models import Contato
from projeto.models import Formulario

# Create your views here.
def home(request):
    inicio = Inicio.objects.last()
    quemsomos = QuemSomos.objects.last()
    servicos = Servicos.objects.last()
    portfolio = Portfolio.objects.last()
    contato = Contato.objects.last()


    context = {
        'inicio': inicio,
        'quemsomos': quemsomos,
        'servicos': servicos,
        'portfolio': portfolio,
        'contato': contato
        
    }
    
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        whatsapp = request.POST['whatsapp']
        mensagem = request.POST['mensagem']

        form = Formulario(nome=nome, email=email, whatsapp=whatsapp, mensagem=mensagem)
        form.save()
        
    return render(request, 'index.html', context)