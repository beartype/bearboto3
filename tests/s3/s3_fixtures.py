import boto3
import pytest
from moto import mock_s3
from tests.utils import random_str


@pytest.fixture
def s3_client(aws_setup):
    with mock_s3():
        yield boto3.client('s3')

@pytest.fixture
def s3_resource(aws_setup):
    with mock_s3():
        yield boto3.resource('s3')

@pytest.fixture
def s3_bucket(s3_resource):
    return s3_resource.create_bucket(Bucket=random_str())
