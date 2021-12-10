import pytest
from bearboto3.lambda_ import (
    FunctionExistsWaiter,
    FunctionActiveWaiter,
    FunctionUpdatedWaiter,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# FunctionExistsWaiter
# ============================


def test_function_exists_arg_pass(gen_function_exists_waiter):
    @beartype
    def func(param: FunctionExistsWaiter):
        pass

    func(gen_function_exists_waiter)


def test_function_exists_arg_fail(gen_function_updated_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: FunctionExistsWaiter):
            pass

        func(gen_function_updated_waiter)


def test_function_exists_return_pass(gen_function_exists_waiter):
    @beartype
    def func() -> FunctionExistsWaiter:
        return gen_function_exists_waiter

    func()


def test_function_exists_return_fail(gen_function_updated_waiter):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> FunctionExistsWaiter:
            return gen_function_updated_waiter

        func()


# ============================
# FunctionActiveWaiter
# ============================


def test_function_active_arg_pass(gen_function_active_waiter):
    @beartype
    def func(param: FunctionActiveWaiter):
        pass

    func(gen_function_active_waiter)


def test_function_active_arg_fail(gen_function_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: FunctionActiveWaiter):
            pass

        func(gen_function_exists_waiter)


def test_function_active_return_pass(gen_function_active_waiter):
    @beartype
    def func() -> FunctionActiveWaiter:
        return gen_function_active_waiter

    func()


def test_function_active_return_fail(gen_function_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> FunctionActiveWaiter:
            return gen_function_exists_waiter

        func()


# ============================
# FunctionUpdatedWaiter
# ============================


def test_function_updated_arg_pass(gen_function_updated_waiter):
    @beartype
    def func(param: FunctionUpdatedWaiter):
        pass

    func(gen_function_updated_waiter)


def test_function_updated_arg_fail(gen_function_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: FunctionUpdatedWaiter):
            pass

        func(gen_function_exists_waiter)


def test_function_updated_return_pass(gen_function_updated_waiter):
    @beartype
    def func() -> FunctionUpdatedWaiter:
        return gen_function_updated_waiter

    func()


def test_function_updated_return_fail(gen_function_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> FunctionUpdatedWaiter:
            return gen_function_exists_waiter

        func()
