#!/usr/bin/python3
"""
Here to implement testing
"""

import unittest
import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
parent_parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(parent_parent_dir)

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """
        Here to set up a test for the FileStorage
        """
        self.storage = FileStorage

    def tearDown(self):
        """
        Here to clean all the created files
        """
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """
        Here to test all the method included
        """
        objects = self.storage.all()
        self.assertEqual(len(objects), 0)

        wmodel = BaseModel()
        wmodel.save()

        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn("BaseModel." + wmodel.id, objects)

    def test_new(self):
        """
        Here for testing new methods
        """
        wmodel = BaseModel()

        self.storage.new(wmodel)

        self.asserIn("BaseModel." + wmodel.id, self.storage._FileStorage__objects)

    def test_save_reload(self):
        """
        Here to test the save and reload methods
        """
        wmodel = BaseModel()
        wmodel.save()
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn("BaseModel." + wmodel.id, objects)

    def test_save(self):
        """
        Here to test the save method
        """
        wmodel = BaseModel()
        wmodel.save()

        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """
        Here testing for reload method
        """
        wmodel = BaseModel()
        wmodel.save()
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn("BaseModel." + wmodel.id, objects)


if __name__ == "__main__":
    unittest.main()




