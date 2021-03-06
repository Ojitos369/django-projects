from django.urls import path
from . import views

app_name = 'psico_front'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/<int:test_id>/', views.test, name='test'),
    path('section/<int:section_id>/', views.section, name='section'),
    path('login/', views.login, name='login'),
]