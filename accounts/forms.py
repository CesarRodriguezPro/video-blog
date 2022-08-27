from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        model = User


class UpdatePasswordForm(forms.Form):
    current_password = forms.CharField(max_length=225, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=225, widget=forms.PasswordInput)
    re_enter_password = forms.CharField(max_length=225, widget=forms.PasswordInput)
