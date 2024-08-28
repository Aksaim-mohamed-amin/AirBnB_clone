#!/usr/bin/python3
"""
Unittest for the User class
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up a fresh user instance for each test."""
        self.user1 = User()

    def test_email_is_str(self):
        """Test that the user attribute email is a string"""
        self.assertIsInstance(self.user1.email, str)

    def test_password_is_str(self):
        """Test that the user attribute password is a string"""
        self.assertIsInstance(self.user1.password, str)

    def test_first_name_is_str(self):
        """Test that the user attribute first_name is a string"""
        self.assertIsInstance(self.user1.first_name, str)

    def test_last_name_is_str(self):
        """Test that the user attribute last_name is a string"""
        self.assertIsInstance(self.user1.last_name, str)
