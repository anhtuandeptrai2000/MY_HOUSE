from django.db import models

# Create your models here.

class Person(models.Model):
    person_id = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    persion_name = models.CharField(max_length=200)
    person_age = models.IntegerField(auto_created=True)
    person_address = models.CharField(max_length=200)
    person_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.person_id