import json
from random import choices
import re
from os import path

from soupsieve import match
from psico_api.models import *
# from db_info.db_scripts import *


current_path = path.dirname(path.abspath(__file__))
def make_test():
    t1 = Test(name = 'Test 1', description = 'Test 1 description')
    t2 = Test(name = 'Test 2', description = 'Test 2 description')
    t3 = Test(name = 'Test 3', description = 'Test 3 description')
    t1.save()
    t2.save()
    t3.save()


def test_info():
    t = Test.objects.all()
        
    for test in t:
        print()
        print(f'{test.pk}.- {test.name}')
        sections = test.section_set.all()
        for s in sections:
            print(f'{s.pk}.- {s.description} - {s.duration} ({s.test.pk})')
        print()

    
def make_sections():
    with open(f'{current_path}/sectiones.txt', 'r') as f:
        sections = f.readlines()
        
    expresion = "^(\d), (.*), (\d+)$"
    for section in sections:
        match_obj = re.match(expresion, section)
        if match_obj:
            test_id = int(match_obj.group(1))
            description = str(match_obj.group(2))
            duration = int(match_obj.group(3))
            section = Section(test_id = test_id, description = description, duration = duration)
            section.save()

def section_info():
    sections = Section.objects.all()
    
    for s in sections:
        print()
        print(f'{s.pk}.- {s.description} - {s.duration} ({s.test.pk})')
        questions = s.question_set.all()
        for q in questions:
            print(f'{q.pk}.- {q.text} - {q.tipo} ({q.section.test.pk} > {q.section.pk})')
        print()
        
def make_questions():
    with open(f'{current_path}/preguntas.txt', 'r') as f:
        questions = f.readlines()
    
    expresion = "^(\d+), '(.*)', '(.*)'$"
    for q in questions:
        match_obj = re.match(expresion, q)
        if match_obj:
            section_id = int(match_obj.group(1))
            text = str(match_obj.group(2))
            tipo = str(match_obj.group(3))
            question = Question(section_id = section_id, text = text, tipo = tipo)
            question.save()

def question_info():
    questions = Question.objects.all()
    
    for q in questions:
        print()
        print(f'{q.pk}.- {q.text} ({q.section.test.pk} > {q.section.pk})')
        
        choices = q.choice_set.all()
        for c in choices:
            print(f'{c.pk}.- {c.text} ({q.section.test.pk} > {q.section.pk} > {q.pk})')
        print()
        
def make_choices():
    with open(f'{current_path}/respuestas.txt', 'r') as f:
        choices = f.readlines()
    
    expresion = "^(\d+), '(.*)'$"
    question_id = 0
    info_id = 0
    for c in choices:
        match_obj = re.match(expresion, c)
        if match_obj:
            id = int(match_obj.group(1))
            text = str(match_obj.group(2))
            if id != info_id:
                info_id = id
                question_id +=1
            choice = Choice(question_id = question_id, text = text)
            choice.save()
            
def choice_info():
    choices = Choice.objects.all()
    for c in choices:
        print(f'{c.pk}.- {c.text} ({c.question.section.test.pk} > {c.question.section.pk} > {c.question.pk})')


def main():
    make_test()
    make_sections()
    make_questions()
    make_choices()