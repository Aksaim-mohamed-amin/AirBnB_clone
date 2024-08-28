#!/usr/bin/python3
"""
Unittest for the Review class
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up a fresh Review instance for each test."""
        self.review = Review()

    def test_place_id_is_str(self):
        """Test that the review attribute place_id is a string"""
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_is_str(self):
        """Test that the review attribute user_id is a string"""
        self.assertIsInstance(self.review.user_id, str)

    def test_text_is_str(self):
        """Test that the review attribute text is a string"""
        self.assertIsInstance(self.review.text, str)
