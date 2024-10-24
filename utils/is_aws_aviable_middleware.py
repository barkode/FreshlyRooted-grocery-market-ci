from django.utils.deprecation import MiddlewareMixin

from utils.is_aws_aviable import is_aws_available
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

class AWSCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not is_aws_available():
            # AWS is unavailable, change the configuration
            INSTALLED_APPS.insert(0,'whitenoise.runserver_nostatic')
            MIDDLEWARE.insert(2, 'whitenoise.middleware.WhiteNoiseMiddleware')
            STORAGES = {
                "default": {
                    "BACKEND": "django.core.files.storage.FileSystemStorage",
                    },
                "staticfiles": {
                    "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
                    }
                }
            STATIC_ROOT = BASE_DIR / 'staticfiles'
            STATIC_URL = '/static/'
            MEDIA_URL = '/media/'
            MEDIA_ROOT = BASE_DIR / 'media'

