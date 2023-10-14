#!/usr/bin/python3
"""This module defines the tests for the BaseModel class"""

import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models import storage # import storage variable

class TestBaseModel(unittest.TestCase):
    """This class tests the BaseModel class"""

    def setUp(self):
        """Sets up an instance of BaseModel for testing"""
        self.base = BaseModel()

    def tearDown(self):
        """Tears down the instance of BaseModel after testing"""
        del self.base
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Tests that an instance can be initialized with default or custom values"""
        base1 = BaseModel()
        base2 = BaseModel(id="123", created_at="2020-11-17T04:21:33.000000")
        base3 = BaseModel(**self.base.to_dict())
        
        # check default values
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base1.created_at, datetime)
        
        # check custom values
        self.assertEqual(base2.id, "123")
        self.assertEqual(base2.created_at, datetime(2020, 11, 17, 4, 21, 33))

        # check dictionary values
        self.assertEqual(base3.id, self.base.id)
        self.assertEqual(base3.created_at, self.base.created_at)

    def test_str(self):
        """Tests that the str method returns a string representation of the instance"""
        base_str = self.base.__str__()
        self.assertIsInstance(base_str, str)
        self.assertEqual(base_str, "[{}] ({}) {}".format(self.base.__class__.__name__, self.base.id, self.base.__dict__))

    def test_save(self):
        """Tests that the save method updates the updated_at attribute with the current datetime and saves it to storage"""
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)
        key = self.base.__class__.__name__ + "." + self.base.id
        self.assertIn(key, storage.all()) # check that the object is in storage
        self.assertEqual(self.base, storage.all()[key]) # check that the object is the same as in storage

    def test_to_dict(self):
        """Tests that the to_dict method returns a dictionary representation of the instance with correct keys and values"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(base_dict["created_at"], self.base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], self.base.updated_at.isoformat())
        key = self.base.__class__.__name__ + "." + self.base.id
        storage_dict = storage.all()[key].to_dict() # get the dictionary from storage
        self.assertEqual(base_dict, storage_dict) # check that the dictionaries are equal
