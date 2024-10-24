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
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    measurement_type = models.ForeignKey(MeasurementType, on_delete=models.SET_NULL, related_name="measurements",
                                         null=True)

    def __str__(self):
        return f"{self.name} | ({self.abbreviation})"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True, default='noimage.png')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField()
    added_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)
    measurement_value = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} | ({self.measurement_value} | {self.measurement.abbreviation})"
