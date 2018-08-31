from django.db import models
from django.utils import timezone
# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    registrado_em = models.DateTimeField('data do registro')

    def reservas_nao_confirmadas(self):
        return self.reserva_set.filter(confirmada=False)
    
    def reservas_confirmadas(self):
        return self.reserva_set.filter(confirmada=True)

    def __str__(self):
        return self.nome
    
    def registro_eh_antigo(self):
        um_ano = timezone.now() - timezone.timedelta(days = 365)
        return self.registrado_em < um_ano

    registro_eh_antigo.admin_order_field = 'registrado_em' # indica o nome do campo a ser usado na ordenação
    registro_eh_antigo.boolean = True # indica que a coluna é boolean pra mostrar o icone inves de True ou False
    registro_eh_antigo.short_description = 'Cliente é antigo?' # Muda o nome da coluna pra mostrar


class Reserva(models.Model):
    data_reserva = models.DateTimeField('data da reserva')
    data_evento = models.DateTimeField('data do evento')
    pessoas = models.IntegerField(default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente} - {self.data_evento}"