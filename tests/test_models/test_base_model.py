#!/usr/bin/python3
"""
Unittest for the BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a fresh BaseModel instance for each test."""
        self.i1 = BaseModel()
        self.i2 = BaseModel()

    def test_id_is_unique(self):
        """Test that each instance of BaseModel has a unique id"""
        self.assertNotEqual(self.i1.id, self.i2.id)

    def test_id_is_string(self):
        """Test that the id is a string"""
        self.assertIsInstance(self.i1.id, str)

    def test_created_at_type(self):
        """Test the type of the created_at attribute"""
        self.assertIsInstance(self.i1.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of the updated_at attribute"""
        self.assertIsInstance(self.i1.updated_at, datetime)

    def test_str(self):
        """Test the str method"""
        class_name = self.i1.__class__.__name__
        id = self.i1.id
        dict_copy = self.i1.__dict__.copy()

        self.assertEqual(str(self.i1), "[{}] ({}) {}".format(class_name, id,
                                                             dict_copy))

    def test_save(self):
        """Test the save method"""
        o_updated_at = self.i1.updated_at
        self.i1.save()

        self.assertNotEqual(self.i1.updated_at, o_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        i2_dict = self.i2.to_dict()

        self.assertIn('__class__', i2_dict)
        self.assertIn('id', i2_dict)
        self.assertIn('created_at', i2_dict)
        self.assertIn('updated_at', i2_dict)

        self.assertEqual(i2_dict['__class__'], 'BaseModel')
        self.assertEqual(i2_dict['created_at'], self.i2.created_at.isoformat())
        self.assertEqual(i2_dict['updated_at'], self.i2.updated_at.isoformat())

        self.assertIsInstance(i2_dict['id'], str)
        self.assertIsInstance(i2_dict['created_at'], str)
        self.assertIsInstance(i2_dict['updated_at'], str)
