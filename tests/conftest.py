import os

import pytest

from s3.s3_fixtures import *
from utils import random_str

AWS_REGION = "us-east-1"  # Moto requires a valid AWS region


@pytest.fixture
def aws_setup():
    os.environ["AWS_ACCESS_KEY_ID"] = random_str()
    os.environ["AWS_SECRET_ACCESS_KEY"] = random_str()
    os.environ["AWS_DEFAULT_REGION"] = AWS_REGION
