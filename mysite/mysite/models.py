from django.db import models
from PIL import Image

class Creditcard(models.Model):
    number = models.CharField(max_length=16, null=False)
    date = models.DateTimeField()
    name = models.CharField(max_length=200, null=False)
    safety_key = models.CharField(max_length=3, null=False)


class SellObjects(models.Model):
    name = models.CharField(max_length=200, null=False)
    img = models.ImageField(upload_to='photo')
