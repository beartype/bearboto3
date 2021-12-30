import pytest
from bearboto3.sqs import (
    SQSClient,
    SQSServiceResource,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# SQSClient
# ============================


def test_sqs_client_arg_pass(gen_sqs_client):
    @beartype
    def func(param: SQSClient):
        pass

    func(gen_sqs_client)


def test_sqs_client_arg_fail(gen_s3_client):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SQSClient):
            pass

        func(gen_s3_client)


def test_sqs_client_return_pass(gen_sqs_client):
    @beartype
    def func() -> SQSClient:
        return gen_sqs_client

    func()


def test_sqs_client_return_fail(gen_s3_client):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SQSClient:
            return gen_s3_client

        func()


# ============================
# SQSServiceResource
# ============================


def test_sqs_resource_arg_pass(gen_sqs_resource):
    @beartype
    def func(param: SQSServiceResource):
        pass

    func(gen_sqs_resource)


def test_sqs_resource_arg_fail(gen_s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SQSServiceResource):
            pass

        func(gen_s3_resource)


def test_sqs_resource_return_pass(gen_sqs_resource):
    @beartype
    def func() -> SQSServiceResource:
        return gen_sqs_resource

    func()


def test_sqs_resource_return_fail(gen_s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SQSServiceResource:
            return gen_s3_resource

        func()
