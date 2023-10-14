#!/usr/bin/python3
"""This module defines the tests for the User class"""

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """This class tests the User class"""

    def setUp(self):
        """Sets up an instance of User for testing"""
        self.user = User()

    def tearDown(self):
        """Tears down the instance of User after testing"""
        del self.user

    def test_init(self):
        """Tests that an instance can be initialized with default or custom values"""
        user1 = User()
        user2 = User(email="bob@gmail.com", password="1234", first_name="Bob", last_name="Smith")
        
        # check default values
        self.assertIsInstance(user1.email, str)
        self.assertIsInstance(user1.password, str)
        self.assertIsInstance(user1.first_name, str)
        self.assertIsInstance(user1.last_name, str)
        self.assertEqual(user1.email, "")
        self.assertEqual(user1.password, "")
        self.assertEqual(user1.first_name, "")
        self.assertEqual(user1.last_name, "")

        # check custom values
        self.assertEqual(user2.email, "bob@gmail.com")
        self.assertEqual(user2.password, "1234")
        self.assertEqual(user2.first_name, "Bob")
        self.assertEqual(user2.last_name, "Smith")

    def test_inheritance(self):
        """Tests that the User class inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_attributes(self):
        """
        Tests that the User class has the public class
        attributes email, password, first_name and last_name
        """
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
