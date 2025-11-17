from Client.app.models.ContentModel import ContentModel


class GameModel(ContentModel):
    def __init__(self, title:str, description:str, file_path:str, file_size:int,
                 created_at:str, updated_at:str, image_url:str):
        super().__init__(title, description,file_path,file_size,created_at,updated_at)
        self.image_url = image_url