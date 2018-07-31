
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



def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
