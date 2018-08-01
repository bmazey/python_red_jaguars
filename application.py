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


@api.route("/api/recipe/<string:name>")
class Recipe(Resource):
    def get(self, name):
        for index in range(0,9):
            if data[index].get('name') == name:
                return data[index].get('ingredients')


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
