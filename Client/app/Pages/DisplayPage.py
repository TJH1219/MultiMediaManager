from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from Client.app.Models.ContentModel import ContentModel


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
        #Create the widgets used to display data onto the page
        self.title = QLabel("Display Page")
        self.description = QLabel("This is the display page")
        self.file_size = QLabel("")
        self.updated_at = QLabel("")
        layout.addWidget(self.title)
        layout.addWidget(self.description)
        layout.addWidget(self.file_size)
        layout.addWidget(self.updated_at)

        #Create widgets used to navigate
        self.NavigateButton = QPushButton("Go Back")
        self.NavigateButton.clicked.connect(lambda: self.navigate_to.emit("dashboard"))
        layout.addWidget(self.NavigateButton)

    #Display the data in the model passed to the function onto the page
    def set_content(self, model:ContentModel):
        self.current_item_id = model.id
        self.title.setText(model.title)
        self.description.setText(model.description)
        self.file_size.setText(f"Size{model.file_size}")
        self.updated_at.setText(f"Last Modified{model.updated_at}")

    def show(self) -> None:
        super().show()
        self.title.setFocus()

    def hide(self):
        super().hide()

    def cleanup(self):
        pass