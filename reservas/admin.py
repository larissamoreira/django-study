from django.contrib import admin

# Register your models here.

from .models import Cliente, Reserva


class ReservasInline(admin.TabularInline):  # Aparece o relacionamento.
    model = Reserva
    extra = 3  # Quantos itens vao ser apresentados


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'registro_eh_antigo') # Como vai mostrar na lista de clientes
    list_filter = ['registrado_em'] # permite que um filtro seja aplicado a lista
    search_fields = ['nome'] # adiciona um input de pesquisa

    fieldsets = [
        (None, {"fields": ["nome", "email", "telefone", "endereco"]}),
        ("Datas", {"fields": ["registrado_em"]}),
    ]
    inlines = [ReservasInline]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Reserva)
