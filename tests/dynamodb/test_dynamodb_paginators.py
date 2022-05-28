import pytest
from bearboto3.dynamodb import (
    ListBackupsPaginator,
    ListTablesPaginator,
    QueryPaginator,
    ScanPaginator,
    ListTagsOfResourcePaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ListBackupsPaginator
# ============================


def test_list_backups_arg_pass(gen_list_backups_paginator):
    @beartype
    def func(param: ListBackupsPaginator):
        pass

    func(gen_list_backups_paginator)


def test_list_backups_arg_fail(gen_list_tags_of_resource_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListBackupsPaginator):
            pass

        func(gen_list_tags_of_resource_paginator)


def test_list_backups_return_pass(gen_list_backups_paginator):
    @beartype
    def func() -> ListBackupsPaginator:
        return gen_list_backups_paginator

    func()


def test_list_backups_return_fail(gen_list_tags_of_resource_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListBackupsPaginator:
            return gen_list_tags_of_resource_paginator

        func()


# ============================
# ListTablesPaginator
# ============================


def test_list_tables_arg_pass(gen_list_tables_paginator):
    @beartype
    def func(param: ListTablesPaginator):
        pass

    func(gen_list_tables_paginator)


def test_list_tables_arg_fail(gen_list_backups_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListTablesPaginator):
            pass

        func(gen_list_backups_paginator)


def test_list_tables_return_pass(gen_list_tables_paginator):
    @beartype
    def func() -> ListTablesPaginator:
        return gen_list_tables_paginator

    func()


def test_list_tables_return_fail(gen_list_backups_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListTablesPaginator:
            return gen_list_backups_paginator

        func()


# ============================
# QueryPaginator
# ============================


def test_query_arg_pass(gen_query_paginator):
    @beartype
    def func(param: QueryPaginator):
        pass

    func(gen_query_paginator)


def test_query_arg_fail(gen_scan_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: QueryPaginator):
            pass

        func(gen_scan_paginator)


def test_query_return_pass(gen_query_paginator):
    @beartype
    def func() -> QueryPaginator:
        return gen_query_paginator

    func()


def test_query_return_fail(gen_scan_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> QueryPaginator:
            return gen_scan_paginator

        func()


# ============================
# ScanPaginator
# ============================


def test_scan_arg_pass(gen_scan_paginator):
    @beartype
    def func(param: ScanPaginator):
        pass

    func(gen_scan_paginator)


def test_scan_arg_fail(gen_query_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ScanPaginator):
            pass

        func(gen_query_paginator)


def test_scan_return_pass(gen_scan_paginator):
    @beartype
    def func() -> ScanPaginator:
        return gen_scan_paginator

    func()


def test_scan_return_fail(gen_query_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ScanPaginator:
            return gen_query_paginator

        func()


# ============================
# ListTagsOfResourcePaginator
# ============================


def test_list_tags_of_resource_arg_pass(gen_list_tags_of_resource_paginator):
    @beartype
    def func(param: ListTagsOfResourcePaginator):
        pass

    func(gen_list_tags_of_resource_paginator)


def test_list_tags_of_resource_arg_fail(gen_query_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListTagsOfResourcePaginator):
            pass

        func(gen_query_paginator)


def test_list_tags_of_resource_return_pass(gen_list_tags_of_resource_paginator):
    @beartype
    def func() -> ListTagsOfResourcePaginator:
        return gen_list_tags_of_resource_paginator

    func()


def test_list_tags_of_resource_return_fail(gen_query_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListTagsOfResourcePaginator:
            return gen_query_paginator

        func()
