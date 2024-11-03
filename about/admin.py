from django.contrib import admin

from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Adds rich-text editing of content in admin
    """

    summernote_fields = ("content",)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """

    list_display = (
        "message",
        "read",
    )
