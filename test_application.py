from unittest import TestCase
from application import get_app

# adding comments for travis CI


class RecipeTest(TestCase):
    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()

    def test_simple_recipe_get(self):
        response = self.client.get('/api/recipe/Cranberry and Apple Stuffed Acorn Squash Recipe')
        print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.json.get('name') == 'Cranberry and Apple Stuffed Acorn Squash Recipe')
        response2 = self.client.get('/api/recipe/Crock Pot Roast')
        self.assertTrue(200, response2.status_code)
        self.assertTrue(response2.json.get('name') == 'Crock Pot Roast')


