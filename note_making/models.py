from django.db import models
from django.utils import timezone

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_of_creation = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, default=None)

    def __str__(self):
        return f"title: {self.title}, Date of Creation: {self.date_of_creation}"
