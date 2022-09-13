from unicodedata import name
from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    name = models.CharField(max_length=200)
    age = models.IntegerField(auto_created=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    