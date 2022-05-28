import pytest
from bearboto3.dynamodb import (
    TableExistsWaiter,
    TableNotExistsWaiter,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# TableExistsWaiter
# ============================


def test_table_exists_arg_pass(gen_table_exists_waiter):
    @beartype
    def func(param: TableExistsWaiter):
        pass

    func(gen_table_exists_waiter)


def test_table_exists_arg_fail(gen_table_not_exists_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: TableExistsWaiter):
            pass

        func(gen_table_not_exists_waiter)


def test_table_exists_return_pass(gen_table_exists_waiter):
    @beartype
    def func() -> TableExistsWaiter:
        return gen_table_exists_waiter

    func()


def test_table_exists_return_fail(gen_table_not_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> TableExistsWaiter:
            return gen_table_not_exists_waiter

        func()


# ============================
# TableNotExistsWaiter
# ============================


def test_table_not_exists_arg_pass(gen_table_not_exists_waiter):
    @beartype
    def func(param: TableNotExistsWaiter):
        pass

    func(gen_table_not_exists_waiter)


def test_table_not_exists_arg_fail(gen_table_exists_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: TableNotExistsWaiter):
            pass

        func(gen_table_exists_waiter)


def test_table_not_exists_return_pass(gen_table_not_exists_waiter):
    @beartype
    def func() -> TableNotExistsWaiter:
        return gen_table_not_exists_waiter

    func()


def test_table_not_exists_return_fail(gen_table_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> TableNotExistsWaiter:
            return gen_table_exists_waiter

        func()
