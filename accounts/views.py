from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from .forms import UserCreateForm, UpdatePasswordForm, UserUpdateForm
from django.views.generic import CreateView, View, ListView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.messages import error, success
from .models import User


class SignUp(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    success_message = 'You Successfully Sign Up'


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


class ListViewAccounts(LoginRequiredMixin, ListView):
    model = User
    template_name = 'accounts/list_view.html'


class UpdatePasswordView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return render(request, "accounts/change_password.html", context={'pk': pk})

    def post(self, request, pk=None):
        form_data = request.POST
        if form_data['password1'] == form_data['password2'] and len(form_data['password1']) > 7:
            u = User.objects.get(pk=pk)
            u.set_password(form_data['password1'])
            success(request, "Password Update Successfully ")
            u.save()
            return redirect(reverse('accounts:list_view'))
        else:
            error(request, "The Passwords Do Not Match or needs to be more that 8 characters")
            return redirect("accounts:password_update", pk)


class AccountsUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_update_form.html'
    success_url = reverse_lazy('accounts:list_view')


class AccountsDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('accounts:list_view')
    template_name = 'accounts/user_confirm_delete.html'
