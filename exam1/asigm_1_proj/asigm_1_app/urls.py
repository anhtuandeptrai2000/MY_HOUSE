from django.urls import path
from.import views

app = 'asigm_1_app'
urlpatterns = [
    # path('',views.index , name='index')
    path('<int:Person_id>/detail', views.detail , name='detail'),
    path('<int:Person_id>/results', views.results, name='results'),
]

