import boto3
import pytest
from moto import mock_lambda


@pytest.fixture
def gen_lambda_client(aws_setup):
    with mock_lambda():
        yield boto3.client("lambda")


# ============================
# WAITER
# ============================


@pytest.fixture
def gen_function_exists_waiter(gen_lambda_client):
    return gen_lambda_client.get_waiter("function_exists")


@pytest.fixture
def gen_function_active_waiter(gen_lambda_client):
    return gen_lambda_client.get_waiter("function_active")


@pytest.fixture
def gen_function_updated_waiter(gen_lambda_client):
    return gen_lambda_client.get_waiter("function_updated")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_list_event_source_mappings_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_event_source_mappings")


@pytest.fixture
def gen_list_functions_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_functions")


@pytest.fixture
def gen_list_aliases_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_aliases")


@pytest.fixture
def gen_list_layer_versions_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_layer_versions")


@pytest.fixture
def gen_list_layers_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_layers")


@pytest.fixture
def gen_list_versions_by_function_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_versions_by_function")


@pytest.fixture
def gen_list_function_event_invoke_configs_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_function_event_invoke_configs")


@pytest.fixture
def gen_list_provisioned_concurrency_configs_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_provisioned_concurrency_configs")


@pytest.fixture
def gen_list_code_signing_configs_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_code_signing_configs")


@pytest.fixture
def gen_list_functions_by_code_signing_config_paginator(gen_lambda_client):
    return gen_lambda_client.get_paginator("list_functions_by_code_signing_config")
