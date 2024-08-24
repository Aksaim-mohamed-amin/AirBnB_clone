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

    def test_new_adds_object(self):
        """Test that new adds an object to __objects."""
        self.storage.new(self.model)
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save actually saves the objects to file.json."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_correct_content(self):
        """Test that save writes the correct content to the file."""
        self.storage.new(self.model)
        self.storage.save()

        with open('file.json', 'r') as json_file:
            data = json.load(json_file)

        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key], self.model.to_dict())

    def test_reload_loads_objects(self):
        """Test that reload loads objects from the file."""
        self.storage.new(self.model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, new_storage.all())

    def test_reload_no_file(self):
        """Test that reload does nothing if no file exists."""
        new_storage = FileStorage()
        self.assertIsNone(new_storage.reload())
