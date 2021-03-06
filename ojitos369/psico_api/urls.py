from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view
from . import views

schema_view = get_swagger_view(title='Pastebin API')
app_name = 'psico_api'
urlpatterns = [
    re_path(r'^$', schema_view),
    path('testing/', views.testing, name='testing'),
    path('get_test/<int:test_id>/', views.get_test, name='get_test'),
    path('get_sections/<str:mode>/<int:filter_id>/', views.get_sections, name='get_sections'),
    path('get_questions/<str:mode>/<int:filter_id>/', views.get_questions, name='get_questions'),
    path('get_choices/<str:mode>/<int:filter_id>/', views.get_choices, name='get_choices'),
    path('check_section/<int:section_id>', views.check_section, name='check_section'),
]