# Python
import requests
import json
# Django
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import include
from psico_front.models import *

# User

def handler404(request, exception):
    return render(request, 'psico_front/404.html')

def index(request):
    domain = request.build_absolute_uri('/')[:-1]
    tests = []
    for i in range(3):
        test_info = requests.get(f'{domain}/psico_api/get_test/{i+1}/').json()
        test_info['url'] = 'psico_front:test'
        test_info['id'] = i+1
        tests.append(test_info)
    context = {
        'title': 'Test Psicometrico',
        'user_load': False,
        'tests': tests
    }
    return render(request, 'psico_front/index.html', context)

def test(request, test_id):
    domain = request.build_absolute_uri('/')[:-1]
    sections = requests.get(f'{domain}/psico_api/get_sections/test/{test_id}/')
    if sections.status_code == 400:
        raise Http404
    sections = sections.json()
    i = 0
    for seccion in sections:
        i+=1
        seccion['name'] = f'Seccion {i}'
        seccion['url'] = 'psico_front:section'
    context = {
        'title': f'Test {test_id}',
        'sections': sections,
    }
    return render(request, f'psico_front/test{test_id}.html', context)

def section(request, section_id):
    return render(request, f'psico_front/construccion.html')
    domain = request.build_absolute_uri('/')[:-1]
    questions = requests.get(f'{domain}/psico_api/get_questions/section/{section_id}/')
    if questions.status_code == 400:
        raise Http404
    questions = questions.json()
    