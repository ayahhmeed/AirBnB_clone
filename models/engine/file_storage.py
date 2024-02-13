#!/usr/bin/python3
"""
Here this module to create FileStorage
that contain serilization and deserilization
"""

import json
from os.path import exists


class FileStorage:
    """
    This class to serialize instances to a json file and to deserialize
    """
    __file_path = "file.json"
    __objects = {}

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
        if exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_objects = json.load(f)

                for key, obj_dict in json_objects.items():
                    self.__objects[key] = BaseModel(**obj_dict)
