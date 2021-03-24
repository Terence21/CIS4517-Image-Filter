import logging
import boto3
from botocore.exceptions import ClientError
import configurations


session = boto3.Session( aws_access_key_id=configurations.ACCESS_KEY, aws_secret_access_key=configurations.SECRET_KEY)
s3_client = session.client('s3')
BUCKET_NAME = "terence-image-filter-bucket"

# upload file to s3 bucket
def upload_file(filename, bucket, object_name=None):
    print('uploading')
    if object_name is None:
        object_name = filename

    try:
        s3_client.upload_file('downloads/' + filename, bucket, object_name)
        print("done uploading")
    except ClientError as e:
        print("error")
        logging.error(e)
        return False
    return True

# download file from s3 bucket
def download_file(filename, bucket):
    s3_client.download_file(BUCKET_NAME, filename, f'downloads/{filename}')
    return f'downloads/{filename}'
