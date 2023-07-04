from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = 'homepage.html'


class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme


class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super(Detalhesfilme, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar tabela de filmes pelos que têm a mesma categoria do atual
        # (ou seja, o object -- cujo equivalente na view obtemos usando a
        # função get_object()):
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


""" Subsitituído por uma classe genérica, já que apenas retorna um template
def homepage(request):
    return render(request, 'homepage.html')"""

""" Substituído por uma classe genérica de listagem
def homefilme(request):
    context = {}
    lista_filmes = Filme.objects.all()
    context['lista_filmes'] = lista_filmes
    return render(request, "homefilmes.html", context)"""
