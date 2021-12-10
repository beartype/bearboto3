import boto3
import pytest
from moto import mock_dynamodb2
from tests.utils import random_str


@pytest.fixture
def gen_dynamodb_client(aws_setup):
    with mock_dynamodb2():
        yield boto3.client("dynamodb")


@pytest.fixture
def gen_dynamodb_resource(aws_setup):
    with mock_dynamodb2():
        yield boto3.resource("dynamodb")


# ============================
# WAITER
# ============================


@pytest.fixture
def gen_table_exists_waiter(gen_dynamodb_client):
    return gen_dynamodb_client.get_waiter("table_exists")


@pytest.fixture
def gen_table_not_exists_waiter(gen_dynamodb_client):
    return gen_dynamodb_client.get_waiter("table_not_exists")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_list_backups_paginator(gen_dynamodb_client):
    return gen_dynamodb_client.get_paginator("list_backups")


@pytest.fixture
def gen_list_tables_paginator(gen_dynamodb_client):
    return gen_dynamodb_client.get_paginator("list_tables")


@pytest.fixture
def gen_query_paginator(gen_dynamodb_client):
    return gen_dynamodb_client.get_paginator("query")


@pytest.fixture
def gen_scan_paginator(gen_dynamodb_client):
    return gen_dynamodb_client.get_paginator("scan")


@pytest.fixture
def gen_list_tags_of_resource_paginator(gen_dynamodb_client):
    return gen_dynamodb_client.get_paginator("list_tags_of_resource")


# ============================
# RESOURCES
# ============================


@pytest.fixture
def gen_table(gen_dynamodb_resource):
    return gen_dynamodb_resource.Table(random_str())


# ============================
# COLLECTIONS
# ============================


@pytest.fixture
def gen_service_resource_tables_collection(gen_dynamodb_resource):
    return gen_dynamodb_resource.tables.all()
