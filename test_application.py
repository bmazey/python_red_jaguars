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
        response3 = self.client.get('/api/recipe/Roasted Asparagus')
        self.assertTrue(200, response3.status_code)
        self.assertTrue(response3.json.get('name') == 'Roasted Asparagus')
        response4 = self.client.get('/api/recipe/Curried Lentils and Rice')
        self.assertTrue(200, response4.status_code)
        self.assertTrue(response4.json.get('name') == 'Curried Lentils and Rice')
        response5 = self.client.get('/api/recipe/Big Night Pizza')
        self.assertTrue(200, response5.status_code)
        self.assertTrue(response5.json.get('name') == 'Big Night Pizza')
        response6 = self.client.get("/api/recipe/Mic's Yorkshire Puds")
        self.assertTrue(200, response6.status_code)
        self.assertTrue(response6.json.get('name') == "Mic's Yorkshire Puds")
        response7 = self.client.get('/api/recipe/Old-Fashioned Oatmeal Cookies')
        self.assertTrue(200, response7.status_code)
        self.assertTrue(response7.json.get('name') == 'Old-Fashioned Oatmeal Cookies')
        response8 = self.client.get('/api/recipe/Blueberry Oatmeal Squares')
        self.assertTrue(200, response8.status_code)
        self.assertTrue(response8.json.get('name') == 'Blueberry Oatmeal Squares')
        response9 = self.client.get('/api/recipe/Curried chicken salad')
        self.assertTrue(200, response9.status_code)
        self.assertTrue(response9.json.get('name') == 'Curried chicken salad')









