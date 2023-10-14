#!/usr/bin/python3
"""This module defines the tests for the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """This class tests the BaseModel class"""

    def setUp(self):
        """Sets up an instance of BaseModel for testing"""
        self.base = BaseModel()

    def tearDown(self):
        """Tears down the instance of BaseModel after testing"""
        del self.base

    def test_id(self):
        """Tests that the id attribute is a string and unique"""
        self.assertIsInstance(self.base.id, str)
        base2 = BaseModel()
        self.assertNotEqual(self.base.id, base2.id)

    def test_created_at(self):
        """Tests that the created_at attribute is a datetime object and assigned at initialization"""
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertLessEqual(self.base.created_at, datetime.now())

    def test_updated_at(self):
        """Tests that the updated_at attribute is a datetime object and assigned at initialization and updated by save method"""
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertEqual(self.base.updated_at, self.base.created_at)
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_str(self):
        """Tests that the __str__ method returns the correct string representation of the instance"""
        expected_str = "[{}] ({}) {}".format(self.base.__class__.__name__, self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), expected_str)

    def test_save(self):
        """Tests that the save method updates the updated_at attribute with the current datetime"""
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """Tests that the to_dict method returns a dictionary representation of the instance with correct keys and values"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["id"], self.base.id)
        self.assertEqual(base_dict["created_at"], self.base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], self.base.updated_at.isoformat())

    def test_init_from_dict(self):
        """Tests that an instance can be initialized from a dictionary representation"""
        base_dict = self.base.to_dict()
        base2 = BaseModel(**base_dict)
        self.assertIsInstance(base2, BaseModel)
        self.assertEqual(base2.id, base_dict["id"])
        self.assertEqual(base2.created_at, datetime.strptime(base_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base2.updated_at, datetime.strptime(base_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"))
