# Python
import requests
# Django
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404


def index(request):
    tests = []
    for i in range(3):
        test_info = requests.get(reverse('psico_api:get_test', args=(i+1,))).json()
        tests.append(test_info)
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