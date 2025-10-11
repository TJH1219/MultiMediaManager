from flask import jsonify
from __init__ import app

app.route("/")
def hello():
    return jsonify({"message": "Hello World!"})