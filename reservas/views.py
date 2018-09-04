from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Cliente

def index(request):
    ordem = request.GET.get('ordem', 'registrado_em')
    direcao = request.GET.get('direcao', 'desc')
    campos = (field.name for field in Cliente._meta.fields)

    if ordem not in campos:
        ordem = 'registrado_em'

    if direcao == 'desc':
        direcao = '-'
    else:
        direcao = ''
    ordenacao = f'{direcao}{ordem}' #-nome ou nome

    ultimos_clientes = Cliente.objects.order_by(ordenacao)
    return render(request, 'reservas/index.html', {'ultimos_clientes': ultimos_clientes})

"""
class IndexView(ListView):
    model = Cliente
    template_name='reservas/index.html'
"""
def detalhe(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    # Para listas é get_list_or_404
    return render(request, 'reservas/detalhe.html', {'cliente': cliente})

def reservas(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'reservas/reservas.html', {'cliente': cliente})

def confirma(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    confirmados = request.POST.getlist('confirmacao')
    for reserva_id in confirmados: # pega os values dos inputs,que possuem os ids das reservas
        try:
            reserva = cliente.reserva_set.get(pk=reserva_id)
        except(KeyError, Reserva.DoesNotExist):
            # Reapresenta o form do cliente 
            return render('reservas/detalhe.html', {'cliente': cliente, 'error_message':"Código de reserva não encontrado.",})
        else:
            reserva.confirmada = True
            reserva.save()
            return HttpResponseRedirect(reverse('reservas:reservas', args=(cliente.id,)))