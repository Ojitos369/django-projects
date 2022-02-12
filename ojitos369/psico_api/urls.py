from django.urls import path
from . import views

app_name = 'psico_api'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_test/<int:test_id>/', views.get_test, name='get_test'),
]