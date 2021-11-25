import boto3
import os


class S3:
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
        self.aws_access_key_id = aws_access_key_id or os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = aws_secret_access_key or os.getenv("AWS_SECRET_ACCESS_KEY")
        self.region_name = region_name or os.getenv("AWS_REGION_NAME")
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name
        )

    # check if file exists in bucket
    def file_exists(self, bucket, file_name):
        res = self.client.list_objects_v2(Bucket=bucket, Prefix=file_name, MaxKeys=1)
        return 'Contents' in res

    def download(self, bucket, file_name, local_file_path):
        self.client.download_file(bucket, file_name, local_file_path)

    def upload(self, local_file_path, bucket, file_name):
        self.client.uplload_file(local_file_path, bucket, file_name)
