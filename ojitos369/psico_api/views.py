# Python
import json
from multiprocessing import context
from unittest import result
# Django
from django.shortcuts import render
from django.forms.models import model_to_dict

# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
# User
from .models import *
from .serializers import *
from .sections_evals.test_eval import check_test


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
def get_sections(request, mode, filter_id):
    """
    Get Sections
    Get a data from sections depending on the mode and filter_id
    
    Args:
    - path parameter:
        - mode: str (required)
            - Options:
                - test
                - section
                -all
        - filter_id: int (required)
    
    return:
    a json list with the sections data:
        - test: Test
        - text: str
        - tipo: tipo
    
    Raises:
        - 400: if the mode or filter_id does not exist
    """
    if mode == 'test':
        sections = Section.objects.filter(test__id=filter_id)
    elif mode == 'section':
        sections = Section.objects.filter(pk=filter_id)
    elif mode == 'all':
        sections = Section.objects.all()
    else:
        return Response({"error": "Mode not found"}, status=404)
    if len(sections) == 0:
        return Response({"error": "Id not found in this mode"}, status=404)
    serializer = SectionSerializer(sections, many=True)
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
                - section
                - question
                - all
        - filter_id: int (required)
    
    return:
    a json list with the questions data:
        - section: Section
        - text: str
        - tipo: tipo
    
    Raises:
        - 400: if the mode or filter_id does not exist
    """
    if mode == 'test':
        questions = Question.objects.filter(section__test__id=filter_id)
    elif mode == 'section':
        questions = Question.objects.filter(section__id=filter_id)
    elif mode == 'question':
        questions = Question.objects.filter(pk=filter_id)
    elif mode == 'all':
        questions = Question.objects.all()
    else:
        return Response({"error": "Mode not found"}, status=404)
    if len(questions) == 0:
        return Response({"error": "Id not found in this mode"}, status=404)
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
                - section
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
        choices = Choice.objects.filter(question__section__test__id=filter_id)
    elif mode == 'section':
        choices = Choice.objects.filter(question__section__id=filter_id)
    elif mode == 'question':
        choices = Choice.objects.filter(question__id=filter_id)
    elif mode == 'choice':
        choices = Choice.objects.filter(pk=filter_id)
    elif mode == 'all':
        choices = Choice.objects.all()
    else:
        return Response({"error": "Mode not found"}, status=404)
    if len(choices) == 0:
        return Response({"error": "Id not found in this mode"}, status=404)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def check_section(request, section_id):
    """
    """
    
    if section_id > 3:
        return render(request, f'psico_front/construction.html')
    
    result = check_test.check_section(request.data, section_id)
    context = {
        'title': f'Resultados Section {section_id}',
        'result': result
    }
    
    return render(request, f'psico_front/check_section.html', context)