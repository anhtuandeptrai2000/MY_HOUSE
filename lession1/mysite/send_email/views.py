from django.shortcuts import render

# Create your views here.

from django.dispatch import receiver
from .form import EmailForm
from django.core.mail import send_mail
from django.conf import settings

