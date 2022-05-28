import pytest
from bearboto3.ec2 import (
    EC2Client,
    EC2ServiceResource,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# EC2Client
# ============================


def test_ec2_client_arg_pass(gen_ec2_client):
    @beartype
    def func(param: EC2Client):
        pass

    func(gen_ec2_client)


def test_ec2_client_arg_fail(gen_s3_client):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: EC2Client):
            pass

        func(gen_s3_client)


def test_ec2_client_return_pass(gen_ec2_client):
    @beartype
    def func() -> EC2Client:
        return gen_ec2_client

    func()


def test_ec2_client_return_fail(gen_s3_client):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> EC2Client:
            return gen_s3_client

        func()


# ============================
# EC2ServiceResource
# ============================


def test_ec2_resource_arg_pass(gen_ec2_resource):
    @beartype
    def func(param: EC2ServiceResource):
        pass

    func(gen_ec2_resource)


def test_ec2_resource_arg_fail(gen_s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: EC2ServiceResource):
            pass

        func(gen_s3_resource)


def test_ec2_resource_return_pass(gen_ec2_resource):
    @beartype
    def func() -> EC2ServiceResource:
        return gen_ec2_resource

    func()


def test_ec2_resource_return_fail(gen_s3_resource):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> EC2ServiceResource:
            return gen_s3_resource

        func()
