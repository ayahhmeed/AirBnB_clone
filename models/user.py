#!/usr/bin/python3
"""
This the user class that containd its information
"""


class User:
    """
    This the user class that inherits from BaseModel
    """

    def __init__(self, first_name, last_name, email, password):
        """
        class initialize the user instances
        """
        from models.base_model import BaseModel
        self.base_model_instance = BaseModel()

        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
        self.id = None
        self.created_at = None
        self.updated_at = None
