from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout


class DashBoard(QWidget):
    #Signal emitted when this page wants to navigate to another page
    navigate_to = Signal(str)
    display_item_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
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

        items = [
            ("Item1", "item 1"),
            ("Item2", "item 2"),
            ("Item3", "item 3"),
            ("Item4", "item 4"),
        ]

        rows = 2
        cols = 2
        for index, (label, item_id) in enumerate(items):
            row = index // cols
            col = index % cols
            button = QPushButton(label)

            # emit which item was clicked
            button.clicked.connect(
                lambda _, iid=item_id: self.display_item_selected.emit(iid)
            )

            grid_layout.addWidget(button, row, col)

    def create_grid(self):
        pass
    #Todo implement grid method

    def show(self) -> None:
        super().show()
        self.temp_label.setFocus()

    def hide(self) -> None:
        super().hide()

    def cleanup(self):
        pass