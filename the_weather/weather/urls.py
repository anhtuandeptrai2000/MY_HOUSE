from django.urls import path,include

urlpatterns = [ 
    path('api',include('weather.api.urls')),
]