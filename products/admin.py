from django.contrib import admin

from .models import Category, Measurement, MeasurementType, Product, ProductMessage, Shipping, Currency

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'friendly_name',)
    ordering = ('name', 'friendly_name',)



class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'measurement_type',)



class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_type',)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('sku', 'name', 'category', 'price', 'rating', 'image',)
    ordering = ('sku', 'name', 'category', 'rating',)



class ProductMessageAdmin(admin.ModelAdmin):
    pass

class ShippingAdmin(admin.ModelAdmin):
    pass

class CurrencyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ProductMessage, ProductMessageAdmin)
admin.site.register(Shipping, ShippingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(MeasurementType, MeasurementTypeAdmin)
admin.site.register(Product, ProductAdmin)
