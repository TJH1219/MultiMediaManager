from typing import List

from Client.app.Models.GameModel import GameModel


def build_game_models(data:List[dict]):
    games = []
    for item in data:
        games.append(GameModel(**item))
    return games