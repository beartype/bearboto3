import boto3
import pytest
from moto import mock_sns
from tests.utils import random_str


@pytest.fixture
def gen_sns_client(aws_setup):
    with mock_sns():
        yield boto3.client("sns")


@pytest.fixture
def gen_sns_resource(aws_setup):
    with mock_sns():
        yield boto3.resource("sns")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_list_endpoints_by_platform_application_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_endpoints_by_platform_application")


@pytest.fixture
def gen_list_platform_applications_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_platform_applications")


@pytest.fixture
def gen_list_subscriptions_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_subscriptions")


@pytest.fixture
def gen_list_subscriptions_by_topic_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_subscriptions_by_topic")


@pytest.fixture
def gen_list_topics_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_topics")


@pytest.fixture
def gen_list_phone_numbers_opted_out_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_phone_numbers_opted_out")


@pytest.fixture
def gen_list_origination_numbers_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_origination_numbers")


@pytest.fixture
def gen_list_sms_sandbox_phone_numbers_paginator(gen_sns_client):
    return gen_sns_client.get_paginator("list_sms_sandbox_phone_numbers")


# ============================
# RESOURCES
# ============================


@pytest.fixture
def gen_platform_application(gen_sns_resource):
    return gen_sns_resource.PlatformApplication(random_str())


@pytest.fixture
def gen_platform_endpoint(gen_sns_resource):
    return gen_sns_resource.PlatformEndpoint(random_str())


@pytest.fixture
def gen_subscription(gen_sns_resource):
    return gen_sns_resource.Subscription(random_str())


@pytest.fixture
def gen_topic(gen_sns_resource):
    return gen_sns_resource.Topic(random_str())


# ============================
# COLLECTIONS
# ============================


@pytest.fixture
def gen_service_resource_platform_applications_collection(gen_sns_resource):
    return gen_sns_resource.platform_applications.all()


@pytest.fixture
def gen_service_resource_subscriptions_collection(gen_sns_resource):
    return gen_sns_resource.subscriptions.all()


@pytest.fixture
def gen_service_resource_topics_collection(gen_sns_resource):
    return gen_sns_resource.topics.all()


@pytest.fixture
def gen_platform_application_endpoints_collection(gen_platform_application):
    return gen_platform_application.endpoints.all()


@pytest.fixture
def gen_topic_subscriptions_collection(gen_topic):
    return gen_topic.subscriptions.all()
