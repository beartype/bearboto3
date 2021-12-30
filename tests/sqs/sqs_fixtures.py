import boto3
import pytest
from moto import mock_sqs
from tests.utils import random_str


@pytest.fixture
def gen_sqs_client(aws_setup):
    with mock_sqs():
        yield boto3.client("sqs")


@pytest.fixture
def gen_sqs_resource(aws_setup):
    with mock_sqs():
        yield boto3.resource("sqs")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_list_dead_letter_source_queues_paginator(gen_sqs_client):
    return gen_sqs_client.get_paginator("list_dead_letter_source_queues")


@pytest.fixture
def gen_list_queues_paginator(gen_sqs_client):
    return gen_sqs_client.get_paginator("list_queues")


# ============================
# RESOURCES
# ============================


@pytest.fixture
def gen_message(gen_sqs_resource):
    return gen_sqs_resource.Message(random_str(), random_str())


@pytest.fixture
def gen_queue(gen_sqs_resource):
    return gen_sqs_resource.Queue(random_str())


# ============================
# COLLECTIONS
# ============================


@pytest.fixture
def gen_service_resource_queues_collection(gen_sqs_resource):
    return gen_sqs_resource.queues.all()


@pytest.fixture
def gen_queue_dead_letter_source_queues_collection(gen_queue):
    return gen_queue.dead_letter_source_queues.all()
