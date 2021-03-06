import pytest
from bearboto3.lambda_ import (
    LambdaClient,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# LambdaClient
# ============================


def test_lambda_client_arg_pass(gen_lambda_client):
    @beartype
    def func(param: LambdaClient):
        pass

    func(gen_lambda_client)


def test_lambda_client_arg_fail(gen_s3_client):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: LambdaClient):
            pass

        func(gen_s3_client)


def test_lambda_client_return_pass(gen_lambda_client):
    @beartype
    def func() -> LambdaClient:
        return gen_lambda_client

    func()


def test_lambda_client_return_fail(gen_s3_client):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> LambdaClient:
            return gen_s3_client

        func()
