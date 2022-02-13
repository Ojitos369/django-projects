# Python
import requests
# Django
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import include

from ojitos369.psico_api.models import Seccion
# User

def handler404(request, exception):
    return render(request, 'psico_front/404.html')

def index(request):
    domain = request.build_absolute_uri('/')[:-1]
    tests = []
    for i in range(3):
        test_info = requests.get(f'{domain}/psico_api/get_test/{i+1}/').json()
        
        test_info['url'] = i+1
        tests.append(test_info)
    context = {
        'user_load': False,
        'tests': tests
    }
    return render(request, 'psico_front/index.html', context)

def test(request, test_id):
    if test_id > 3:
        raise Http404
    domain = request.build_absolute_uri('/')[:-1]
    seccion = requests.get(f'{domain}/psico_api/get_seccion/test/{test_id}/').json()
    context = {
        'seccion': seccion,
    }
    return render(request, f'psico_front/test{test_id}.html', context)