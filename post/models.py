from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now())
    file = models.FileField(upload_to='files/', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.date} -> {self.title} "
