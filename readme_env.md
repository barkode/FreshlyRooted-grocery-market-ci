DEBUG: Controls whether debug mode is on (True) or off (False). Should be False in production.
DEVELOPMENT: Flag to indicate if the environment is development (True) or production (False).
SITE_ID: Specifies the current site for Django's sites framework.
LANGUAGE_CODE: Sets the default language for the project (e.g., en-us for U.S. English).
DJANGO_SECRET_KEY: Secret key used for cryptographic signing, keep this safe and private.
DATABASE_NAME: The name of the project's database.
DATABASE_USER: Username for accessing the database.
DATABASE_PASSWORD: Password for the database user.
DATABASE_HOST: Database server's host address (e.g., localhost or IP address).
DATABASE_PORT: Port number for the database connection (default for PostgreSQL is 5432).
ALLOWED_HOSTS: List of host/domain names that Django can serve (commented out here).
CSRF_TRUSTED_ORIGINS: Trusted domains for CSRF protection (commented out here).
STRIPE_PUBLIC_KEY: Public key for the Stripe payment gateway.
STRIPE_SECRET_KEY: Secret key for the Stripe API (keep private).
STRIPE_WH_SECRET: Secret key for validating Stripe webhooks.
USE_AWS: Flag to indicate if AWS S3 is used for static/media storage.
AWS_STORAGE_BUCKET_NAME: Name of the AWS S3 bucket for storage.
AWS_S3_REGION_NAME: AWS region where the S3 bucket is hosted.
AWS_ACCESS_KEY_ID: AWS access key for authentication.
AWS_SECRET_ACCESS_KEY: AWS secret key for authentication.
EMAIL_HOST: SMTP server address for sending emails.
EMAIL_PORT: Port number for the email server (commonly 587 for TLS).
EMAIL_HOST_USER: Username for the email server.
EMAIL_HOST_PASSWORD: Password for the email server.
DEFAULT_FROM_EMAIL: Default email address used for sending emails from the app.

EXAMPLE:

DEBUG = "True"
DEVELOPMENT = "True"
SITE_ID = "1"
LANGUAGE_CODE = "en-us"
DJANGO_SECRET_KEY = "put django secret key here"
DATABASE_NAME = "put database name here"
DATABASE_USER = "put database username here"
DATABASE_PASSWORD = "put database password here"
DATABASE_HOST = "put database host address here"
DATABASE_PORT = "put database port here"
ALLOWED_HOSTS = ".example1.com;.example2.com"
CSRF_TRUSTED_ORIGINS = "https://*.example1.com;https://*.example2.com"
STRIPE_PUBLIC_KEY = "put stripe public key here"
STRIPE_SECRET_KEY = "put stripe secret key here"
STRIPE_WH_SECRET = "put stripe sh secret here"
USE_AWS = "True"
AWS_STORAGE_BUCKET_NAME = "put aws storage bucket name here"
AWS_S3_REGION_NAME = "put aws s3 region name here"
AWS_ACCESS_KEY_ID = "put aws access key id here"
AWS_SECRET_ACCESS_KEY = "put aws secret access key here"
EMAIL_HOST = "put email smtp host here"
EMAIL_PORT = "put email smtp port here"
EMAIL_HOST_USER = "put email smtp username here"
EMAIL_HOST_PASSWORD = "put email smtp password here"
DEFAULT_FROM_EMAIL = "put email from here"

