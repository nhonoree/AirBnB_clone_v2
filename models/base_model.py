# models/base_model.py
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all models."""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Save object to storage."""
        self.updated_at = datetime.now()
        # This is just a placeholder to simulate saving to FileStorage
        storage.new(self)
        storage.save()

    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
