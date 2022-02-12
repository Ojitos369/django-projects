# Python
import json
# Django
from django.forms.models import model_to_dict

# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
# User
from .models import *
from .serializers import *


@api_view(['GET'])
def get_test(request, test_id):
    """
    Get test
    
    Get a data from test

    Args:
    - path parameter:
        - test_id: int (required)

    Returns:
        a json with the test data:
            - test_id: int
            - test_name: str
            - test_description: str
    
    Raises:
        - 400: if the test_id does not exist
    """
    
    test = Test.objects.filter(pk=test_id)
    if len(test) == 0:
        return Response({"error": "Test not found"}, status=404)
    serializer = TestSerializer(test[0], many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_questions(request, test_id):
    """
    Get Questions
    Get a data from all questions of a test
    
    Args:
    - path parameter:
        - test_id: int (required)
    
    return:
    a json list with the questions data:
        - seccion: Seccion
        - text: str
        - tipo: tipo
    
    Raises:
        - 400: if the test_id does not exist
    """
    
    questions = Question.objects.filter(seccion__test__id=test_id)
    if len(questions) == 0:
        return Response({"error": "Test not found"}, status=404)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_choices(request, seccion_id):
    """
    Get Choices
    Get a data from all choices of a seccion
    
    Args:
    - path parameter:
        - seccion_id: int (required)
    
    return:
    a json list with the choices data:
        - question: Question
        - text: str
    
    Raises:
        - 400: if the question_id does not exist
    """
    
    choices = Choice.objects.filter(question__seccion__id=seccion_id)
    if len(choices) == 0:
        return Response({"error": "Seccion not found"}, status=404)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_test(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)