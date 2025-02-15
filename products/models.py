from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


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
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category",
    )
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="noimage.png")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10000)],
    )
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

    def sell_price(self):
        if self.discount and self.discount > 0:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price

    def get_rating_class(self):
        if self.rating is None:
            return "width-0percent"
        percentage = (float(self.rating) / 5) * 100
        return f"width-{int((percentage // 20) * 20)}percent"

    def __str__(self):
        return self.name
