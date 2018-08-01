import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy


# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

'''
TODO - create marshaller!
'''
# this the the recipe api that has a name and content property
recipe = api.model('recipe', {
    'name': fields.String(required=True, description='name of recipe'),
    'content': fields.String(required=True, description='how to make it'),

})

recipe_id = api.model('recipe_id', {
    'id': fields.String(readOnly=True, description='unique identifier of a recipe'),
    'name': fields.String(required=True, description='name of recipe'),
    'content': fields.String(required=True, description='how to make it'),
})

# recipe

class Recipe(db.Model):
    id = db.Column(db.Text(80), primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Recipe %r>' % self.content


def create_recipe(data):
    id = str(uuid.uuid4())
    name = data.get('name')
    content = data.get('content')
    recipe = Recipe(id=id, name=name, content=content)
    db.session.add(recipe)
    db.session.commit()
    return recipe


@api.route("/api/recipe")
class RecipeRoute(Resource):
    # @api.response(201, 'Rumor successfully created.')
    @api.expect(recipe)
    @api.marshal_with(recipe)
    def post(self):
        return



def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
