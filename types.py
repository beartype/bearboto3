from typing import Annotated
from beartype.vale import Is
from mypy_boto3_s3.service_resource import Bucket

S3Bucket = Annotated[object, lambda obj: obj.__class__.__name__ == "s3.Bucket"]
