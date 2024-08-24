#!/usr/bin/python3
"""Unittest for file storage"""

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test methods with an instance of FileStorage"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after each test method"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_all_returns_dict(self):
        """Test that the all method returns the __objects dictionary"""
        self.assertIsInstance(self.storage.all(), dict)
