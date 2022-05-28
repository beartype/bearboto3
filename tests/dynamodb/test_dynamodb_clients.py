import pytest
from bearboto3.dynamodb import (
    DynamoDBClient,
    DynamoDBServiceResource,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# DynamoDBClient
# ============================


def test_dynamodb_client_arg_pass(gen_dynamodb_client):
    @beartype
    def func(param: DynamoDBClient):
        pass

    func(gen_dynamodb_client)


def test_dynamodb_client_arg_fail(gen_ec2_client):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: DynamoDBClient):
            pass

        func(gen_ec2_client)


def test_dynamodb_client_return_pass(gen_dynamodb_client):
    @beartype
    def func() -> DynamoDBClient:
        return gen_dynamodb_client

    func()


def test_dynamodb_client_return_fail(gen_ec2_client):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DynamoDBClient:
            return gen_ec2_client

        func()


# ============================
# DynamoDBServiceResource
# ============================


def test_dynamodb_resource_arg_pass(gen_dynamodb_resource):
    @beartype
    def func(param: DynamoDBServiceResource):
        pass

    func(gen_dynamodb_resource)


def test_dynamodb_resource_arg_fail(gen_ec2_resource):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: DynamoDBServiceResource):
            pass

        func(gen_ec2_resource)


def test_dynamodb_resource_return_pass(gen_dynamodb_resource):
    @beartype
    def func() -> DynamoDBServiceResource:
        return gen_dynamodb_resource

    func()


def test_dynamodb_resource_return_fail(gen_ec2_resource):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DynamoDBServiceResource:
            return gen_ec2_resource

        func()
