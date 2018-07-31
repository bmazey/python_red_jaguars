from flask import Flask
from flask_restplus import Resource, Api
from flask_restplus import fields


# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
application = Flask(__name__)
api = Api(application)

'''
TODO - create marshaller!
'''

person = api.model('person', {
    'colour': fields.String(required=True, description='favourite colour'),
    'hobby': fields.String(required=True, description='favourite hobby'),
    'food': fields.String(required=True, description='favourite food'),
    'sport': fields.String(required=True, description='favourite sport'),
    'animal': fields.String(required=True, description='favourite animal'),
    'artist': fields.String(required=True, description='favourite artist'),
    'genre': fields.String(required=True, description='favourite genre'),
    'season': fields.String(required=True, description='favourite season'),
    'vacation': fields.String(required=True, description='favourite vacation'),
    'social_media': fields.String(required=True, description='social_media'),
})

# couple = api.model('couple', {
#     'person_a': fields.Nested(person),
#     'person_b': fields.Nested(person),
#
# })


def match(person_a, person_b):
    points = 0
    for property in person:
        if (person_a.property == person_b.property):
                points += 1

    return "You are " + str(points*10) + "% compatible"
'''
TODO - create Person object from Model
'''


@api.route("/api/person")
class Person(Resource):
    # @api.response(201, 'Rumor successfully created.')
    @api.expect(person)
    @api.marshal_with(person)
    def post(self):
        return


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
