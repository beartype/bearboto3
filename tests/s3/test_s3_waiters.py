import pytest
from bearboto3.s3 import (
    BucketExistsWaiter,
    BucketNotExistsWaiter,
    ObjectExistsWaiter,
    ObjectNotExistsWaiter,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# BucketExistsWaiter
# ============================


def test_bucket_exists_arg_pass(gen_bucket_exists_waiter):
    @beartype
    def func(param: BucketExistsWaiter):
        pass

    func(gen_bucket_exists_waiter)


def test_bucket_exists_arg_fail(gen_object_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketExistsWaiter):
            pass

        func(gen_object_exists_waiter)


def test_bucket_exists_return_pass(gen_bucket_exists_waiter):
    @beartype
    def func() -> BucketExistsWaiter:
        return gen_bucket_exists_waiter

    func()


def test_bucket_exists_return_fail(gen_object_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketExistsWaiter:
            return gen_object_exists_waiter

        func()


# ============================
# BucketNotExistsWaiter
# ============================


def test_bucket_not_exists_arg_pass(gen_bucket_not_exists_waiter):
    @beartype
    def func(param: BucketNotExistsWaiter):
        pass

    func(gen_bucket_not_exists_waiter)


def test_bucket_not_exists_arg_fail(gen_object_not_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketNotExistsWaiter):
            pass

        func(gen_object_not_exists_waiter)


def test_bucket_not_exists_return_pass(gen_bucket_not_exists_waiter):
    @beartype
    def func() -> BucketNotExistsWaiter:
        return gen_bucket_not_exists_waiter

    func()


def test_bucket_not_exists_return_fail(gen_object_not_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketNotExistsWaiter:
            return gen_object_not_exists_waiter

        func()


# ============================
# ObjectExistsWaiter
# ============================


def test_object_exists_arg_pass(gen_object_exists_waiter):
    @beartype
    def func(param: ObjectExistsWaiter):
        pass

    func(gen_object_exists_waiter)


def test_object_exists_arg_fail(gen_bucket_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ObjectExistsWaiter):
            pass

        func(gen_bucket_exists_waiter)


def test_object_exists_return_pass(gen_object_exists_waiter):
    @beartype
    def func() -> ObjectExistsWaiter:
        return gen_object_exists_waiter

    func()


def test_object_exists_return_fail(gen_bucket_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectExistsWaiter:
            return gen_bucket_exists_waiter

        func()


# ============================
# ObjectNotExistsWaiter
# ============================


def test_object_not_exists_arg_pass(gen_object_not_exists_waiter):
    @beartype
    def func(param: ObjectNotExistsWaiter):
        pass

    func(gen_object_not_exists_waiter)


def test_object_not_exists_arg_fail(gen_bucket_not_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ObjectNotExistsWaiter):
            pass

        func(gen_bucket_not_exists_waiter)


def test_object_not_exists_return_pass(gen_object_not_exists_waiter):
    @beartype
    def func() -> ObjectNotExistsWaiter:
        return gen_object_not_exists_waiter

    func()


def test_object_not_exists_return_fail(gen_bucket_not_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectNotExistsWaiter:
            return gen_bucket_not_exists_waiter

        func()
