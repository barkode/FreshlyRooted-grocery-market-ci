import unittest
from unittest.mock import MagicMock, patch

from django import forms
from products.forms import ProductForm
from products.models import Category, Product


class ProductFormTest(unittest.TestCase):

    def setUp(self):
        self.form = ProductForm()

    def test_form_meta(self):
        self.assertEqual(self.form.Meta.model, Product)
        self.assertEqual(self.form.Meta.fields, "__all__")

    @patch("products.forms.Category.objects.all")
    def test_form_init_categories(self, mock_all):
        category1 = MagicMock()
        category1.id = 1
        category1.get_friendly_name.return_value = "Category 1"
        category2 = MagicMock()
        category2.id = 2
        category2.get_friendly_name.return_value = "Category 2"
        mock_all.return_value = [category1, category2]

        form = ProductForm()

        self.assertEqual(
            form.fields["category"].choices, [(1, "Category 1"), (2, "Category 2")]
        )

    def test_form_init_field_classes(self):
        for field_name, field in self.form.fields.items():
            self.assertEqual(field.widget.attrs["class"], "border-black rounded-0")

    def test_form_image(self):
        self.assertIsInstance(self.form.fields["image"], forms.ImageField)
        self.assertEqual(self.form.fields["image"].label, "Image")
        self.assertFalse(self.form.fields["image"].required)
        self.assertIsInstance(
            self.form.fields["image"].widget, CustomClearableFileInput
        )


if __name__ == "__main__":
    unittest.main()
