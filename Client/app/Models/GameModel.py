from Client.app.Models.ContentModel import ContentModel


class GameModel(ContentModel):
    def __init__(self, id:int,  title:str, description:str, file_path:str, file_size:int,
                 created_at:str, updated_at:str, image_url:str):
        super().__init__(id, title, description,file_path,file_size,created_at,updated_at)
        self.image_url = image_url