from django.urls import path
from bloguinho import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home')
]