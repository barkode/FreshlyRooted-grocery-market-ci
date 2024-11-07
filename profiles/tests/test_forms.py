import unittest
from unittest import mock

from profiles.forms import UserProfileForm


class TestUserProfileForm(unittest.TestCase):

	def setUp(self):
		self.form = UserProfileForm()

	@mock.patch('profiles.forms.UserProfileForm.__init__')
	def test_init_called_with_correct_parameters(self, mock_init):
		mock_init.return_value = None
		UserProfileForm()
		self.assertTrue(mock_init.called)

	def test_form_meta(self):
		self.assertEqual(self.form.Meta.exclude[0], 'user')
		self.assertEqual(self.form.Meta.model.__name__, 'UserProfile')

	def test_form_fields(self):
		form = UserProfileForm()
		self.assertEquals(form.fields['default_phone_number'].widget.attrs['autofocus'], True)

		for field in form.fields:
			if field != 'default_country':
				self.assertIn('placeholder', form.fields[field].widget.attrs)
			self.assertIn('class', form.fields[field].widget.attrs)
			self.assertFalse(form.fields[field].label)

	def test_form_attributes_non_empty(self):
		form = UserProfileForm()
		for field in form.fields:
			self.assertTrue(form.fields[field].widget.attrs)


if __name__ == "__main__":
	unittest.main()
