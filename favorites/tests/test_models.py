import unittest
from unittest.mock import Mock

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from favorites.models import Favorites
from products.models import Product


class FavoritesModelTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='12345')
		self.product1 = Product.objects.create(name='Product 1', description='Product 1 description')
		self.product2 = Product.objects.create(name='Product 2', description='Product 2 description')

	def test_creation(self):
		fav = Favorites.objects.create(user=self.user)
		self.assertIsInstance(fav, Favorites)
		self.assertEqual(fav.user.username, 'testuser')

	def test_date_added_field(self):
		fav = Favorites.objects.create(user=self.user)
		self.assertIsNotNone(fav.date_added)

	def test_str(self):
		fav = Favorites.objects.create(user=self.user)
		self.assertEqual(str(fav), "testuser's Favorites")

	def test_products_relation(self):
		fav = Favorites.objects.create(user=self.user)
		fav.products.add(self.product1)
		fav.products.add(self.product2)
		self.assertEqual(fav.products.count(), 2)

	def test_user_field_on_delete(self):
		fav = Favorites.objects.create(user=self.user)
		self.user.delete()
		with self.assertRaises(Favorites.DoesNotExist):
			Favorites.objects.get(id=fav.id)


if __name__ == '__main__':
	unittest.main()
