from beartype import beartype
import boto3
from mypy_boto3_s3.service_resource import S3ServiceResource, Bucket

@beartype
def example(s3: S3ServiceResource) -> Bucket:
    return s3.Bucket('example')

if __name__ == "__main__":
    s3 = boto3.resource('s3')
    bucket = example(s3)