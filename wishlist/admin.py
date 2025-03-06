from django.contrib import admin
from .models import Wishlist


# Define the admin configuration for the Wishlist model
class WishlistAdmin(admin.ModelAdmin):

    search_fields = [
        "user",
    ]

    filter_horizontal = ("products",)
    list_display = (
        "user",
        "date_added",
    )

    ordering = ("user",)


# Register the Wishlist model with its corresponding admin configuration
admin.site.register(Wishlist, WishlistAdmin)
