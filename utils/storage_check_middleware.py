import logging
import os
from pathlib import Path

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

from utils.storage_availability import is_aws_available, is_cloudinary_available

logger = logging.getLogger('storage_check')

BASE_DIR = Path(__file__).resolve().parent.parent


class StorageCheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if is_aws_available():
            # AWS Cache parameters
            settings.AWS_S3_OBJECT_PARAMETERS = {
                'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
                'CacheControl': 'max-age=94608000',
                }
            # S3 Configuration
            settings.AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
            settings.AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
            settings.AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
            settings.AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
            settings.AWS_S3_CUSTOM_DOMAIN = f'{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

            # Static and Media files settings
            settings.STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            settings.DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            settings.STATICFILES_DIRECTORY = 'static'
            settings.STATIC_URL = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/static/'
            settings.MEDIAFILES_DIRECTORY = 'media'
            settings.MEDIA_URL = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/media/'

            logger.info('Using AWS to store files')

        elif is_cloudinary_available():
            # Settings for Cloudinary
            settings.CLOUDINARY_STORAGE = {
                'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
                'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
                'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
                }
            settings.DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
            settings.STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
            settings.STATIC_URL = '/static/'
            settings.MEDIA_URL = '/media/'

            logger.info('Using Cloudinary to store files')
        else:
            # Local files with WhiteNoise
            settings.INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')
            settings.MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

            settings.STORAGES = {
                "default": {
                    "BACKEND": "django.core.files.storage.FileSystemStorage",
                    },
                "staticfiles": {
                    "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
                    }
                }

            settings.STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
            settings.DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
            settings.STATIC_ROOT = settings.BASE_DIR / 'staticfiles'
            settings.STATIC_URL = '/static/'
            settings.MEDIA_URL = '/media/'
            settings.MEDIA_ROOT = settings.BASE_DIR / 'media'

            logger.info('Switching to local files via WhiteNoise')
