from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_countries.fields import CountryField

from profile.models import UserProfile


class Category(models.Model):
    """
    Model for category
    """

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    """
    Model for brand
    """

    class Meta:
        verbose_name_plural = "Brands"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class MeasurementType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    measurement_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    measurement_type = models.ForeignKey(
        MeasurementType,
        on_delete=models.SET_NULL,
        related_name="measurements",
        null=True,
    )

    def __str__(self):
        return f"{self.name} | ({self.abbreviation})"


class Shipping(models.Model):
    name = models.CharField(max_length=50)
    days = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ProductMessage(models.Model):
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text


class Currency(models.Model):
    name = models.CharField(max_length=3)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} | {self.symbol}"


class Product(models.Model):
    """
    Model for products
    """

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.ForeignKey("Brand", null=True, blank=True, on_delete=models.SET_NULL)
    on_sale = models.BooleanField(default=False)
    created_on = models.DateField(default=timezone.now)
    average_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    materials = models.TextField(null=True, blank=True)
    country_origin = CountryField(blank_label="Country *", null=False, blank=False)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)
    measurement_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    stock_quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ["-last_updated"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{num}"
            num += 1
        return unique_slug

    def clean(self):
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    """
    Model representing a product variant
    """

    SHOE_SIZE_CHOICES = [
        ("4", "Four"),
        ("5", "Five"),
        ("6", "Six"),
        ("7", "Seven"),
        ("8", "Eight"),
        ("9", "Nine"),
        ("10", "Ten"),
        ("11", "Eleven"),
        ("12", "Twelve"),
    ]

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    men_shoe_size = models.CharField(
        max_length=10, choices=SHOE_SIZE_CHOICES, null=True, blank=True
    )
    women_shoe_size = models.CharField(
        max_length=10, choices=SHOE_SIZE_CHOICES, null=True, blank=True
    )
    color = models.CharField(max_length=50, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Men Shoe Size: {self.men_shoe_size}, Women Shoe Size: \
                {self.women_shoe_size}, \
                        Color: {self.color}"


class Reviews(models.Model):
    """
    model to render review
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=1500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "product"], name="reviews_per_user")
        ]
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.title
