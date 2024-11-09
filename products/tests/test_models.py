import unittest
from decimal import Decimal

from django.test import TestCase
from products.models import (
    Category,
    Currency,
    Measurement,
    Product,
    ProductMessage,
    Shipping,
)


class TestModels(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="testCategory")
        self.measurement = Measurement.objects.create(name="testMeasurement")
        self.shipping = Shipping.objects.create(name="testShipping")
        self.product_message = ProductMessage.objects.create(message="testMessage")
        self.currency = Currency.objects.create(name="testCurrency", symbol="$")
        self.product = Product.objects.create(
            category=self.category,
            description="Test Product",
            name="Test Product",
            price=Decimal("14.99"),
            sku="SKU123456",
            stock_quantity=10,
            measurement=self.measurement,
            measurement_value=Decimal("10.00"),
            rating=Decimal("4.00"),
            shipping=self.shipping,
            message=self.product_message,
            currency=self.currency,
            discount=Decimal("10.00"),
        )

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), "Test Product")

    def test_slug_generation(self):
        self.assertIsNotNone(self.product.slug)

    def test_sell_price_with_discount(self):
        self.assertEqual(self.product.sell_price(), Decimal("13.49"))

    def test_get_rating_class(self):
        self.assertEqual(self.product.get_rating_class(), "width-80percent")


class TestUniqueSlug(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="testCategory")
        self.measurement = Measurement.objects.create(name="testMeasurement")
        self.shipping = Shipping.objects.create(name="testShipping")
        self.product_message = ProductMessage.objects.create(message="testMessage")
        self.currency = Currency.objects.create(name="testCurrency", symbol="$")
        self.product1 = Product.objects.create(
            category=self.category,
            description="Test Product 1",
            name="Test Product",
            price=Decimal("14.99"),
            sku="SKU123456",
            stock_quantity=10,
            measurement=self.measurement,
            measurement_value=Decimal("10.00"),
            rating=Decimal("4.00"),
            shipping=self.shipping,
            message=self.product_message,
            currency=self.currency,
            discount=Decimal("10.00"),
        )
        self.product2 = Product.objects.create(
            category=self.category,
            description="Test Product 2",
            name="Test Product",
            price=Decimal("14.99"),
            sku="SKU123457",
            stock_quantity=10,
            measurement=self.measurement,
            measurement_value=Decimal("10.00"),
            rating=Decimal("4.00"),
            shipping=self.shipping,
            message=self.product_message,
            currency=self.currency,
            discount=Decimal("10.00"),
        )

    def test_unique_slug(self):
        self.assertNotEqual(self.product1.slug, self.product2.slug)


if __name__ == "__main__":
    unittest.main()
