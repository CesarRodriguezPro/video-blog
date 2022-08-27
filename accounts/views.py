from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import UserCreateForm, UpdatePasswordForm
from django.views.generic import CreateView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.messages import error, success

from .models import User


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    success_message = 'You Succesfully Sign Up'


class Profile(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'form': UpdatePasswordForm()
        }
        return render(request, 'accounts/profile.html', context)

    def post(self, request):

        # todo update edit profile tab and overview.

        password = request.POST['current_password']
        new_password = request.POST['new_password']
        re_enter_password = request.POST['re_enter_password']
        user = authenticate(request, username=request.user.username, password=password)
        if user is not None:
            user = User.objects.get(username=request.user.username)
            if new_password == re_enter_password:
                user.set_password(new_password)
                success(request, 'New Password is Update.')
            else:
                error(request, 'new password and re enter password have to match')
        else:
            error(request, 'Your current password is not working')
        return redirect("accounts:profile")

