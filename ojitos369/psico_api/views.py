# Apis for psico_api
# Django
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# User
from .models import *
# Python
import json

@api_view(['GET'])
def index(request):
    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_test(request, test_id):
    test = Test.objects.get(pk=test_id)
    test = model_to_dict(test)
    test['url'] = f'/psico_front/test/{test_id}.html'
    return Response(test, status=status.HTTP_200_OK)