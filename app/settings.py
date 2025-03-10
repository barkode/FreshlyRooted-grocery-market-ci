"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from os import getenv
from pathlib import Path

from dotenv import load_dotenv

# Take environment variables from .env.
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", "False").lower() == "true"

# DEVELOPMENT Settings
DEVELOPMENT = getenv("DEVELOPMENT", "False").lower() == "true"

# LOGING variable. Default "False"
IS_LOGGING = getenv("IS_LOGGING", "False").lower() == "true"

# Use external storage parameter default "False"
USE_STORAGE = getenv("USE_STORAGE", "False").lower() == "true"

# Use external database default "False"
USE_DATABASE = getenv("USE_DATABASE", "False").lower() == "true"

# Site ID default 1
SITE_ID = int(getenv("SITE_ID", "1"))

if DEVELOPMENT:
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
    ]
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost",
        "http://127.0.0.1",
    ]
    # Email settings
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "freshlyrooted@example.com"
else:
    ALLOWED_HOSTS = list(getenv("ALLOWED_HOSTS").split(";"))
    CSRF_TRUSTED_ORIGINS = list(getenv("CSRF_TRUSTED_ORIGINS").split(";"))
    # Email settings
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = int(getenv("EMAIL_PORT", "587"))
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD")
    DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "crispy_bootstrap5",
    "crispy_bootstrap4",
    "crispy_tailwind",
    "django_summernote",
    "storages",
    "cookie_consent",
    "home",
    "products",
    "bag",
    # "blog",
    # "about",
    "checkout",
    "profiles",
    "wishlist",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "app.urls"

CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = ["bootstrap4", "bootstrap5", "tailwind"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "templates/allauth",
            BASE_DIR / "home/templates/home",
            BASE_DIR / "products/templates/products",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.messages.context_processors.messages",
                "bag.contexts.bag_contents",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
            "libraries": {
                "bag_tags": "bag.templatetags.bag_tools",
            },
        },
    },
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

WSGI_APPLICATION = "app.wsgi.application"

ACCOUNT_LOGIN_METHODS = {"username", "email"}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none" if DEVELOPMENT else "mandatory"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if USE_DATABASE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": getenv("DATABASE_NAME"),
            "USER": getenv("DATABASE_USER"),
            "PASSWORD": getenv("DATABASE_PASSWORD"),
            "HOST": getenv("DATABASE_HOST"),
            "PORT": int(getenv("DATABASE_PORT", "5432")),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = getenv("LANGUAGE_CODE", "en-us")

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (BASE_DIR / "static",)
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AWS and white settings
if USE_STORAGE:
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    # S3 Configuration
    AWS_STORAGE_BUCKET_NAME = getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = getenv("AWS_S3_REGION_NAME")
    AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Static and Media files settings
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_DIRECTORY = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_DIRECTORY = "media"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_DIRECTORY}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_DIRECTORY}/"

# Stripe settings
FREE_DELIVERY_THRESHOLD = 75
STANDARD_DELIVERY_PERCENTAGE = 12
STRIPE_CURRENCY = "eur"
STRIPE_PUBLIC_KEY = getenv("STRIPE_PUBLIC_KEY", None)
STRIPE_SECRET_KEY = getenv("STRIPE_SECRET_KEY", None)
STRIPE_WH_SECRET = getenv("STRIPE_WH_SECRET", None)
