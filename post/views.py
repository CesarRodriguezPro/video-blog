from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    fields = ['title', 'message', 'file']


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    fields = ['title', 'message', 'file']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    success_url = reverse_lazy('post:list_view')
    fields = ['date', 'title', 'message', 'file']


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post:list_view')
