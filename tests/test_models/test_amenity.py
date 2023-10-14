#!/usr/bin/python3
"""This module defines the tests for the Amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """This class tests the Amenity class"""

    def setUp(self):
        """Sets up an instance of Amenity for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down the instance of Amenity after testing"""
        del self.amenity

    def test_init(self):
        """Tests that an instance can be initialized with default or custom values"""
        amenity1 = Amenity()
        amenity2 = Amenity(name="Wifi")
        
        # check default values
        self.assertIsInstance(amenity1.name, str)
        self.assertEqual(amenity1.name, "")

        # check custom values
        self.assertEqual(amenity2.name, "Wifi")

    def test_inheritance(self):
        """Tests that the Amenity class inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)
