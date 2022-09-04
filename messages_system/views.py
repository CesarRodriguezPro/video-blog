from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MessagePost


class MessageListView(LoginRequiredMixin, ListView):
    model = MessagePost


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MessagePost
    success_url = reverse_lazy('post:list_view')
    fields = ['title', 'message', 'file']


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MessagePost
    success_url = reverse_lazy('post:list_view')
    fields = ['title', 'message', 'file']


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = MessagePost
    success_url = reverse_lazy('post:list_view')
    fields = ['date', 'title', 'message', 'file']


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MessagePost
    success_url = reverse_lazy('post:list_view')
