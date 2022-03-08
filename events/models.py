from django.db import models


# Create your models here.
class Event(models.Model):
    image = models.ImageField(upload_to='event_images/')
    text = models.CharField(max_length=300)