from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    fields = ['title', 'message', 'file', 'thumbnail']


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    fields = ['title', 'message', 'file', 'thumbnail']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    fields = ['date', 'title', 'message', 'file', 'thumbnail']


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post:list_view')
