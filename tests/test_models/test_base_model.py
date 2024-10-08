#!/usr/bin/python3
"""
Unittest for the BaseModel class
"""

import unittest
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up a fresh BaseModel instance for each test."""
        self.i1 = BaseModel()
        self.i2 = BaseModel()

    def test_init_with_kwargs(self):
        """Test initialisation of an instance from a dictionary"""
        self.i1.name = "Test Model"
        self.i1.my_number = 7
        i1_dict = self.i1.to_dict()

        new_model = BaseModel(**i1_dict)

        self.assertEqual(new_model.id, self.i1.id)
        self.assertEqual(new_model.created_at, self.i1.created_at)
        self.assertEqual(new_model.updated_at, self.i1.updated_at)

        self.assertIn('name', new_model.to_dict())
        self.assertIn('my_number', new_model.to_dict())

        self.assertEqual(new_model.name, 'Test Model')
        self.assertEqual(new_model.my_number, 7)

        self.assertNotEqual(self.i1, new_model)

    def test_init_with_kwargs_missing_fields(self):
        """Test initialization when kwargs are missing some fields"""
        partial_dict = {key: value for key, value in self.i2.to_dict().items()
                        if key not in ['name', 'my_number']}

        new_model = BaseModel(**partial_dict)

        self.assertEqual(new_model.id, self.i2.id)
        self.assertEqual(new_model.created_at, self.i2.created_at)
        self.assertEqual(new_model.updated_at, self.i2.updated_at)

        self.assertNotIn('name', new_model.to_dict())
        self.assertNotIn('my_number', new_model.to_dict())

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

    def test_save_updated_at(self):
        """Test if updated_at was correctly updated"""
        o_updated_at = self.i1.updated_at
        self.i1.save()

        self.assertNotEqual(self.i1.updated_at, o_updated_at)

    def test_save_to_json_file(self):
        """test if the instance is correctly saved to storage file"""
        self.i2.save()
        key = f"{self.i2.__class__.__name__}.{self.i2.id}"
        with open('file.json', 'r') as json_file:
            objects = json.load(json_file)
            self.assertEqual(objects[key], self.i2.to_dict())

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
