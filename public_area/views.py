from django.views.generic import View
from django.shortcuts import render, redirect
from post.models import Post
from public_area.forms import MessagesPostForm
from django.contrib.messages import success, error

# public area


class Home(View):
    def get(self, request):
        context = {
            'list_items': Post.objects.all().order_by('-last_updated')[:10],
            'contact_form': MessagesPostForm(),
        }
        return render(request, "public_area/main.html", context)

    def post(self, request):

        message = MessagesPostForm(request.POST)
        if message.is_valid():
            message.save()
            success(request, "Message was send")
            return redirect('public_area:home')

        error(request, "there was a error, please try again later")
        return redirect('public_area:home')

