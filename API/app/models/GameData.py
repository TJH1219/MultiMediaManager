import MetaData

class GameData(MetaData):
    def __init__(self, title, description, image):
        super().__init__(title, description, image)