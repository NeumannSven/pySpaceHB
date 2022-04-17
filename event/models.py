from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=80)
    content = models.TextField()
    date = models.DateTimeField()
    