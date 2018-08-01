import recipe
from unittest import TestCase
from flask import Flask
from recipe import db
from recipe import RecipeRoute
from recipe import get_app


class TestRecipe(TestCase):

    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()

    def test_simple_get(self):
        response = self.client.get('/api/recipe')
        print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('Brownies') == 'Use the betty crocker mix and add eggs, water, and vegetable oil. Then place in oven.')
    # def setUp(self):
    #     """
    #     Creates a new database for the unit test to use
    #     """
    #     self.app = Flask(__name__)
    #     db.init_app(self.app)
    #     with self.app.app_context():
    #         db.create_all()
    #
    # def tearDown(self):
    #     """
    #     Ensures that the database is emptied for next unit test
    #     """
    #     self.app = Flask(__name__)
    #     db.init_app(self.app)
    #     with self.app.app_context():
    #         db.drop_all()
    #
    # def test_post_and_get(self):
    #     response = self.app.test_client().post('/api/recipe', data=dict(name='Brownies', content='Use the betty crocker mix and add eggs, water, and vegetable oil. Then place in oven.'))
    #     print(response.json())
    # #     self.assertTrue(200, response.status_code)