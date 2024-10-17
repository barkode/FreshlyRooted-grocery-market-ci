DJ_SECRET_KEY: The secret key for Django, used to ensure the security of the application. This should be a unique and random string of a significant length.
DEBUG: Debug option. Can be set to "True" or "False". The default value is "False". Setting it to "True" will enable the debugging mode, which is not recommended for production environments.

#PostgreSQL credentials
DB_NAME: Name of the PostgreSQL database.
DB_USER: Username to connect to the database.
DB_PASSWORD: Password for the database user.
DB_HOST: Host where the database resides.
DB_PORT: Port on which the database server is running.

# Github authorization
SOCIAL_AUTH_GITHUB_KEY: Client key for GitHub OAuth authorization.
SOCIAL_AUTH_GITHUB_SECRET: Client secret key for GitHub OAuth authorization.

# Cloudinary credentials
CLOUD_NAME: Name of the cloud in Cloudinary.
CLOUD_API_KEY: Cloudinary API key.
CLOUD_API_SECRET: Cloudinary secret API key.

# AWS credentials

# Stripe credentials