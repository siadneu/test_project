import boto3
import os


class S3:
    def __init__(self, region_name=None):
        self.region_name = region_name or os.getenv("AWS_REGION_NAME")
        self.client = boto3.client(
            's3',
            region_name=self.region_name
        )

    # check if file exists in bucket
    def file_exists(self, bucket, file_name):
        res = self.client.list_objects_v2(Bucket=bucket, Prefix=file_name, MaxKeys=1)
        return 'Contents' in res

    def download(self, bucket, file_name, local_file_path):
        self.client.download_file(bucket, file_name, local_file_path)

    def upload(self, local_file_path, bucket, file_name):
        self.client.upload_file(local_file_path, bucket, file_name)
