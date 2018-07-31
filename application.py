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


couple = api.model('couple', {
    'person_a': fields.Nested(person),
    'person_b': fields.Nested(person),

})

# might not be able to do .colour
def match(person_a, person_b):
    points = 0

    if person_a.colour == person_b['colour']:
        points += 10

    if person_a.hobby == person_b.hobby:
        points += 10

    if person_a.food == person_b.food:
        points += 10

    if person_a.sport == person_b.sport:
        points += 10

    if person_a.animal == person_b.animal:
        points += 10

    if person_a.artist == person_b.artist:
        points += 10

    if person_a.genre == person_b.genre:
        points += 10

    if person_a.season == person_b.season:
        points += 10

    if person_a.vacation == person_b.vacation:
        points += 10

    if person_a.social_media == person_b.social_media:
        points += 10

    return "You are " + str(points) + "% compatible"


# creating a person so that we can use it in the match api

class Person:
    def __init__(self, colour, hobby, food, sport, animal, artist, genre, season, vacation, social_media):
        self.colour = colour
        self.hobby = hobby
        self.food = food
        self.sport = sport
        self.animal = animal
        self.artist = artist
        self.genre = genre
        self.season = season
        self.vacation = vacation
        self.social_media = social_media

    def create_person(self):
        person = api.model('person', {
            'colour': self.colour.String(required=True, description='favourite colour'),
            'hobby': self.hobby.String(required=True, description='favourite hobby'),
            'food': self.food.String(required=True, description='favourite food'),
            'sport': self.sport.String(required=True, description='favourite sport'),
            'animal': self.animal.String(required=True, description='favourite animal'),
            'artist': self.artist.String(required=True, description='favourite artist'),
            'genre': self.genre.String(required=True, description='favourite genre'),
            'season': self.season.String(required=True, description='favourite season'),
            'vacation': self.vacation.String(required=True, description='favourite vacation'),
            'social_media': self.social_media.String(required=True, description='social_media'),
        })
        return person



'''
TODO - create Person object from Model
'''


@api.route("/api/person")
class PersonRoute(Resource):

    # @api.response(201, 'Rumor successfully created.')
    @api.expect(couple)
    @api.marshal_with()
    def post(self):
        person_a = Person('red', 'guitar', 'salad', 'football', 'dog', 'beyonce', 'sci-fi', 'winter', 'skiing',
                          'snapchat')
        return person_a.create_person()


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
