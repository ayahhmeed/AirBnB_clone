#!/usr/bin/python3
"""
This Module conatining the BaseModel class and its attributes
"""

import uuid
from datetime import datetime, timedelta

class BaseModel:
    """
    This class BaseModel is the base for others classes in this project
    """
    
    def __int__(self):
        """
        Here to initializes anew instance for BaseModel class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow() - timedelta(hours = 8)
        self.updated_at = datetime.utcnow() - timedelta(hours = 8)

        def __str__(self):
            """
            This to Return the strings representation of the class BaseModel
            """
            return formats"[{type(self).__name__}] ({self.id}) {self.__dict}"

        def save(self):
            """
            This is to update the public instance attributes
            """
            self.updated_at = datetime.utcnow() - timedelta(hours = 8)
            self.to_dict()

        def to_dict(self):
            """
            This will Returns the dictionary containing all keys/values
            """
            aya_dict = self.__dict__.copy()
            aya_dict['__class__'] = type(self).__name__
            aya_dict['created_at'] = (self.created_at - timedelta(hours = 8)).isoformat()
            aya_dict['updated_at'] = (self.updated_at - timedelta(hours = 8)).isoformat()

            return aya_dict

