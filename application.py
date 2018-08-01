import json
from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import fields


# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
application = Flask(__name__)
api = Api(application)

# allowing us to access the json file with recipes
with open('recipe.json') as file:
    data = json.load(file)

# this class and the line below is creating our api
@api.route("/api/recipe/<string:name>")
class Recipe(Resource):
    def get(self, name):
        # json file we're accessing is a list of jsons
        # to check each json in the list we had to create a for loop and trace through each one
        for index in range(0, 9):
            # the if statement is checking to see whether the name inputted is the same as the name at that position
            if data[index].get('name') == name:
                # this creates a new variable that is assigned the recipe that matches the name inputted by the user
                my_recipe = data[index]
                # this then returns that recipe so that the user can see how to make the meal
                return my_recipe

# this is for testing purposes only
def get_app():
    return application


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
