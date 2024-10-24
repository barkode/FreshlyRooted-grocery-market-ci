from django.contrib import admin

from .models import Category, Measurement, MeasurementType, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'friendly_name')


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('sku', 'name', 'category', 'price', 'rating', 'image')


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'measurement_type')


class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_type')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(MeasurementType, MeasurementTypeAdmin)
