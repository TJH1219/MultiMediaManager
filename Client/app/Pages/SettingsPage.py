from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QPushButton


class SettingsPage(QWidget):

    #Sngianl emitted when this page wants to navigate to another page
    navigate_to = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        self.temp_label = QLabel("Settings Page")
        layout.addWidget(self.temp_label)

        self.NavigateButton = QPushButton("Go Back")
        self.NavigateButton.clicked.connect(lambda: self.navigate_to.emit("main"))
        layout.addWidget(self.NavigateButton)

    def show(self) -> None:
        super().show()
        self.temp_label.setFocus()

    def hide(self):
        super().hide()

    def cleanup(self):
        pass