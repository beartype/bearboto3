import pytest
from bearboto3.iam import (
    IAMClient,
    IAMServiceResource,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# IAMClient
# ============================


def test_iam_client_arg_pass(gen_iam_client):
    @beartype
    def func(param: IAMClient):
        pass

    func(gen_iam_client)


def test_iam_client_arg_fail(gen_s3_client):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: IAMClient):
            pass

        func(gen_s3_client)


def test_iam_client_return_pass(gen_iam_client):
    @beartype
    def func() -> IAMClient:
        return gen_iam_client

    func()


def test_iam_client_return_fail(gen_s3_client):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> IAMClient:
            return gen_s3_client

        func()


# ============================
# IAMServiceResource
# ============================


def test_iam_resource_arg_pass(gen_iam_resource):
    @beartype
    def func(param: IAMServiceResource):
        pass

    func(gen_iam_resource)


def test_iam_resource_arg_fail(gen_s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: IAMServiceResource):
            pass

        func(gen_s3_resource)


def test_iam_resource_return_pass(gen_iam_resource):
    @beartype
    def func() -> IAMServiceResource:
        return gen_iam_resource

    func()


def test_iam_resource_return_fail(gen_s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> IAMServiceResource:
            return gen_s3_resource

        func()
