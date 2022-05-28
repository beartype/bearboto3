import pytest
from bearboto3.sqs import (
    ListDeadLetterSourceQueuesPaginator,
    ListQueuesPaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ListDeadLetterSourceQueuesPaginator
# ============================


def test_list_dead_letter_source_queues_arg_pass(
    gen_list_dead_letter_source_queues_paginator,
):
    @beartype
    def func(param: ListDeadLetterSourceQueuesPaginator):
        pass

    func(gen_list_dead_letter_source_queues_paginator)


def test_list_dead_letter_source_queues_arg_fail(gen_list_queues_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListDeadLetterSourceQueuesPaginator):
            pass

        func(gen_list_queues_paginator)


def test_list_dead_letter_source_queues_return_pass(
    gen_list_dead_letter_source_queues_paginator,
):
    @beartype
    def func() -> ListDeadLetterSourceQueuesPaginator:
        return gen_list_dead_letter_source_queues_paginator

    func()


def test_list_dead_letter_source_queues_return_fail(gen_list_queues_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListDeadLetterSourceQueuesPaginator:
            return gen_list_queues_paginator

        func()


# ============================
# ListQueuesPaginator
# ============================


def test_list_queues_arg_pass(gen_list_queues_paginator):
    @beartype
    def func(param: ListQueuesPaginator):
        pass

    func(gen_list_queues_paginator)


def test_list_queues_arg_fail(gen_list_dead_letter_source_queues_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListQueuesPaginator):
            pass

        func(gen_list_dead_letter_source_queues_paginator)


def test_list_queues_return_pass(gen_list_queues_paginator):
    @beartype
    def func() -> ListQueuesPaginator:
        return gen_list_queues_paginator

    func()


def test_list_queues_return_fail(gen_list_dead_letter_source_queues_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListQueuesPaginator:
            return gen_list_dead_letter_source_queues_paginator

        func()
