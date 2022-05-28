import pytest
from bearboto3.s3 import (
    S3Client,
    S3ServiceResource,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# S3Client
# ============================


def test_s3_client_arg_pass(gen_s3_client):
    @beartype
    def func(param: S3Client):
        pass

    func(gen_s3_client)


def test_s3_client_arg_fail(gen_ec2_client):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: S3Client):
            pass

        func(gen_ec2_client)


def test_s3_client_return_pass(gen_s3_client):
    @beartype
    def func() -> S3Client:
        return gen_s3_client

    func()


def test_s3_client_return_fail(gen_ec2_client):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> S3Client:
            return gen_ec2_client

        func()


# ============================
# S3ServiceResource
# ============================


def test_s3_resource_arg_pass(gen_s3_resource):
    @beartype
    def func(param: S3ServiceResource):
        pass

    func(gen_s3_resource)


def test_s3_resource_arg_fail(gen_ec2_resource):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: S3ServiceResource):
            pass

        func(gen_ec2_resource)


def test_s3_resource_return_pass(gen_s3_resource):
    @beartype
    def func() -> S3ServiceResource:
        return gen_s3_resource

    func()


def test_s3_resource_return_fail(gen_ec2_resource):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> S3ServiceResource:
            return gen_ec2_resource

        func()
