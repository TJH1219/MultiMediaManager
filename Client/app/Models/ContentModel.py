from PySide6.QtCore import QObject


class ContentModel(QObject):
    def __init__(self, id: int, title: str, description: str, file_path: str, file_size: int, created_at: str,
                 updated_at: str, /):
        super().__init__()
        self.id = id
        self.title = title
        self.description = description
        self.file_path = file_path
        self.file_size = file_size
        self.created_at = created_at
        self.updated_at = updated_at