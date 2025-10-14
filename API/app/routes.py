from flask import jsonify
from __init__ import app

app.route("/")
def hello():
    return jsonify({"message": "Hello World!"})

app.route("/games", methods=["GET"])
def get_games():
    pass

app.route("/games/<id>", methods=["GET"])
def get_game(title):
    pass

app.route("/photos", methods=["GET"])
def get_photos():
    pass

app.route("/photos/<id>", methods=["GET"])
def get_photo(title):
    pass

app.route("/videos", methods=["GET"])
def get_videos():
    pass

app.route("/videos/<id>", methods=["GET"])
def get_video(title):
    pass