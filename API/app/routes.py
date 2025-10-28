from flask import jsonify, request, abort
from . import app, db_manager
from os import path, makedirs, remove

@app.route("/games", methods=["GET"])
def get_all_games():
    #get all rows in game table joined with data from meta table
    query_result = db_manager.select_all_games()
    if not query_result:
        return jsonify("Query failed"), 400
    #convert query result to a list of dictionaries using list comprehension
    games = [dict(row) for row in query_result]
    return jsonify(games), 200

@app.route("/games/<int:id>", methods=["GET"])
def get_game(id):
    #selects game from the game table using the rows id
    query_result = db_manager.select_game(id)
    if not query_result:
        return jsonify("Query failed"), 404
    game = dict(query_result)
    return jsonify(game), 200

@app.route("/games", methods=["POST"])
def create_game():
    #Get the data out of the json request as a Dict
    data = request.get_json()
    #get the metadata object out of the json request
    meta = data.get("meta")
    query_result = db_manager.insert_metadata(meta["title"], meta["description"],
                                              meta["file_path"],meta["file_size"])
    # if the result of the query in insert_metadata method returns none than we return a 400 bad request
    if not query_result:
        return jsonify("Failed to create game meta problem"), 400
    #get game data out of request (this should just be an image path at the moment)
    game = data.get("game")
    query_result = db_manager.insert_game(game["image_url"],query_result)
    #If the query in insert_ game method returns False then we return a 400 bad request
    if not query_result:
        return jsonify("Failed to create game, game data problem"), 400
    #Return a 201 created response since the rows in the database tables should have been created properly
    return jsonify("Game created"), 201

@app.route("/games/<int:metaid>", methods=["DELETE"])
def delete_game(metaid):
    #Delete game will only delete the entry on the metadata table since the foreign key on the game table is set to cascade delete
    query_result = db_manager.delete_data(metaid)
    if not query_result:
        return jsonify("Query failed"), 404
    return jsonify("Game deleted"), 200

@app.route("/games", methods=["PUT"])
def update_game():
    data = request.get_json()
    meta = data.get("meta")
    game = data.get("game")
    # Attempt to update the metadata table, save the number of rows affected to the variable meta_update
    meta_update = db_manager.update_metadata_full(meta)

    if not meta_update:
        return jsonify("Query failed"), 404

    # Attempt to update the game data table, save the number of rows affected to the variable game_update
    game_update = db_manager.update_game(game)

    if not game_update:
        return jsonify("Query failed"), 404

    return jsonify("Game updated"), 200

# Only used for testing will delete database!
@app.route("/reset", methods=["DELETE"])
def reset_database():
    if not app.debug:
        abort(404)
    #build the path to the database file
    db_dir = path.join(path.dirname(__file__), 'data')
    db_path = path.join(db_dir, 'multimedia.db')

    try:
    # remove the database file
        remove(db_path)
        return jsonify("Database reset"), 200
    except OSError as e:
        return jsonify("Database reset failed"), 200

