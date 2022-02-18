import uuid

import boto3
from bearboto3.s3 import Bucket, Object


def random_str():
    return str(uuid.uuid4())


def integration(bucket: Bucket) -> Object:
    return bucket.Object(random_str())


s3 = boto3.resource("s3")
obj = integration(s3.Bucket(random_str()))
