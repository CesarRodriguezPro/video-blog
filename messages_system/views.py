from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DetailView, DeleteView, UpdateView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MessagePost


class MessageListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'object_list': MessagePost.objects.filter(saved=False)
        }

        return render(request, "messages_system/messagepost_list.html", context)

    model = MessagePost


class MessageSaveView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'object_list': MessagePost.objects.filter(saved=True),
            'is_message_saved': True,
        }
        return render(request, "messages_system/messagepost_list.html", context)


class CreateMessageSave(LoginRequiredMixin, View):
    def get(self, request, pk):
        MessagePost.objects.filter(pk=pk).update(saved=True)
        return redirect('message_post:list')


class UnSavedMessage(LoginRequiredMixin, View):
    def get(self, request, pk):
        MessagePost.objects.filter(pk=pk).update(saved=False)
        return redirect('message_post:view_saved')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MessagePost
    success_url = reverse_lazy('message_post:list')
    fields = ['title', 'message', 'file']


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MessagePost
    success_url = reverse_lazy('message_post:list')
    fields = ['title', 'message', 'file']


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = MessagePost
    success_url = reverse_lazy('message_post:list')
    fields = ['date', 'title', 'message', 'file']


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MessagePost
    success_url = reverse_lazy('message_post:list')
