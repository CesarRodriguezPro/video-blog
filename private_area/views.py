from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from messages_system.models import MessagePost


# private_area


class Home(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'object_list': MessagePost.objects.filter(saved=False, read=False),

        }
        return render(request, 'private_area/main.html', context)

