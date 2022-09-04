from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/signup.html'), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('list_view/', views.ListViewAccounts.as_view(), name='list_view'),
    path('password_update/<pk>/', views.UpdatePasswordView.as_view(), name='password_update'),
    path('update/<pk>/', views.AccountsUpdate.as_view(), name='updateView'),
    path('delete/<pk>/', views.AccountsDelete.as_view(), name='deleteView'),
]