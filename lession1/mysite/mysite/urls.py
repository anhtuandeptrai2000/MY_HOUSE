"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('polls/', include('polls.urls')),
    path('user-auth/',include('user_auth.urls')),
    path('file-upload/',include('file_uploader.urls')),
    path('form-form-model/',include('form_form_model.urls')),
    path('registration/',include('registration.urls')),
    path('pagination/',include('pagination.urls')),
    path('adv_temp/',include('adv_temp.urls')),
    path('redis_cache/',include('redis_cache.urls')),
    path('login_session',include('login_session.urls')),
]
