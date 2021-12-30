import pytest
from bearboto3.sqs import (
    ServiceResourceQueuesCollection,
    QueueDeadLetterSourceQueuesCollection,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ServiceResourceQueuesCollection
# ============================


def test_queues_arg_pass(gen_service_resource_queues_collection):
    @beartype
    def func(param: ServiceResourceQueuesCollection):
        pass

    func(gen_service_resource_queues_collection)


def test_queues_arg_fail(gen_queue_dead_letter_source_queues_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceQueuesCollection):
            pass

        func(gen_queue_dead_letter_source_queues_collection)


def test_queues_return_pass(gen_service_resource_queues_collection):
    @beartype
    def func() -> ServiceResourceQueuesCollection:
        return gen_service_resource_queues_collection

    func()


def test_queues_return_fail(gen_queue_dead_letter_source_queues_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceQueuesCollection:
            return gen_queue_dead_letter_source_queues_collection

        func()


# ============================
# QueueDeadLetterSourceQueuesCollection
# ============================


def test_dead_letter_source_queues_arg_pass(
    gen_queue_dead_letter_source_queues_collection,
):
    @beartype
    def func(param: QueueDeadLetterSourceQueuesCollection):
        pass

    func(gen_queue_dead_letter_source_queues_collection)


def test_dead_letter_source_queues_arg_fail(gen_service_resource_queues_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: QueueDeadLetterSourceQueuesCollection):
            pass

        func(gen_service_resource_queues_collection)


def test_dead_letter_source_queues_return_pass(
    gen_queue_dead_letter_source_queues_collection,
):
    @beartype
    def func() -> QueueDeadLetterSourceQueuesCollection:
        return gen_queue_dead_letter_source_queues_collection

    func()


def test_dead_letter_source_queues_return_fail(gen_service_resource_queues_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> QueueDeadLetterSourceQueuesCollection:
            return gen_service_resource_queues_collection

        func()
