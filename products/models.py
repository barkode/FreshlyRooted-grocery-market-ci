import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_countries.fields import CountryField


class Category(models.Model):
	"""
	Model for category
	"""

	name = models.CharField(max_length=254)
	friendly_name = models.CharField(max_length=254, null=True, blank=True)
	slug = models.SlugField(max_length=254, unique=True, null=True, blank=True)
	description = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

	def get_friendly_name(self):
		return self.friendly_name

	def save(self, *args, **kwargs):

		self.name = self.name.lower()

		# Generate unique slug if it not exist
		if not self.slug:
			base_slug = slugify(self.name)
			slug = base_slug
			counter = 1

			# Check if the slug is unique
			while Category.objects.filter(slug=slug).exists():
				slug = f"{base_slug}-{counter}"
				counter += 1
			self.slug = slug

		super().save(*args, **kwargs)


class MeasurementType(models.Model):
	"""
	Model for measurement type
	"""
	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	measurement_type = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name


class Measurement(models.Model):
	"""
	Model for measurement
	"""
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
	"""
	Model for shipping
	"""
	name = models.CharField(max_length=50)
	days = models.PositiveIntegerField()

	def __str__(self):
		return self.name


class ProductMessage(models.Model):
	"""
	Model for product message
	"""
	text = models.CharField(max_length=500)

	def __str__(self):
		return self.text


class Currency(models.Model):
	"""
	Model for currency
	"""
	name = models.CharField(max_length=3)
	symbol = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.name} | {self.symbol}"


class Product(models.Model):
	"""
	Model for products
	"""

	category = models.ForeignKey('Category', null=True,
	                             blank=True, on_delete=models.SET_NULL)
	sku = models.CharField(max_length=254, unique=True, null=True, blank=True)
	slug = models.SlugField(max_length=254, unique=True, null=True, blank=True)
	name = models.CharField(max_length=254)
	description = models.TextField(null=True, blank=True)
	has_sizes = models.BooleanField(default=False, null=True, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2,
	                            validators=[MinValueValidator(0.00)])
	sale_price = models.DecimalField(max_digits=10, decimal_places=2,
	                                 null=True, blank=True,
	                                 validators=[MinValueValidator(0.00)])
	rating = models.DecimalField(max_digits=6, decimal_places=2,
	                             null=True, blank=True)
	image_url = models.URLField(max_length=1024, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	brand = models.ForeignKey("Brand", null=True, blank=True,
	                          on_delete=models.SET_NULL)
	on_sale = models.BooleanField(default=False)
	is_new = models.BooleanField(default=False)
	created_on = models.DateField(default=timezone.now)
	average_rating = models.DecimalField(max_digits=6, decimal_places=2,
	                                     null=True, blank=True)
	materials = models.TextField(null=True, blank=True)
	country_origin = CountryField(blank_label='Country *', null=True,
	                              blank=True)
	measurement = models.ForeignKey(
		Measurement,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='products',
		verbose_name='Unit of measurement'
		)

	def clean(self):
		"""
		Custom validation for the Product model
		"""
		if int(self.price or 0) < 0:
			raise ValidationError("Price cannot be negative.")

	def save(self, *args, **kwargs):

		self.name = self.name.lower()

		# Generate unique SKU if it not exist
		if not self.sku:
			self.sku = f"PRD-{uuid.uuid4().hex[:8].upper()}"

		# Generate unique SLUG if not exist
		if not self.slug:
			base_slug = slugify(self.name)
			slug = base_slug
			counter = 1

			# Check if the slug unique
			while Product.objects.filter(slug=slug).exists():
				slug = f"{base_slug}-{counter}"
				counter += 1

			self.slug = slug

		super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class ProductVariant(models.Model):
	"""
	Model representing a product variant
	"""

	product = models.ForeignKey(Product, null=False, blank=False,
	                            on_delete=models.CASCADE)
	color = models.CharField(max_length=50, null=True, blank=True)
	stock_quantity = models.PositiveIntegerField(default=0)


class Brand(models.Model):
	"""
	Model for brand
	"""

	class Meta:
		verbose_name_plural = "Brands"

	name = models.CharField(max_length=254)
	friendly_name = models.CharField(max_length=254, null=True, blank=True)
	slug = models.SlugField(max_length=254, unique=True, null=True, blank=True)

	def save(self, *args, **kwargs):

		# Generate unique slug if it not exist
		if not self.slug:
			base_slug = slugify(self.name)
			slug = base_slug
			counter = 1

			# Check if the slug is unique
			while Category.objects.filter(slug=slug).exists():
				slug = f"{base_slug}-{counter}"
				counter += 1
			self.slug = slug

		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	def get_friendly_name(self):
		return self.friendly_name


class Reviews(models.Model):
	"""
	Model to render review
	"""
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100, blank=True)
	review = models.TextField(max_length=1500, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=["user", "product"], name="reviews_per_user")
			]
		verbose_name_plural = "Reviews"

	def __str__(self):
		return self.title
