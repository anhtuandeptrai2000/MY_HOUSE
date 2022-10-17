from django.urls import path
from .views import show_info, country_info

app_name = 'adv_temp'
urlpatterns = [
    path('<str:name>/', show_info),
    path('country-detail/<str:country_name>/', country_info, name='countrydetail'),
]