import unittest
from unittest.mock import patch

from blog.models import Post
from django.contrib.auth.models import User
from django.test import TestCase


class PostModelTest(TestCase):

	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='12345')
		self.post = Post.objects.create(
			title='Test title',
			slug='test-title',
			author=self.user,
			content='Lorem Ipsum',
			excerpt='Lorem Ipsum')

	def tearDown(self):
		self.user.delete()
		self.post.delete()

	def test_post_creation(self):
		self.assertIsInstance(self.post, Post)
		self.assertEqual(self.post.__str__(), 'Test title | written by testuser')

	def test_post_is_assigned_slug_on_creation(self):
		self.assertEqual(self.post.slug, 'test-title')

	def test_post_content(self):
		self.assertEqual(self.post.content, 'Lorem Ipsum')

	def test_excerpt_is_blank(self):
		self.assertEqual(self.post.excerpt, 'Lorem Ipsum')

	def test_featured_image_is_placeholder(self):
		self.assertEqual(self.post.featured_image, 'placeholder')


if __name__ == '__main__':
	unittest.main()
