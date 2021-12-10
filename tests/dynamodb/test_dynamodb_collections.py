import pytest
from bearboto3.dynamodb import ServiceResourceTablesCollection
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)

# ============================
# ServiceResourceTablesCollection
# ============================


def test_tables_arg_pass(gen_service_resource_tables_collection):
    @beartype
    def func(param: ServiceResourceTablesCollection):
        pass

    func(gen_service_resource_tables_collection)


def test_tables_arg_fail(gen_service_resource_buckets_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceTablesCollection):
            pass

        func(gen_service_resource_buckets_collection)


def test_tables_return_pass(gen_service_resource_tables_collection):
    @beartype
    def func() -> ServiceResourceTablesCollection:
        return gen_service_resource_tables_collection

    func()


def test_tables_return_fail(gen_service_resource_buckets_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceTablesCollection:
            return gen_service_resource_buckets_collection

        func()
