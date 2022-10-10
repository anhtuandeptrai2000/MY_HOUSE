from django.urls import path

from .import views

urlpatterns = [
    # path('',views.fileUploadView),
    path('',views.register),
]