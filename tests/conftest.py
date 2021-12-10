import os

import pytest

import utils
from dynamodb.dynamodb_fixtures import *
from ec2.ec2_fixtures import *
from lambda_.lambda_fixtures import *
from s3.s3_fixtures import *

AWS_REGION = "us-east-1"  # Moto requires a valid AWS region


@pytest.fixture
def aws_setup():
    os.environ["AWS_ACCESS_KEY_ID"] = utils.random_str()
    os.environ["AWS_SECRET_ACCESS_KEY"] = utils.random_str()
    os.environ["AWS_DEFAULT_REGION"] = AWS_REGION
