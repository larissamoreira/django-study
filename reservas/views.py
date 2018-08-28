from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Cliente

def index(request):
    ultimos_clientes = Cliente.objects.order_by('-registrado_em')
    return render(request, 'index.html', {'ultimos_clientes': ultimos_clientes})
def detalhe(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    # Para listas é get_list_or_404
    return render(request, 'detalhe.html', {'cliente': cliente})

def reservas(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render('reservas.html', {'cliente': cliente})

def confirma(request, cliente_id):
    cliente = Cliente.objects.filter(cliente_id)
    return render('reservas.html', {'cliente': cliente})