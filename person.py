
from flask import Flask
from flask_restplus import Resource, Api


# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
application = Flask(__name__)
api = Api(application)


@api.route("/api/person")                   # Create a URL route to this resource
class Person(Resource):            # Create a RESTful resource
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

        # method for printing the instance
    def print_instance(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(self.colour, self.hobby, self.food, self.sport, self.animal, self.artist, self.genre, self.season, self.vacation, self.social_media)
# This is the instance example
person_a = Person('red', 'reading', 'pizza', 'rugby', 'cat', 'selena gomez', 'dramatic', 'summer', 'sea_side', 'instagram')

def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
