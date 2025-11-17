class ContentModel:
    def __init__(self, title:str, description:str, file_path:str, file_size:int, created_at:str, updated_at:str):
        self.title = title
        self.description = description
        self.file_path = file_path
        self.file_size = file_size
        self.created_at = created_at
        self.updated_at = updated_at