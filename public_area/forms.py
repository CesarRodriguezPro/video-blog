from django import forms
from messages_system.models import MessagePost


class MessagesPostForm(forms.ModelForm):
    class Meta:
        model = MessagePost
        fields = ['sender_name', 'email', 'subject', 'message']

        default_classes = 'form-control'

        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class':  'form-control', 'placeholder': 'Email', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Messages', 'required': True}),
        }