# Python
# Django
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404


def index(request):
    tests = []
    for i in range(3):
        test = {
            'name': f'Test {i + 1}',
            'description': f'Description {i + 1}',
            'url': '#'
        }
        tests.append(test)
    footer_data = []
    for i in range(5):
        info = {
            'text': f'Info {i + 1}',
            'url': '#'
        }
        footer_data.append(info)
    context = {
        'user_load': False,
        'tests': tests,
        'footer_data': footer_data
    }
    return render(request, 'psico_front/index.html', context)