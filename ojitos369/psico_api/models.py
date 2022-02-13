# Python
from datetime import datetime
import datetime as dt
from unicodedata import name
# Django
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Section(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    description = models.TextField(max_length = 200, blank = True, null = True)
    duration = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name
class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    tipo = models.TextField(max_length = 200, blank = True, null = True)
    
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(max_length = 200)
    
    def __str__(self):
        return self.text
