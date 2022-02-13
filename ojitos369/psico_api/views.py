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
def testing(request, param1, param2=None):
    """"""
    data = {
        'param1': param1,
        'param2': param2
    }
    return Response(data)

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
def get_questions(request, mode, filter_id):
    """
    Get Questions
    Get a data from questions depending on the mode and filter_id
    
    Args:
    - path parameter:
        - mode: str (required)
            - Options:
                - test
                - seccion
                - question
                - all
        - filter_id: int (required)
    
    return:
    a json list with the questions data:
        - seccion: Seccion
        - text: str
        - tipo: tipo
    
    Raises:
        - 400: if the mode or filter_id does not exist
    """
    if mode == 'test':
        questions = Question.objects.filter(seccion__test__id=filter_id)
    elif mode == 'seccion':
        questions = Question.objects.filter(seccion__id=filter_id)
    elif mode == 'question':
        questions = Question.objects.filter(id=filter_id)
    elif mode == 'all':
        questions = Question.objects.all()
    else:
        return Response({"error": "Mode not found"}, status=404)
    if len(questions) == 0:
        return Response({"error": "id not found in this mode"}, status=404)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_choices(request, mode, filter_id):
    """
    Get Choices
    Get a data from choices depending on the mode and filter_id
    
    Args:
    - path parameter:
        - mode: str (required)
            - Options:
                - test
                - seccion
                - question
                - choice
                - all
        - filter_id: int (required)
    
    return:
    a json list with the choices data:
        - question: Question
        - text: str
    
    Raises:
        - 400: if the mode or filter_id does not exist
    """
    
    if mode == 'test':
        choices = Choice.objects.filter(question__seccion__test__id=filter_id)
    elif mode == 'seccion':
        choices = Choice.objects.filter(question__seccion__id=filter_id)
    elif mode == 'question':
        choices = Choice.objects.filter(question__id=filter_id)
    elif mode == 'choice':
        choices = Choice.objects.filter(id=filter_id)
    elif mode == 'all':
        choices = Choice.objects.all()
    else:
        return Response({"error": "Mode not found"}, status=404)
    if len(choices) == 0:
        return Response({"error": "id not found in this mode"}, status=404)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_test(request):
    serializer = TestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)