import logging
import os
import requests
import boto3
from botocore.exceptions import EndpointConnectionError, NoCredentialsError, ClientError

# Get logger
logger = logging.getLogger('aws_check')


def is_aws_available():
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                          region_name=os.getenv('AWS_S3_REGION_NAME')
                          )
        s3.list_buckets()
        logger.info('AWS available')
        return True
    except (NoCredentialsError, EndpointConnectionError):
        logger.error('AWS unavailable')
        return False
    except ClientError as e:
        if e.response['Error']['Code'] == 'ThrottlingException':
            # Over Limit Handling
            return False
        else:
            raise e

def is_cloudinary_available():
    try:
        # Trying access to Cloudinary API
        response = requests.get(f'https://api.cloudinary.com/v1_1/{os.getenv("CLOUDINARY_CLOUD_NAME")}/ping')
        if response.status_code == 200:
            logger.info('Cloudinary is available')
            return True
        else:
            logger.error('Cloudinary is not available')
            return False
    except requests.RequestException:
        logger.error('Error connecting to Cloudinary')
        return False
