from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.all_products, name="products"),
    path("search/", views.all_products, name="products_search"),
    path("<int:product_id>", views.product_detail, name="product_detail"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
]
