import pytest
from bearboto3.dynamodb import Table
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)

# ============================
# Table
# ============================


def test_table_arg_pass(gen_table):
    @beartype
    def func(param: Table):
        pass

    func(gen_table)


def test_table_arg_fail(gen_bucket):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Table):
            pass

        func(gen_bucket)


def test_table_return_pass(gen_table):
    @beartype
    def func() -> Table:
        return gen_table

    func()


def test_table_return_fail(gen_bucket):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Table:
            return gen_bucket

        func()
