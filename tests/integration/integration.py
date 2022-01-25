import boto3
from bearboto3.s3 import Bucket


def test_bucket(bucket: Bucket):
    pass

s3 = boto3.resource('s3')

test_bucket(s3.Bucket('foo'))
