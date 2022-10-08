from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
TITLE_CHOICES = (
    ('MR','Mr'),
    ('MRS','Mrs'),
    ('MS','Ms'),
)

class Author(models.Model):
    name=models.CharField(max_length = 100)
    title = models.CharField(max_length=3,choices=TITLE_CHOICES)
    birth_date = models.DateTimeField()

class Book(models.Model):
    name = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name','title','birth_date']
        widgets = { 'birth_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}), }

class BookFrom(ModelForm):
    class Meta:
        model = Book
        fields = ['name','authors']