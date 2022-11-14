from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProjectList.as_view(), name='home'),
    path('', views.ProjectDetail.as_view(), name='post_detail1'),
]