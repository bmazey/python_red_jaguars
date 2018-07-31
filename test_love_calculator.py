from unittest import TestCase
import match
import application
import person
from flask import Flask

from application import get_app

class LoveCalculatorTest(TestCase):

    def test_person(self):
        person_a = application.person
        person_b = application.person
        assert application.match(person_a, person_b) == "You are 70% compatible"

        person_a_1 = application.person
        person_b_1 = application.person
        assert application.match(person_a_1 , person_b_1) == "You are 50% compatible"

    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()
    def test_simple_get(self):
        response = self.client.get('/api/person')
        print(response.get_json())
        self.assertTrue(200, response.status_code)
     #   self.assertTrue(response.get_json().get('brandon') == 'listens to selena gomez')





