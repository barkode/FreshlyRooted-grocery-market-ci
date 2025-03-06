from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Brand, Category, Currency, Measurement, MeasurementType, \
	Product, ProductVariant, Reviews


class ProductVariantInline(admin.StackedInline):
	model = ProductVariant
	extra = 1


class ProductAdmin(SummernoteModelAdmin, admin.ModelAdmin):
	search_fields = [
		'name',
		]

	list_display = (
		'name',
		'category',
		'price',
		'sale_price',
		'rating',
		'brand',
		'on_sale',
		'created_on',
		'country_origin',
		'sku',
		'slug',
		'measurement',
		)
	summernote_fields = ("materials",)
	list_editable = (
		"on_sale",
		)
	prepopulated_fields = {'slug': ('name',)}
	readonly_fields = ['sku']

	list_filter = ['created_on', 'on_sale']

	ordering = ("name",)

	def save_model(self, request, obj, form, change):
		# Save model after call save() method
		super().save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
	list_display = (
		'friendly_name',
		'name',
		'slug',
		)
	prepopulated_fields = {'slug': ('name',)}


class ProductVariantAdmin(admin.ModelAdmin):
	list_display = (
		'product',
		'stock_quantity',
		)


class BrandAdmin(admin.ModelAdmin):
	list_display = (
		"friendly_name",
		"name",
		"slug",
		)


class ReviewsAdmin(admin.ModelAdmin):
	list_display = (
		"product",
		"user",
		"title",
		"review",
		"created_on",
		"updated_on",
		)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Currency)
admin.site.register(Measurement)
admin.site.register(MeasurementType)
