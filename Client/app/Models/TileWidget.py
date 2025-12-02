"""
Model for the tile widget that will be displayed on the dashboard
"""
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, Qt, QMouseEvent
from PySide6.QtWidgets import QFrame, QWidget, QSizePolicy, QVBoxLayout, QLabel


class TileWidget(QFrame):

    clicked = Signal(str)

    def __init__(self, item_id:int, thumbnail_path:str, parent:QWidget | None = None) -> None:
        super().__init__(parent)
        self.item_id = item_id

        self.setObjectName("tileWidget")
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        self._thumbnail_label = QLabel(self)
        self._thumbnail_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._thumbnail_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._thumbnail_label.setMinimumSize(100, 100)

        pixmap = QPixmap(thumbnail_path)
        if not pixmap.isNull():
            self._thumbnail_label.setPixmap(
                pixmap.scaled(
                    256,
                    256,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        else:
            self._thumbnail_label.setText("No Thumbnail")

        layout.addWidget(self._thumbnail_label)

        self.setStyleSheet(
            """
                QFrame#tileWidget {
                    border: 1px solid #555;
                    border-radius: 4px;
                    background-color: #222;
                }
                QFrame#tileWidget:hover {
                    border: 2px solid #6a9ff8;
                }
            """
        )

    def mousePressEvent(self, event:QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.item_id)
        super().mousePressEvent(event)

    def enterEvent(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        super().enterEvent(event)