import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ This class serializes instances to a JSON file and deserializes JSON
    file to instances """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Return the dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ Add a new object to the storage """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """ Save the objects to the JSON file """
        with open(self.__file_path, 'w') as f:
            json.dump(
                {key: obj.to_dict() for key, obj in self.__objects.items()}, f
            )

    def reload(self):
        """ Reload the objects from the JSON file """
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "State":
                        self.__objects[key] = State(**value)
                    elif class_name == "City":
                        self.__objects[key] = City(**value)
                    elif class_name == "User":
                        self.__objects[key] = User(**value)
                    elif class_name == "Place":
                        self.__objects[key] = Place(**value)
                    elif class_name == "Amenity":
                        self.__objects[key] = Amenity(**value)
                    elif class_name == "Review":
                        self.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete an object from the storage """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()
