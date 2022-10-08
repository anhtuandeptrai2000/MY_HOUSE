from django.urls import path
from.import views

app = "asigm_1_tapp"
urlpatterns = [
    path('', views.index , name='index'),
    path('<int:question_id>/detail', views.detail , name='detail'),
    
]
