from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

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


class SubCategory(Category):
    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"


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
    added_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="noimage.png")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, unique=True)
    stock_quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)
    measurement_value = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    shipping = models.ForeignKey(
        Shipping, on_delete=models.SET_NULL, null=True, blank=True
    )
    message = models.ForeignKey(
        ProductMessage, on_delete=models.SET_NULL, null=True, blank=True
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, blank=True
    )
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    class Meta:
        ordering = ["-added_date"]
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

    def __str__(self):
        abbreviation = self.measurement.abbreviation if self.measurement else "N/A"
        return f"{self.name} | ({self.measurement_value} | {abbreviation})"
