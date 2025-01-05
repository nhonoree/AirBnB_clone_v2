#!/usr/bin/python3
"""
Module: file_storage.py
Defines the FileStorage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of objects.
        If cls is specified, only returns objects of type cls.
        """
        if cls:
            return {key: value for key, value in self.__objects.items() if isinstance(value, cls)}
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it exists.
        """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)
