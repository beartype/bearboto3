import pytest
from bearboto3.sns import (
    SNSClient,
    SNSServiceResource,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# SNSClient
# ============================


def test_sns_client_arg_pass(gen_sns_client):
    @beartype
    def func(param: SNSClient):
        pass

    func(gen_sns_client)


def test_sns_client_arg_fail(gen_ec2_client):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SNSClient):
            pass

        func(gen_ec2_client)


def test_sns_client_return_pass(gen_sns_client):
    @beartype
    def func() -> SNSClient:
        return gen_sns_client

    func()


def test_sns_client_return_fail(gen_ec2_client):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SNSClient:
            return gen_ec2_client

        func()


# ============================
# SNSServiceResource
# ============================


def test_sns_resource_arg_pass(gen_sns_resource):
    @beartype
    def func(param: SNSServiceResource):
        pass

    func(gen_sns_resource)


def test_sns_resource_arg_fail(gen_ec2_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SNSServiceResource):
            pass

        func(gen_ec2_resource)


def test_sns_resource_return_pass(gen_sns_resource):
    @beartype
    def func() -> SNSServiceResource:
        return gen_sns_resource

    func()


def test_sns_resource_return_fail(gen_ec2_resource):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SNSServiceResource:
            return gen_ec2_resource

        func()
