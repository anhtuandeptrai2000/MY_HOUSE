from email import message
from django import forms

class EmailForm(forms.Form):
    subject = ...
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)