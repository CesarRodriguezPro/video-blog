from django.db import models
from django.utils import timezone


class MessagePost(models.Model):
    time = models.DateTimeField(default=timezone.now)
    sender_name = models.CharField(max_length=225,)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    read = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.time} -> {self.email} | {self.subject}"