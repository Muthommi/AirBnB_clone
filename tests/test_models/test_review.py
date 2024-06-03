#!/usr/bin/python3
"""Test for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests the Review class"""

    def setUp(self):
        """Set up test environment"""
        self.review = Review()

    def test_instance_creation(self):
        """Tests if review instance is created correctly"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test if the review has the correct attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str_method(self):
        """Test the __str__ method"""
        string = str(self.review)
        self.assertIn("[Review]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("id", review_dict)


if __name__ == '__main__':
    unittest.main()
