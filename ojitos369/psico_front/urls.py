from django.urls import path
from . import views

app_name = 'psico_front'
urlpatterns = [
    path('', views.index, name='index'),
]