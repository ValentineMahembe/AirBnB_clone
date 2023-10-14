#!/usr/bin/python3
"""This module defines the tests for the FileStorage class"""

import unittest
import os
import json # import json module
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage # import storage variable

class TestFileStorage(unittest.TestCase):
    """This class tests the FileStorage class"""

    def setUp(self):
        """Sets up an instance of FileStorage and a BaseModel for testing"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """Tears down the instance of FileStorage and the BaseModel after testing"""
        del self.storage
        del self.model
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Tests that the all method returns the dictionary __objects"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """Tests that the new method sets in __objects the obj with key <obj class name>.id"""
        key = self.model.__class__.__name__ + "." + self.model.id
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.model, self.storage.all()[key])

    def test_save(self):
        """Tests that the save method serializes __objects to the JSON file (path: __file_path)"""
        key = self.model.__class__.__name__ + "." + self.model.id
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            json_dict = json.load(f) # use json module to load dictionary from file
            self.assertIn(key, json_dict)
            self.assertEqual(self.model.to_dict(), json_dict[key])

    def test_reload(self):
        """Tests that the reload method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)"""
        key = self.model.__class__.__name__ + "." + self.model.id
        self.storage.new(self.model)
        self.storage.save()
        del self.storage._FileStorage__objects[key]
        self.assertNotIn(key, self.storage.all())
        self.storage.reload()
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.model.to_dict(), self.storage.all()[key].to_dict())
