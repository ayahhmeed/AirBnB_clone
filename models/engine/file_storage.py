#!/usr/bin/python3
"""
Here this module to create FileStorage
that contain serilization and deserilization
"""


import json
from pathlib import Path


class FileStorage:

    def __init__(self):
        """
        Here to initialize the User class
        """
        self.__file_path = "users.json"
        self.__objects = {}
        self.reload()

    def all(self):
        """
        Here to return the dicitonary of the object
        """
        return self.__objects

    def new(self, obj):
        """
        Here to set an object with key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Here to serialize object to json file
        """
        json_objects = {}
        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Here to deserialize json to the file
        """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.base_model import BaseModel

        if path(self.__file_path).exists():
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_objects = json.load(f)

                for key, obj_dict in json_objects.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        self.__objects[key] = User(**obj_dict)
                    for key, obj_dict in json_objects.items():
                        if obj_dict["__class__"] == "Place":
                            self.__objects[key] = Place(**obj_dict)
                        elif obj_dict["__class__"] == "State":
                            self.__objects[key] = State(**obj_dict)
                        elif obj_dict["__class__"] == "City":
                            self.__objects[key] = City(**obj_dict)
                        elif obj_dict["__class__"] == "Amenity":
                            self.__objects[key] = Amenity(**obj_dict)
                        elif obj_dict["__class__"] == "Review":
                            self.__objects[key] = Review(**obj_dict)
