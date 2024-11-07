from django.urls import path
from . import views

app_name = "about"

urlpatterns = [
    path("contact/", views.about_contact, name="contact"),
    path("privacy/", views.about_privacy_policy, name="privacy"),
    path("return/", views.about_return_policy, name="return"),
    path("", views.about_us, name="about"),
]
