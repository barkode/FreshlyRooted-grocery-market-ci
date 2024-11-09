import unittest
from unittest.mock import patch

from checkout.forms import Meta  # adjust your import based on actual project structure
from django.test import TestCase


class TestMeta(TestCase):
    def setUp(self):
        self.model = Meta.model
        self.fields = Meta.fields

    # Test that model is Order
    def test_model_is_order(self):
        self.assertEqual(self.model, "Order")

    # Test for fields
    def test_fields(self):
        expected_fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )
        self.assertTupleEqual(self.fields, expected_fields)


if __name__ == "__main__":
    unittest.main()
