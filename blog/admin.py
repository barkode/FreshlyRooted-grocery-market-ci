from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = (
        "status",
        "created_on",
    )
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Comment)
