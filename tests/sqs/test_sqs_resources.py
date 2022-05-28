import pytest
from bearboto3.sqs import (
    Message,
    Queue,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# Message
# ============================


def test_message_arg_pass(gen_message):
    @beartype
    def func(param: Message):
        pass

    func(gen_message)


def test_message_arg_fail(gen_queue):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: Message):
            pass

        func(gen_queue)


def test_message_return_pass(gen_message):
    @beartype
    def func() -> Message:
        return gen_message

    func()


def test_message_return_fail(gen_queue):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Message:
            return gen_queue

        func()


# ============================
# Queue
# ============================


def test_queue_arg_pass(gen_queue):
    @beartype
    def func(param: Queue):
        pass

    func(gen_queue)


def test_queue_arg_fail(gen_message):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: Queue):
            pass

        func(gen_message)


def test_queue_return_pass(gen_queue):
    @beartype
    def func() -> Queue:
        return gen_queue

    func()


def test_queue_return_fail(gen_message):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Queue:
            return gen_message

        func()
