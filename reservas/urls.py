from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # /reservas/
    url(r'^(?P<cliente_id>[0-9]+)/$', views.detalhe, name='detalhe'), # /reservas/1/
    url(r'^(?P<cliente_id>[0-9]+)/lista/$', views.reservas, name='reservas'), # /reservas/1/lista
    url(r'^(?P<cliente_id>[0-9]+)/confirma/$', views.confirma, name='confirma'), # /reservas/1/confirma
]