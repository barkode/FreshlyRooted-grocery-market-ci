import unittest
from unittest.mock import MagicMock, patch

from django.core.paginator import Paginator
from django.test import RequestFactory
from products.models import Category, Product
from products.views import all_products
from favorites.models import Favorites


class AllProductsTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("products.views.Product.objects.all")
    @patch("products.views.Favorites.objects.get_or_create")
    def test_all_products(self, mock_get_or_create, mock_products):
        request = self.factory.get("/products")

        # Mocking user
        user = MagicMock()
        user.is_authenticated = True
        request.user = user

        mock_get_or_create.return_value = (None, None)
        mock_products.return_value = Product.objects.none()

        # Call the view
        response = all_products(request)

        # Verify everything was called correctly
        mock_get_or_create.assert_called_once_with(user=user)
        mock_products.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("products.views.Product.objects.all")
    @patch("products.views.Favorites.objects.get_or_create")
    def test_all_products_with_query(self, mock_get_or_create, mock_products):
        request = self.factory.get("/products?q=test")

        # Mocking user
        user = MagicMock()
        user.is_authenticated = True
        request.user = user

        mock_get_or_create.return_value = (None, None)
        mock_products.return_value = Product.objects.none()

        # Call the view
        response = all_products(request)

        # Verify everything was called correctly
        mock_get_or_create.assert_called_once_with(user=user)
        mock_products.assert_called_once()
        self.assertEqual(response.status_code, 200)

    @patch("products.views.Product.objects.filter")
    @patch("products.views.Category.objects.values_list")
    @patch("products.views.Product.objects.all")
    @patch("products.views.Favorites.objects.get_or_create")
    def test_all_products_with_category(
        self,
        mock_get_or_create,
        mock_products,
        mock_category_values_list,
        mock_products_filter,
    ):
        request = self.factory.get("/products?category=test")

        # Mocking user
        user = MagicMock()
        user.is_authenticated = True
        request.user = user

        mock_get_or_create.return_value = (None, None)
        mock_products.return_value = Product.objects.none()
        paginator = MagicMock(spec=Paginator)
        paginator.num_pages = 1
        mock_products_filter.return_value = paginator.page(1)

        mock_category_values_list.return_value = ["test"]

        # Call the view
        response = all_products(request)

        # Verify everything was called correctly
        mock_get_or_create.assert_called_once_with(user=user)
        mock_products.assert_called_once()
        mock_category_values_list.assert_called_once()
        mock_products_filter.assert_called_once()
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
