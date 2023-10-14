#!/usr/bin/python3
"""This module defines the tests for the City class"""

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """This class tests the City class"""

    def setUp(self):
        """Sets up an instance of City for testing"""
        self.city = City()

    def tearDown(self):
        """Tears down the instance of City after testing"""
        del self.city

    def test_init(self):
        """Tests that an instance can be initialized with default or custom values"""
        city1 = City()
        city2 = City(state_id="1234", name="San Francisco")
        
        # check default values
        self.assertIsInstance(city1.state_id, str)
        self.assertIsInstance(city1.name, str)
        self.assertEqual(city1.state_id, "")
        self.assertEqual(city1.name, "")

        # check custom values
        self.assertEqual(city2.state_id, "1234")
        self.assertEqual(city2.name, "San Francisco")

    def test_inheritance(self):
        """Tests that the City class inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_attributes(self):
        """Tests that the City class has the public class attributes state_id and name"""
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))
