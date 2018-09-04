from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bloguinho.models import Post
from django.urls import reverse_lazy

# Create your views here.

class HomeListView(ListView):
    model = Post
    template_name = 'bloguinho/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'bloguinho/detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'bloguinho/new_post.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'bloguinho/post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'bloguinho/post_delete.html'
    success_url = reverse_lazy('home') # não executa a url até terminar de deletar o post