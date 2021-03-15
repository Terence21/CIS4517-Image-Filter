import logging
import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "terence-image-filter-bucket"
def upload_file(filename, bucket, object_name=None):
    if object_name is None:
        object_name = filename

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(filename, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(filename, bucket):
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, f"download/{filename}")
    return f"download/{filename}"

