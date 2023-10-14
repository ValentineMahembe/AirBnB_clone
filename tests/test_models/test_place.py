#!/usr/bin/python3
"""This module defines the tests for the Place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """This class tests the Place class"""

    def setUp(self):
        """Sets up an instance of Place for testing"""
        self.place = Place()

    def tearDown(self):
        """Tears down the instance of Place after testing"""
        del self.place

    def test_init(self):
        """Tests that an instance can be initialized with default or custom values"""
        place1 = Place()
        place2 = Place(city_id="1234", user_id="5678", name="My place", description="Nice place",
                       number_rooms=3, number_bathrooms=2, max_guest=5, price_by_night=100,
                       latitude=37.7749, longitude=-122.4194, amenity_ids=["4321", "8765"])
        
        # check default values
        self.assertIsInstance(place1.city_id, str)
        self.assertIsInstance(place1.user_id, str)
        self.assertIsInstance(place1.name, str)
        self.assertIsInstance(place1.description, str)
        self.assertIsInstance(place1.number_rooms, int)
        self.assertIsInstance(place1.number_bathrooms, int)
        self.assertIsInstance(place1.max_guest, int)
        self.assertIsInstance(place1.price_by_night, int)
        self.assertIsInstance(place1.latitude, float)
        self.assertIsInstance(place1.longitude, float)
        self.assertIsInstance(place1.amenity_ids, list)
        self.assertEqual(place1.city_id, "")
        self.assertEqual(place1.user_id, "")
        self.assertEqual(place1.name, "")
        self.assertEqual(place1.description, "")
        self.assertEqual(place1.number_rooms, 0)
        self.assertEqual(place1.number_bathrooms, 0)
        self.assertEqual(place1.max_guest, 0)
        self.assertEqual(place1.price_by_night, 0)
        self.assertEqual(place1.latitude, 0.0)
        self.assertEqual(place1.longitude, 0.0)
        self.assertEqual(place1.amenity_ids, [])

        # check custom values
        self.assertEqual(place2.city_id, "1234")
        self.assertEqual(place2.user_id, "5678")
        self.assertEqual(place2.name, "My place")
        self.assertEqual(place2.description, "Nice place")
