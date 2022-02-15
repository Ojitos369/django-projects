# Python
import requests
import json
import os
# Django
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import include
from psico_front.models import *

# User
from . import MyRequest

myrequest = MyRequest('http://localhost:8000/')

def handler404(request, exception):
    return render(request, 'psico_front/404.html')

def index(request):
    tests = []
    for i in range(3):
        test_info = myrequest.get_test(i+1)
        if test_info.status_code == 400:
            raise Http404
        test_info = test_info.json()
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
    sections = myrequest.get_section(test_id, 'test')
    if sections.status_code == 400:
        raise Http404
    sections = sections.json()
    i = 0
    for section in sections:
        i+=1
        section['name'] = f'Seccion {i}'
        section['url'] = 'psico_front:section'
    context = {
        'title': f'Test {test_id}',
        'sections': sections,
    }
    return render(request, f'psico_front/test{test_id}.html', context)

def section(request, section_id):
    questions = myrequest.get_questions(section_id, 'section')
    if questions.status_code == 400:
        raise Http404
    questions = questions.json()
    section_choices = myrequest.get_choices(section_id, 'section')
    if section_choices.status_code == 400:
        raise Http404
    section_choices = section_choices.json()
    choices = {}
    for question in questions:
        choices[question['id']] = []
    for choice in section_choices:
        choices[choice['question']].append(choice)
    for question in questions:
        question['choices'] = choices[question['id']]
    context = {
        'title': f'Seccion {section_id}',
        'questions': questions,
        'choices': choices,
        'section_id': section_id,
    }
    
    return render(request, f'psico_front/section.html', context)