import json
import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

class Team(ndb.Model):
    """Team"""
    name = ndb.StringProperty(required=True)


class Game(ndb.Model):
    """Game"""
    game_id = ndb.StringProperty(required=True)
    owner = ndb.UserProperty(required=True)
    blue_team = ndb.KeyProperty()
    purple_team = ndb.KeyProperty()

class CreateHandler(webapp2.RequestHandler):
    def post(self):
        if not users.get_current_user():
            return webapp2.redirect(users.create_login_url(self.request.uri))

        data = json.loads(self.request.body)

        game_id = "foobar"

        blue_team = Team(parent=ndb.Key('Game', game_id))
        blue_team.name = data['blue_team']['name']
        blue_team.put()
        purple_team = Team(parent=ndb.Key('Game', game_id))
        purple_team.name = data['purple_team']['name']
        purple_team.put()

        game = Game(game_id=game_id, blue_team=blue_team.key, purple_team=purple_team.key)
        game.owner = users.get_current_user()
        game.put()

        game_dict = {
                'game_id': game_id,
                'blue_team': blue_team.to_dict(),
                'purple_team': purple_team.to_dict(),
                'owner': game.owner.email(),
                };

        self.response.out.write(json.dumps(game_dict))

class GetHandler(webapp2.RequestHandler):
    def get(self, game_id):
        game = Game.get(db.Key.from_path('Game', game_id));
        self.response.out.write(json.dumps(game.to_dict()));

application = webapp2.WSGIApplication([
        ('/game/create.json', CreateHandler),
        ('/game/(.*).json', GetHandler),
        ], debug=True)
