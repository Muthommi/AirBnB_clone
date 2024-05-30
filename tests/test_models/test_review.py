#!/usr/bin/python3
"""Test for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests the Review class"""

    def setUp(self):
        """Set up test environment"""
        self.review = Review()

    def test_inheritance(self):
        """Tests if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Tests attributes of review"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqula(self.review.text, "")

    def test_attribute_types(self):
        """Tests types of Review attributes"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
