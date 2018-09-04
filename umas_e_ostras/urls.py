from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservas/', include(('reservas.urls', 'reservas'), namespace='reservas')),
    path('bloguinho/', include('bloguinho.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'))
]
