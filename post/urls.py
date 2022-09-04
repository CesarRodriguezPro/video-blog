from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list_view'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.PostDeleteView.as_view(), name='delete'),
    path('detail/<pk>', views.PostDetailView.as_view(), name='detail'),
]
