# Python

# Django
from django.forms.models import model_to_dict

# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
# User
from .models import *
from .serializers import *


@api_view(['GET'])
def index(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def get_test(request, test_id):
    test = Test.objects.get(pk=test_id)
    serializer = TestSerializer(test, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_test(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)