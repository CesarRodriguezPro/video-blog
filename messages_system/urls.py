from django.urls import path
from . import views

app_name = 'message_post'

urlpatterns = [
    path('', views.MessageListView.as_view(), name='list'),
    path('create/', views.MessageCreateView.as_view(), name='create'),
    path('update/<pk>/', views.MessageUpdateView.as_view(), name='update'),
    path('delete/<pk>', views.MessageDeleteView.as_view(), name='delete'),
    path('detail/<pk>', views.MessageDetailView.as_view(), name='detail'),
    path('message_save/<pk>', views.CreateMessageSave.as_view(), name='save'),
    path('unSave_message_save/<pk>', views.UnSavedMessage.as_view(), name='unsaved'),
    path('saved_messages/', views.MessageSaveView.as_view(), name='view_saved'),
]