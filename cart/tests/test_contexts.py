import unittest
from decimal import Decimal
from unittest.mock import MagicMock, patch

from cart import contexts
from django.shortcuts import get_object_or_404
from django.test import RequestFactory


class TestCartContexts(unittest.TestCase):

	def setUp(self):
		self.factory = RequestFactory()

	@patch.object(contexts, 'get_object_or_404')
	@patch.object(contexts.Product, 'sell_price', MagicMock(return_value=Decimal('50.0')))
	def test_cart_contents_empty(self, mock_get_object_or_404):
		request = self.factory.get('/cart/')
		request.session = {'cart': {}}
		result = contexts.cart_contents(request)

		expected_result = {
			"cart_items": [],
			"total": Decimal('0.0'),
			"product_count": 0,
			"delivery": Decimal('0.0'),
			"free_delivery_delta": contexts.settings.FREE_DELIVERY_THRESHOLD,
			"free_delivery_threshold": contexts.settings.FREE_DELIVERY_THRESHOLD,
			"grand_total": Decimal('0.0'),
			"progress_percentage": Decimal('0.0'),
			}

		self.assertEqual(result, expected_result)

	@patch.object(contexts, 'get_object_or_404')
	@patch.object(contexts.Product, 'sell_price', MagicMock(return_value=Decimal('50.0')))
	def test_cart_contents_with_items(self, mock_get_object_or_404):
		mock_product = MagicMock()
		mock_product.currency.symbol = '$'
		mock_get_object_or_404.return_value = mock_product

		request = self.factory.get('/cart/')
		request.session = {'cart': {'1': 2, '2': {'items_by_size': {'S': 1, 'M': 3}}}}

		result = contexts.cart_contents(request)

		expected_result = {
			"cart_items": [
				{
					'item_id': '1',
					'quantity': 2,
					'product': mock_product,
					'currency_symbol': '$',
					},
				{
					'item_id': '2',
					'quantity': 1,
					'product': mock_product,
					'size': 'S',
					'currency_symbol': '$',
					},
				{
					'item_id': '2',
					'quantity': 3,
					'product': mock_product,
					'size': 'M',
					'currency_symbol': '$',
					},
				],
			"total": Decimal('300.0'),
			"product_count": 6,
			"delivery": Decimal('60.0'),  # 20% deliver charge
			"free_delivery_delta": Decimal('700.0'),
			"free_delivery_threshold": contexts.settings.FREE_DELIVERY_THRESHOLD,
			"grand_total": Decimal('360.0'),
			"progress_percentage": 30,
			}

		self.assertEqual(result, expected_result)


if __name__ == "__main__":
	unittest.main()
