import logging
import boto3
from botocore.exceptions import ClientError
import configurations


session = boto3.Session( aws_access_key_id=configurations.ACCESS_KEY, aws_secret_access_key=configurations.SECRET_KEY)
s3_client = session.client('s3')

BUCKET_NAME = "terence-image-filter-bucket"


def upload_file(filename, bucket, object_name=None):
    if object_name is None:
        object_name = filename

    try:
        response = s3_client.upload_file('uploads/' + filename, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(filename, bucket):

    s3_client.download_file(BUCKET_NAME, filename, f'uploads/{filename}')
    return f'uploads/{filename}'
