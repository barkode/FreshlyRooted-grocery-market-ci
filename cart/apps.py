from django.apps import AppConfig

# Creating a configuration class for the 'cart' app
class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
