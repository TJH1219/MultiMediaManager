from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class DisplayPage(QWidget):

    #Sngianl emitted when this page wants to navigate to another page
    navigate_to = Signal(str)

    def __init__(self):
        super().__init__()
        self.current_item_id = None
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        self.temp_label = QLabel("Display Page")
        layout.addWidget(self.temp_label)

        self.NavigateButton = QPushButton("Go Back")
        self.NavigateButton.clicked.connect(lambda: self.navigate_to.emit("main"))
        layout.addWidget(self.NavigateButton)

    def set_content(self, item_id:str):

        self.current_item_id = item_id
        self.temp_label.setText(f"Display Page: {item_id}")

    def show(self) -> None:
        super().show()
        self.temp_label.setFocus()

    def hide(self):
        super().hide()

    def cleanup(self):
        pass