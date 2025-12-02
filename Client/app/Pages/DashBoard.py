import datetime
import json
from functools import partial

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout
from Client.app.Factories import TileFactory, ModelBuilder
from Client.app.Managers.ConfigManager import ConfigManager
from Client.app.Managers.RequestManager import set_request
from Client.app.Models.ContentModel import ContentModel
from Client.app.Models.GameModel import GameModel


class DashBoard(QWidget):
    #Signal emitted when this page wants to navigate to another page
    navigate_to = Signal(str)
    display_item_selected = Signal(object)

    def __init__(self, parent=None, config_manager=None):
        super().__init__(parent)
        self.config_manager = config_manager
        self.items = None
        games = set_request(self.config_manager.get("api_url"),"/games")
        self.items = ModelBuilder.build_game_models(json.loads(games.text))
        self._setup_ui()


    def _setup_ui(self):
        root_layout = QVBoxLayout(self)
        root_layout.setContentsMargins(20, 20, 20, 20)

        self.temp_label = QLabel("Main Page")
        root_layout.addWidget(self.temp_label)

        self.setting_button = QPushButton("Settings")
        root_layout.addWidget(self.setting_button)
        self.setting_button.clicked.connect(lambda: self.navigate_to.emit("settings"))

        grid_layout = QGridLayout()
        root_layout.addLayout(grid_layout)

        item = [
            GameModel(1,'MegaBonk', 'fun game', "game/game/game",
                      1024, str(datetime.datetime.now()), str(datetime.datetime.now()),
                      r"C:\Users\thadd\PycharmProjects\MultiMediaManager\Client\app\Static\megabonkthumbnail.jpg"),
            GameModel(2,'This War Of Mine', 'fun game', "game/game/game",
                       1024, str(datetime.datetime.now()), str(datetime.datetime.now()),
                      r"C:\Users\thadd\PycharmProjects\MultiMediaManager\Client\app\Static\thiswarofmine.jpg"),
            GameModel(3, 'Pavlov', 'fun game', "game/game/game",
                       1024, str(datetime.datetime.now()), str(datetime.datetime.now()),
                      r"C:\Users\thadd\PycharmProjects\MultiMediaManager\Client\app\Static\pavlov.jpg")
        ]
        tilemap = TileFactory.create_tiles(self.items)
        rows = 2
        cols = 3
        iter:int = 0
        for index in tilemap:
            row = iter // cols
            col = iter % cols
            button = index

            # emit which item was clicked
            button.clicked.connect(partial(self._on_item_clicked, model=self.items[iter]))

            grid_layout.addWidget(button, row, col)
            iter += 1

    def _on_item_clicked(self, checked, model):
        self.display_item_selected.emit(model)

    def create_grid(self):
        pass

    def show(self) -> None:
        super().show()
        self.temp_label.setFocus()

    def hide(self) -> None:
        super().hide()

    def cleanup(self):
        pass