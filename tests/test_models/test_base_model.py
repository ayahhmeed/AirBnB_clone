#!/usr/bin/python3
"""
This is the unit tests for the class BaseModel
"""

import unittest
import sys
import os
from datetime import datetime, timezone
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Here is test cases for the BaseModel class
    """

    def test_initialization(self):
        """
        Here to test the initialization of BaseModel class
        """
        the_model = BaseModel()
        self.assertIsInstance(the_model.id, str)
        self.assertIsInstance(the_model.created_at, datetime)
        self.assertIsInstance(the_model.updated_at, datetime)

    def test_string(self):
        """
        Here to test the string representaion of BaseModel intance
        """
        the_model = BaseModel()
        self.assertEqual(str(the_model), "[BaseModel] ({}) {}".format(
            the_model.id, the_model.__dict__))

    def test_save(self):
        """
        Here to test the save method of BaseModel instance
        """
        the_model = BaseModel()
        the_old_updated = the_model.updated_at
        the_model.save()
        self.assertNotEqual(the_old_updated, the_model.updated_at)

    def test_dict(self):
        """
        Here is the test of to_dict method of BaseModel
        """
        the_model = BaseModel()
        the_model_json = the_model.to_dict()
        self.assertIsInstance(the_model_json, dict)
        self.assertIn('__class__', the_model_json)
        self.assertEqual(the_model_json['__class__'], 'BaseModel')
        self.assertIn('updated_at', the_model_json)
        self.assertIsInstance(the_model_json['created_at'], str)
        self.assertIsInstance(the_model_json['updated_at'], str)
        new_model = BaseModel(**the_model_json)
        self.assertEqual(the_model.id, new_model.id)
        self.assertEqual(the_model.created_at, new_model.created_at)
        self.assertEqual(the_model.updated_at, new_model.updated_at)

    def test_save_and_reload(self):
        the_model = BaseModel()
        the_model.name = "The_Model"
        the_model.my_number = 123
        the_model.save()
        reloaded_model = BaseModel.find(the_model.id)
        self.assertEqual(reloaded_model.id, the_model.id)
        self.assertEqual(
                reloaded_model.created_at,
                the_model.created_at)
        self.assertEqual(
                reloaded_model.updated_at,
                the_model.updated_at)
        self.assertEqual(reloaded_model.name, the_model.name)
        self.assertEqual(reloaded_model.my_number, the_model.my_number)

    if __name__ == "__main__":
        unittest.main()
