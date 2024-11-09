from django.contrib import admin

from .models import About, CollaborateRequest


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """

    list_display = (
        "message",
        "read",
    )


admin.site.register(About)
