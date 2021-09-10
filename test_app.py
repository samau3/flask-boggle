from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            ...
            # test that you're getting a template
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<table class="board">', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            response = client.post("/api/new-game")
            game_data = response.get_json() #, data={"gameId": game_id, "board": game.board}
            self.assertEqual(response.status_code, 200)

            self.assertIn(game_data["gameId"], games)
            self.assertIs(type(game_data["gameId"]), str)
            self.assertIs(type(game_data["board"]), list)
            self.assertIs(len(game_data["board"]), 5)
            
    def test_score_word(self):
        """Test scoring word"""

        with self.client as client: # will need to create a fixed board so it can actually be tested
            ...
            new_game = client.post("/api/new-game")

            breakpoint() #can't put breakpoint as last line of code in function

            # new_data = new_game
            # print(new_game)
            game_id = new_game.get_json()["gameId"]

            breakpoint()
            # response = client.post("/api/score-word", json={"gameId": games[], "word": "DOG"})
            return False
            # breakpoint()
            # response = client.post("/api/score-word", data={"gameId": games["id"], "word": "DOG"})
            # game_data = response.get_json()