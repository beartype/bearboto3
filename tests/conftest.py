import os

import boto3
import pytest

from s3.s3_fixtures import s3_bucket, s3_client, s3_resource
from utils import random_str

AWS_REGION = "us-east-1"  # Moto requires a valid AWS region

@pytest.fixture
def aws_setup():
    os.putenv("AWS_ACCESS_KEY_ID", random_str())
    os.putenv("AWS_SECRET_ACCESS_KEY", random_str())
    os.putenv("AWS_DEFAULT_REGION", AWS_REGION)
