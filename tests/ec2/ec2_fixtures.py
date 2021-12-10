import boto3
import pytest
from moto import mock_ec2
from tests.utils import random_str


@pytest.fixture
def gen_ec2_client(aws_setup):
    with mock_ec2():
        yield boto3.client("ec2")


@pytest.fixture
def gen_ec2_resource(aws_setup):
    with mock_ec2():
        yield boto3.resource("ec2")
