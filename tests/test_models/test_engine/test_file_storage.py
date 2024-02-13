#!/usr/bin/python3
"""
Here to implement testing
"""

import unittest
import os
import sys

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

parent_dir = os.path.abspath(os.path.dirname(__file__))
parent_parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(parent_parent_dir)


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Here to set up a test for the FileStorage
        """
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.name = "My_First_Model"
        self.base_model.my_number = 89

    def test_save_model(self):
        """
        Here to clean all the created files
        """
        self.base_model.save()
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_get_model(self):
        """
        Here to test all the method included
        """
        self.base_model.save()
        base_model_from_storage = self.storage.get(
                BaseModel, self.base_model.id)
        self.assertEqual(base_model_from_storage.name, "My_First_Model")
        self.assertEqual(base_model_from_storage.my_number, 89)

    def test_get_all_models(self):
        """
        Here for testing new methods
        """
        self.base_model.save()
        base_models_from_storage = self.storage.all(BaseModel)
        self.assertIsNotNone(base_models_from_storage)
        self.assertEqual(len(base_models_from_storage), 1)
        self.assertEqual(base_models_from_storage[0].name, "My_First_Model")
        self.assertEqual(base_models_from_storage[0].my_number, 89)

    def test_delete_model(self):
        """
        Here to test the save and reload methods
        """
        self.base_model.save()
        self.storage.delete(self.base_model)
        base_model_from_storage = self.storage.get(
                BaseModel, self.base_model.id)
        self.assertIsNone(base_model_from_storage)


if __name__ == "__main__":
    unittest.main()
