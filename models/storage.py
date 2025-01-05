# models/storage.py
import json

class FileStorage:
    """Simulates storage of objects."""
    __objects = {}

    def all(self):
        """Returns all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to storage."""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Saves objects to a file (simulated)."""
        with open("file.json", "w") as file:
            json.dump({key: obj.__dict__ for key, obj in FileStorage.__objects.items()}, file)

    def reload(self):
        """Reloads objects from the file (simulated)."""
        try:
            with open("file.json", "r") as file:
                objects = json.load(file)
                for key, value in objects.items():
                    class_name = value["__class__"]
                    class_ = globals()[class_name]
                    FileStorage.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass

# Instance of FileStorage
storage = FileStorage()
