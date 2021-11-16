import pytest
from bearboto3.s3 import (
    ListMultipartUploadsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListObjectVersionsPaginator,
    ListPartsPaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)

# ============================
# MULTIPART
# ============================


def test_list_multipart_uploads_paginator_pass(gen_list_multipart_uploads_paginator):
    @beartype
    def func(paginator: ListMultipartUploadsPaginator):
        pass

    func(gen_list_multipart_uploads_paginator)


def test_list_multipart_uploads_paginator_arg_fail(get_list_object_versions_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(paginator: ListMultipartUploadsPaginator):
            pass

        func(get_list_object_versions_paginator)


def test_list_multipart_uploads_paginator_return_pass(
    gen_list_multipart_uploads_paginator,
):
    @beartype
    def func() -> ListMultipartUploadsPaginator:
        return gen_list_multipart_uploads_paginator

    paginator = func()


def test_list_multipart_uploads_paginator_return_fail(
    get_list_object_versions_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListMultipartUploadsPaginator:
            return get_list_object_versions_paginator

        paginator = func()


# ============================
# OBJECT VERSIONS
# ============================


def test_list_object_versions_paginator_pass(get_list_object_versions_paginator):
    @beartype
    def func(paginator: ListObjectVersionsPaginator):
        pass

    func(get_list_object_versions_paginator)


def test_list_object_versions_paginator_arg_fail(gen_list_multipart_uploads_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(paginator: ListObjectVersionsPaginator):
            pass

        func(gen_list_multipart_uploads_paginator)


def test_list_object_versions_paginator_return_pass(get_list_object_versions_paginator):
    @beartype
    def func() -> ListObjectVersionsPaginator:
        return get_list_object_versions_paginator

    paginator = func()


def test_list_object_versions_paginator_return_fail(
    gen_list_multipart_uploads_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListObjectVersionsPaginator:
            return gen_list_multipart_uploads_paginator

        paginator = func()


# ============================
# LIST OBJECTS
# ============================


def test_list_objects_paginator_pass(gen_list_objects_paginator):
    @beartype
    def func(paginator: ListObjectsPaginator):
        pass

    func(gen_list_objects_paginator)


def test_list_objects_paginator_arg_fail(gen_list_objects_v2_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(paginator: ListObjectsPaginator):
            pass

        func(gen_list_objects_v2_paginator)


def test_list_objects_paginator_return_pass(gen_list_objects_paginator):
    @beartype
    def func() -> ListObjectsPaginator:
        return gen_list_objects_paginator

    paginator = func()


def test_list_objects_paginator_return_fail(gen_list_objects_v2_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListObjectsPaginator:
            return gen_list_objects_v2_paginator

        paginator = func()


# ============================
# LIST OBJECTS V2
# ============================


def test_list_objects_v2_paginator_pass(gen_list_objects_v2_paginator):
    @beartype
    def func(paginator: ListObjectsV2Paginator):
        pass

    func(gen_list_objects_v2_paginator)


def test_list_objects_v2_paginator_arg_fail(gen_list_objects_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(paginator: ListObjectsV2Paginator):
            pass

        func(gen_list_objects_paginator)


def test_list_objects_v2_paginator_return_pass(gen_list_objects_v2_paginator):
    @beartype
    def func() -> ListObjectsV2Paginator:
        return gen_list_objects_v2_paginator

    paginator = func()


def test_list_objects_v2_paginator_return_fail(gen_list_objects_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListObjectsV2Paginator:
            return gen_list_objects_paginator

        paginator = func()


# ============================
# LIST PARTS
# ============================


def test_list_parts_paginator_pass(gen_list_parts_paginator):
    @beartype
    def func(paginator: ListPartsPaginator):
        pass

    func(gen_list_parts_paginator)


def test_list_parts_paginator_arg_fail(gen_list_objects_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(paginator: ListPartsPaginator):
            pass

        func(gen_list_objects_paginator)


def test_list_parts_paginator_return_pass(gen_list_parts_paginator):
    @beartype
    def func() -> ListPartsPaginator:
        return gen_list_parts_paginator

    paginator = func()


def test_list_parts_paginator_return_fail(gen_list_objects_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListPartsPaginator:
            return gen_list_objects_paginator

        paginator = func()
