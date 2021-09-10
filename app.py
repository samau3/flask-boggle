from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game


    return {"gameId": game_id, "board": game.board} #currently returning a dictionary; Flask turns into JSON

@app.post("/api/score-word")
def score_word():
    """Scores word, returns validity of the word in the response body """

    id = request.json["gameId"]
    word = request.json["word"]
    # breakpoint()
    game = games[id]
    in_word_list = game.is_word_in_word_list(word)
    on_board = game.check_word_on_board(word)

    # breakpoint()

    if (not in_word_list):
        return {"result": "not-word"}
    elif (not on_board):
        return {"result": "not-on-board"}
    else:
        return {"result": "ok"}