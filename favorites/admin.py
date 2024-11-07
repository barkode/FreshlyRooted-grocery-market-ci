from django.contrib import admin
from .models import Favorites


# Define the admin configuration for the Favorites model

class FavoritesAdmin(admin.ModelAdmin):

	search_fields = [
		"user",
		]

	filter_horizontal = ("products",)
	list_display = (
		"user",
		"date_added",
		)

	ordering = ("user",)


# Register the Favorites model with its corresponding admin configuration
admin.site.register(Favorites, FavoritesAdmin)