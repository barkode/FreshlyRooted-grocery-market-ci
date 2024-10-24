import logging
import os

import boto3
from botocore.exceptions import EndpointConnectionError, NoCredentialsError

# Get logger
logger = logging.getLogger('aws_check')


def is_aws_available():
    try:
        # Try to create S3 client and connect with AWS S3
        s3 = boto3.client('s3',
                          aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                          region_name=os.environ.get('AWS_S3_REGION_NAME')
                          )
        # Trying to get a list of buckets as a test request
        s3.list_buckets()
        logger.info('AWS available')  # Logging a successful connection
        return True
    except (NoCredentialsError, EndpointConnectionError) as e:
        logger.error(f'AWS inaccessible: {str(e)}')  # Logging the error and the reason for unavailability
        return False
