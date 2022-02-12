# Python
import requests
# Django
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import include
# User

def index(request):
    domain = request.build_absolute_uri('/')[:-1]
    tests = []
    for i in range(3):
        test_info = requests.get(f'{domain}/psico_api/get_test/{i+1}/').json()
        
        test_info['url'] = i+1
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

def test(request, test_id):
    domain = request.build_absolute_uri('/')[:-1]
    return render(request, f'psico_front/test{test_id}.html')