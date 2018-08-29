from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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
    return render(request, 'reservas.html', {'cliente': cliente})

def confirma(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    confirmados = request.POST.getlist('confirmacao')
    for reserva_id in confirmados: # pega os values dos inputs,que possuem os ids das reservas
        try:
            reserva = cliente.reserva_set.get(pk=reserva_id)
        except(KeyError, Reserva.DoesNotExist):
            # Reapresenta o form do cliente 
            return render('detalhe.html', {'cliente': cliente, 'error_message':"Código de reserva não encontrado.",})
        else:
            reserva.confirmada = True
            reserva.save()
            return HttpResponseRedirect(reverse('reservas:reservas', args=(cliente.id,)))