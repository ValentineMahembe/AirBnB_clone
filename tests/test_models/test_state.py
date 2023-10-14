#!/usr/bin/python3
"""This module defines the tests for the State class"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """This class tests the State class"""

    def setUp(self):
        """Sets up an instance of State for testing"""
        self.state = State()

    def tearDown(self):
        """Tears down the instance of State after testing"""
        del self.state

    def test_init(self):
        """Tests that an instance can be initialized with default or custom values"""
        state1 = State()
        state2 = State(name="California")
        
        # check default values
        self.assertIsInstance(state1.name, str)
        self.assertEqual(state1.name, "")

        # check custom values
        self.assertEqual(state2.name, "California")

    def test_inheritance(self):
        """Tests that the State class inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_attributes(self):
        """Tests that the State class has the public class attribute name"""
        self.assertTrue(hasattr(State, "name"))
