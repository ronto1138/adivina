from django.db import models

# Create your models here.
class User(models.Model):
    iniciales = models.CharField(max_length = 128)
    1intentos = models.IntegerField()

class Rankings(models.Model):
    iniciales = models.CharField(max_length = 128)
    intentos = models.IntegerField()