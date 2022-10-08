from pyexpat import model
from unicodedata import name
from django.db import models


# Create your models here.

class Person(models.Model):
    person_id = models.AutoField(auto_created=True,primary_key=True)
    persion_name = models.CharField(max_length=200)
    person_age = models.IntegerField(auto_created=True)
    person_address = models.CharField(max_length=200)
    person_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.persion_name

class Manufacturer(models.Model):
    name = models.CharField(max_length =200)
    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    name_car = models.CharField(max_length = 100)
    company = models.CharField(max_length =100)
    def __str__(self) -> str:
        return self.name_car