#!/usr/bin/python3
"""This module defines the tests for the Review class"""

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """This class tests the Review class"""

    def setUp(self):
        """Sets up an instance of Review for testing"""
        self.review = Review()

    def tearDown(self):
        """Tears down the instance of Review after testing"""
        del self.review

    def test_init(self):
        """Tests that an instance can be initialized with default or custom values"""
        review1 = Review()
        review2 = Review(place_id="1234", user_id="5678", text="Great place")
        
        # check default values
        self.assertIsInstance(review1.place_id, str)
        self.assertIsInstance(review1.user_id, str)
        self.assertIsInstance(review1.text, str)
        self.assertEqual(review1.place_id, "")
        self.assertEqual(review1.user_id, "")
        self.assertEqual(review1.text, "")

        # check custom values
        self.assertEqual(review2.place_id, "1234")
        self.assertEqual(review2.user_id, "5678")
        self.assertEqual(review2.text, "Great place")

    def test_inheritance(self):
        """Tests that the Review class inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_attributes(self):
        """Tests that the Review class has the public class
        attributes place_id, user_id and text"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))
