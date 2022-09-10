from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField


class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now())
    file = models.FileField(upload_to='files/', blank=True, null=True)
    thumbnail = ImageField(upload_to='thumbnail/')
    message = models.TextField(blank=True, null=True)
    time = models.DateTimeField(default=timezone.now())
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.date} -> {self.title} "
