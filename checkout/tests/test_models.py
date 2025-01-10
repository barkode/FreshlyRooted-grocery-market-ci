import uuid
from decimal import Decimal

from checkout.models import Order, UserProfile
from django.contrib.auth import get_user_model
from django.test import TestCase
from django_countries.fields import CountryField


class OrderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="abcdef123"
        )
        testuser1.save()
        test_profile = UserProfile.objects.create(user=testuser1)
        test_profile.save()
        test_order = Order.objects.create(
            order_number=uuid.uuid4().hex.upper(),
            user_profile=test_profile,
            full_name="Test User",
            email="test@example.com",
            phone_number="01234567890",
            country=CountryField(
                blank_label="Country *", null=False, blank=False
            ).to_python("GB"),
            town_or_city="Test City",
            street_address1="123 Test Street",
            street_address2="Test Suburb",
            county="Test County",
            delivery_cost=Decimal("5.00"),
            order_total=Decimal("15.00"),
            grand_total=Decimal("20.00"),
            original_bag="",
            stripe_pid="test_stripe_pid",
        )
        test_order.save()

    def test_order_content(self):
        order = Order.objects.get(id=1)
        expected_order_number = f"{order.order_number}"
        expected_user_profile = f"{order.user_profile}"
        expected_full_name = f"{order.full_name}"
        expected_email = f"{order.email}"
        expected_phone_number = f"{order.phone_number}"
        expected_country = f"{order.country}"
        expected_town_or_city = f"{order.town_or_city}"
        expected_street_address1 = f"{order.street_address1}"
        expected_street_address2 = f"{order.street_address2}"
        expected_county = f"{order.county}"
        expected_delivery_cost = f"{order.delivery_cost}"
        expected_order_total = f"{order.order_total}"
        expected_grand_total = f"{order.grand_total}"
        expected_origional_bag = f"{order.origional_bag}"
        expected_stripe_pid = f"{order.stripe_pid}"
        self.assertEquals(expected_order_number, str(order))
        self.assertEquals(expected_user_profile, str(order.user_profile))
        self.assertEquals(expected_full_name, str(order.full_name))
        self.assertEquals(expected_email, str(order.email))
        self.assertEquals(expected_phone_number, str(order.phone_number))
        self.assertEquals(expected_country, str(order.country))
        self.assertEquals(expected_town_or_city, str(order.town_or_city))
        self.assertEquals(expected_street_address1, str(order.street_address1))
        self.assertEquals(expected_street_address2, str(order.street_address2))
        self.assertEquals(expected_county, str(order.county))
        self.assertEquals(expected_delivery_cost, str(order.delivery_cost))
        self.assertEquals(expected_order_total, str(order.order_total))
        self.assertEquals(expected_grand_total, str(order.grand_total))
        self.assertEquals(expected_origional_bag, str(order.origional_bag))
        self.assertEquals(expected_stripe_pid, str(order.stripe_pid))

    def test_order_list(self):
        response = self.client.get(reverse("checkout:orders"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")
        self.assertTemplateUsed(response, "orders.html")

    def test_order_create(self):
        url = reverse("checkout:checkout")
        data = {
            "order_number": uuid.uuid4().hex.upper(),
            "user_profile": 1,
            "full_name": "New User",
            "email": "new@example.com",
            "phone_number": "09876543210",
            "country": "US",
            "town_or_city": "New City",
            "street_address1": "321 Test Ave",
            "street_address2": "Test District",
            "county": "New County",
            "delivery_cost": "10.00",
            "order_total": "30.00",
            "grand_total": "40.00",
            "original_bag": "",
            "stripe_pid": "new_stripe_pid",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

    def test_order_update(self):
        response = self.client.post(
            reverse("checkout:update_order", args="1"),
            {
                "full_name": "Updated User",
                "email": "update@example.com",
                "phone_number": "1122334455",
                "country": "DE",
                "town_or_city": "Updated City",
                "street_address1": "456 Update Blvd",
                "street_address2": "Update Area",
                "county": "Updated County",
                "delivery_cost": "7.00",
                "order_total": "21.00",
                "grand_total": "28.00",
                "original_bag": "",
                "stripe_pid": "update_stripe_pid",
            },
        )
        self.assertEqual(response.status_code, 302)

    def test_order_delete(self):
        response = self.client.get(reverse("checkout:delete_order", args="1"))
        self.assertEqual(response.status_code, 200)
