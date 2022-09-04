from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list_view'),
    path('create/', views.PostCreateView.as_view(), name='create'),
]
