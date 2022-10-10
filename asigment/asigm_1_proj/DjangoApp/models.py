from urllib import request
from django.db import models

# Create your models here.
class Animal(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    age = models.DateTimeField()
    color = models.CharField(max_length=50)