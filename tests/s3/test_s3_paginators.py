import pytest
from bearboto3.s3 import (
    ListMultipartUploadsPaginator,
    ListObjectVersionsPaginator,
    ListObjectsPaginator,
    ListObjectsV2Paginator,
    ListPartsPaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ListMultipartUploadsPaginator
# ============================


def test_list_multipart_uploads_arg_pass(gen_list_multipart_uploads_paginator):
    @beartype
    def func(param: ListMultipartUploadsPaginator):
        pass

    func(gen_list_multipart_uploads_paginator)


def test_list_multipart_uploads_arg_fail(gen_list_objects_v2_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListMultipartUploadsPaginator):
            pass

        func(gen_list_objects_v2_paginator)


def test_list_multipart_uploads_return_pass(gen_list_multipart_uploads_paginator):
    @beartype
    def func() -> ListMultipartUploadsPaginator:
        return gen_list_multipart_uploads_paginator

    func()


def test_list_multipart_uploads_return_fail(gen_list_objects_v2_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListMultipartUploadsPaginator:
            return gen_list_objects_v2_paginator

        func()


# ============================
# ListObjectVersionsPaginator
# ============================


def test_list_object_versions_arg_pass(gen_list_object_versions_paginator):
    @beartype
    def func(param: ListObjectVersionsPaginator):
        pass

    func(gen_list_object_versions_paginator)


def test_list_object_versions_arg_fail(gen_list_objects_v2_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListObjectVersionsPaginator):
            pass

        func(gen_list_objects_v2_paginator)


def test_list_object_versions_return_pass(gen_list_object_versions_paginator):
    @beartype
    def func() -> ListObjectVersionsPaginator:
        return gen_list_object_versions_paginator

    func()


def test_list_object_versions_return_fail(gen_list_objects_v2_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListObjectVersionsPaginator:
            return gen_list_objects_v2_paginator

        func()


# ============================
# ListObjectsPaginator
# ============================


def test_list_objects_arg_pass(gen_list_objects_paginator):
    @beartype
    def func(param: ListObjectsPaginator):
        pass

    func(gen_list_objects_paginator)


def test_list_objects_arg_fail(gen_list_multipart_uploads_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListObjectsPaginator):
            pass

        func(gen_list_multipart_uploads_paginator)


def test_list_objects_return_pass(gen_list_objects_paginator):
    @beartype
    def func() -> ListObjectsPaginator:
        return gen_list_objects_paginator

    func()


def test_list_objects_return_fail(gen_list_multipart_uploads_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListObjectsPaginator:
            return gen_list_multipart_uploads_paginator

        func()


# ============================
# ListObjectsV2Paginator
# ============================


def test_list_objects_v2_arg_pass(gen_list_objects_v2_paginator):
    @beartype
    def func(param: ListObjectsV2Paginator):
        pass

    func(gen_list_objects_v2_paginator)


def test_list_objects_v2_arg_fail(gen_list_object_versions_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListObjectsV2Paginator):
            pass

        func(gen_list_object_versions_paginator)


def test_list_objects_v2_return_pass(gen_list_objects_v2_paginator):
    @beartype
    def func() -> ListObjectsV2Paginator:
        return gen_list_objects_v2_paginator

    func()


def test_list_objects_v2_return_fail(gen_list_object_versions_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListObjectsV2Paginator:
            return gen_list_object_versions_paginator

        func()


# ============================
# ListPartsPaginator
# ============================


def test_list_parts_arg_pass(gen_list_parts_paginator):
    @beartype
    def func(param: ListPartsPaginator):
        pass

    func(gen_list_parts_paginator)


def test_list_parts_arg_fail(gen_list_object_versions_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListPartsPaginator):
            pass

        func(gen_list_object_versions_paginator)


def test_list_parts_return_pass(gen_list_parts_paginator):
    @beartype
    def func() -> ListPartsPaginator:
        return gen_list_parts_paginator

    func()


def test_list_parts_return_fail(gen_list_object_versions_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListPartsPaginator:
            return gen_list_object_versions_paginator

        func()
