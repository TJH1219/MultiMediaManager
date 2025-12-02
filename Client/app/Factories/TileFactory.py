"""
    This factory is used to create the buttons or tiles seen on the content grid in the main display.
    At the moment it will be using a hard-coded dictionary, but later on it will be given data parsed out of a
    JSON file
"""
from PySide6.QtWidgets import QWidget

from Client.app.Models.TileWidget import TileWidget


def create_tiles(data: list, parent:QWidget = None) -> list:
    tile_list = []
    for item in data:
        tile_list.append(TileWidget(item.id, item.image_url, parent))
    return tile_list
