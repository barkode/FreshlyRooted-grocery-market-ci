import unittest
from unittest.mock import Mock, patch
from about.views import about_contact
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory


class AboutContactTest(unittest.TestCase):

    def setUp(self):
	    self.factory = RequestFactory()

    @patch("about.views.About.objects", new_callable=Mock)
    @patch("about.views.process_collaborate_form", return_value=False)
    def test_about_contact_GET(self, mock_process_collaborate_form):
	    request = self.factory.get("/about/contact/")
	    response = about_contact(request)
        self.assertEqual(response.status_code, 200)

    @patch("about.views.About.objects", new_callable=Mock)
    @patch("about.views.messages")
    @patch("about.views.process_collaborate_form")
    def test_about_contact_POST_valid(
		    self, mock_process_collaborate_form, mock_messages
		    ):
	    mock_process_collaborate_form.return_value = True
	    request = self.factory.post("/about/contact/")
	    request.session = "session"
	    request._messages = FallbackStorage(request)
	    response = about_contact(request)
	    mock_messages.success.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("about.views.About.objects", new_callable=Mock)
    @patch("about.views.process_collaborate_form", return_value=False)
    def test_about_contact_POST_invalid(self, mock_process_collaborate_form):
	    request = self.factory.post("/about/contact/")
	    request.session = "session"
	    request._messages = FallbackStorage(request)
	    response = about_contact(request)
	    self.assertEqual(response.status_code, 200)
	    self.assertFalse(mock_process_collaborate_form.called)


if __name__ == "__main__":
	unittest.main()
