from unittest import TestCase
from flask import Flask
import json

'''
this does not work yet!!
'''


class appDBTests(TestCase):
    def test_application(self):



    # def setUp(self):
    #     """
    #     Creates a new database for the unit test to use
    #     """
    #     self.app = Flask(__name__)
    #     db.init_app(self.app)
    #     with self.app.app_context():
    #         db.create_all()
    #         # self._db()  # Your function that adds test data.
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
    #     response = self.app.test_client().post('/rumor', data=dict(name='Brownies', content='Use the betty crocker mix and add eggs, water, and vegetable oil. Then place in oven.'))
    #     print(response.json())
    #     self.assertTrue(200, response.status_code)
