from django import forms

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     file = forms.FileField()


class RegisterForm(forms.Form):
    id = forms.IntegerField(label="Id")
    name  = forms.CharField(label="Name",max_length=100)
    age = forms.DateField(label="age")
    color = forms.CharField(label="Color",max_length=100)