import os

import pytest

from utils import random_str

AWS_REGION = "us-east-1"  # Moto requires a valid AWS region

@pytest.fixture
def aws_setup():
    os.putenv("AWS_ACCESS_KEY_ID", random_str())
    os.putenv("AWS_SECRET_ACCESS_KEY", random_str())
    os.putenv("AWS_DEFAULT_REGION", AWS_REGION)
