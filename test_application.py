from unittest import TestCase
from application import get_app

# adding comments for travis CI


class RecipeTest(TestCase):
    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()

    def test_simple_recipe_get(self):
        response = self.client.get('/recipe')
        print(response.get_json())
        self.assertTrue(200, response.status_code)
