#!/usr/bin/python3
"""This module defines the tests for the FileStorage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User # import User class

class TestFileStorage(unittest.TestCase):
    """This class tests the FileStorage class"""

    def setUp(self):
        """Sets up an instance of FileStorage and a BaseModel and a User for testing"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.user = User() # create a User instance

    def tearDown(self):
        """Tears down the instance of FileStorage and the BaseModel and the User after testing"""
        del self.storage
        del self.model
        del self.user
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Tests that the all method returns the dictionary __objects"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """Tests that the new method sets in __objects the obj with key <obj class name>.id"""
        key1 = self.model.__class__.__name__ + "." + self.model.id # create the key for the BaseModel object
        key2 = self.user.__class__.__name__ + "." + self.user.id # create the key for the User object
        self.storage.new(self.model)
        self.storage.new(self.user) # add the User object to storage
        self.assertIn(key1, self.storage.all())
        self.assertIn(key2, self.storage.all()) # check that both objects are in storage
        self.assertEqual(self.model, self.storage.all()[key1])
        self.assertEqual(self.user, self.storage.all()[key2]) # check that both objects are equal to those in storage

    def test_save(self):
        """Tests that the save method serializes __objects to the JSON file (path: __file_path)"""
        key1 = self.model.__class__.__name__ + "." + self.model.id # create the key for the BaseModel object
        key2 = self.user.__class__.__name__ + "." + self.user.id # create the key for the User object
        self.storage.new(self.model)
        self.storage.new(self.user) # add both objects to storage
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            json_dict = json.load(f) # use json module to load dictionary from file
            self.assertIn(key1, json_dict)
            self.assertIn(key2, json_dict) # check that both keys are in the dictionary
            self.assertEqual(self.model.to_dict(), json_dict[key1])
            self.assertEqual(self.user.to_dict(), json_dict[key2]) # check that both objects are equal to those in the dictionary

    def test_reload(self):
        """Tests that the reload method deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""
        key1 = self.model.__class__.__name__ + "." + self.model.id # create the key for the BaseModel object
        key2 = self.user.__class__.__name__ + "." + self.user.id # create the key for the User object
        self.storage.new(self.model)
        self.storage.new(self.user) # add both objects to storage
        self.storage.save()
        del self.storage._FileStorage__objects[key1]
        del self.storage._FileStorage__objects[key2] # delete both objects from storage
        self.assertNotIn(key1, self.storage.all())
        self.assertNotIn(key2, self.storage.all()) # check that both objects are not in storage
        self.storage.reload()
        self.assertIn(key1, self.storage.all())
        self.assertIn(key2, self.storage.all()) # check that both objects are in storage after reloading
        self.assertEqual(self.model.to_dict(), self.storage.all()[key1].to_dict())
