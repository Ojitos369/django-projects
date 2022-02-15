import requests
import os

class MyRequest:
    
    def __init__(self, domain):
        """
        MyRequest
        Generate a request in base the domain gived
        
        example:
        domain = 'http://localhost:8000/'
        
        Have 4 methods:
        
        """
        if domain.endswith('/'):
            domain = domain[:-1]
        self.domain = domain
        
    def get_test(self, test_id):
        """
        Get Test
        Get test in base to user input
        
        Args:
            - test_id: str
        
        Returns:
            - a request petition to get the test
        """
        return requests.get(f'{self.domain}/psico_api/get_test/{test_id}/')
    
    def get_section(self, filter_id, mode = 'section'):
        """
        Get section
        Get a sections in base to id and mode to filter
        
        Args:
            - filter_id: int
            - mode: str
        """
        return requests.get(f'{self.domain}/psico_api/get_sections/{mode}/{filter_id}/')
    
    def get_questions(self, filter_id, mode = 'question'):
        """
        Get questions
        Get questions in base to id and mode to filter
        
        Args:
            - filter_id: int
            - mode: str
        """
        return requests.get(f'{self.domain}/psico_api/get_questions/{mode}/{filter_id}/')
    
    def get_choices(self, filter_id, mode = 'choice'):
        """
        Get choices
        Get choices in base to id and mode to filter
        
        Args:
            - filter_id: int
            - mode: str
        """
        return requests.get(f'{self.domain}/psico_api/get_choices/{mode}/{filter_id}/')
    