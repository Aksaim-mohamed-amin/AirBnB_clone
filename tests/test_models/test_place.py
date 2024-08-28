#!/usr/bin/python3
"""
Unittest for the Place class
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up a fresh Place instance for each test."""
        self.place = Place()

    def test_city_id_is_str(self):
        """Test that the place attribute city_id is a string"""
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_is_str(self):
        """Test that the place attribute user_id is a string"""
        self.assertIsInstance(self.place.user_id, str)

    def test_name_is_str(self):
        """Test that the place attribute name is a string"""
        self.assertIsInstance(self.place.name, str)

    def test_descritption_is_str(self):
        """Test that the place attribute description is a string"""
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_is_int(self):
        """Test that the place attribute number_rooms is an integer"""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_is_int(self):
        """Test that the place attribute number_bathrooms is an integer"""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_is_int(self):
        """Test that the place attribute max_guest is an integer"""
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_is_int(self):
        """Test that the place attribute price_by_night is an integer"""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_is_flaot(self):
        """Test that the place attribute latitude is a float"""
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_is_flaot(self):
        """Test that the place attribute longitude is a float"""
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_is_list(self):
        """Test that the place attribute amenity_ids is a list"""
        self.assertIsInstance(self.place.amenity_ids, list)
