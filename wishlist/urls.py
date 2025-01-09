from django.urls import path

from . import views

app_name = "wishlist"

urlpatterns = [
    path("", views.view_favorites, name="wishlist"),
    path("add_favorites/<int:product_id>/", views.add_favorites, name="add_favorites"),
    path(
        "remove_favorites/<int:product_id>/",
        views.remove_favorites,
        name="remove_favorites",
    ),
    path(
        "clear_favorites/",
        views.clear_favorites,
        name="clear_favorites",
    ),
]
