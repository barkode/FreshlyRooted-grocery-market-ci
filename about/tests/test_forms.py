import unittest

from about.forms import CollaborateForm
from django.test import TestCase


class CollaborateFormTest(TestCase):

	def setUp(self):
		self.data = {
			"name": "Test User",
			"email": "testuser@test.com",
			"message": "This is a test message",
			}

	def test_form_valid(self):
		form = CollaborateForm(data=self.data)
		self.assertTrue(form.is_valid())

	def test_form_invalid(self):
		self.data["email"] = "invalidemail"
		form = CollaborateForm(data=self.data)
		self.assertFalse(form.is_valid())

	def test_form_fields(self):
		form = CollaborateForm()
		self.assertEqual(
			sorted(["name", "email", "message"]), sorted(list(form.fields))
			)


if __name__ == "__main__":
	unittest.main()
