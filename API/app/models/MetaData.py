from datetime import datetime

class MetaData:
    def __init__(self, title, description, image, **kwargs):
        self.title = title
        self.description = description
        self.image = image
        self.created_on = kwargs.get('created_at', datetime.now())
        self.file_path = kwargs.get("file_path", None)
        self.tags = kwargs.get("tags", [])

    def __to_dict__(self):
        #convert object to dictionary for JSON serialization
        return{
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "created_on": self.created_on,
            "file_path": self.file_path
        }

    def __str__(self):
        return f"MetaData('{self.title}', '{self.description}', '{self.image}')"