from django.db import models

class creditcard(models.Model):
    number = models.CharField(max_length=16)
    date = models.DateTimeField()
    name = models.CharField(max_length=200)

class list_object(models.Model):
    name = models.CharField(max_length=10)
    img_url = models.URLField()