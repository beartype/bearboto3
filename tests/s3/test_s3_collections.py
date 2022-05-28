import pytest
from bearboto3.s3 import (
    ServiceResourceBucketsCollection,
    BucketMultipartUploadsCollection,
    BucketObjectVersionsCollection,
    BucketObjectsCollection,
    MultipartUploadPartsCollection,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ServiceResourceBucketsCollection
# ============================


def test_buckets_arg_pass(gen_service_resource_buckets_collection):
    @beartype
    def func(param: ServiceResourceBucketsCollection):
        pass

    func(gen_service_resource_buckets_collection)


def test_buckets_arg_fail(gen_bucket_objects_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ServiceResourceBucketsCollection):
            pass

        func(gen_bucket_objects_collection)


def test_buckets_return_pass(gen_service_resource_buckets_collection):
    @beartype
    def func() -> ServiceResourceBucketsCollection:
        return gen_service_resource_buckets_collection

    func()


def test_buckets_return_fail(gen_bucket_objects_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceBucketsCollection:
            return gen_bucket_objects_collection

        func()


# ============================
# BucketMultipartUploadsCollection
# ============================


def test_multipart_uploads_arg_pass(gen_bucket_multipart_uploads_collection):
    @beartype
    def func(param: BucketMultipartUploadsCollection):
        pass

    func(gen_bucket_multipart_uploads_collection)


def test_multipart_uploads_arg_fail(gen_bucket_object_versions_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: BucketMultipartUploadsCollection):
            pass

        func(gen_bucket_object_versions_collection)


def test_multipart_uploads_return_pass(gen_bucket_multipart_uploads_collection):
    @beartype
    def func() -> BucketMultipartUploadsCollection:
        return gen_bucket_multipart_uploads_collection

    func()


def test_multipart_uploads_return_fail(gen_bucket_object_versions_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketMultipartUploadsCollection:
            return gen_bucket_object_versions_collection

        func()


# ============================
# BucketObjectVersionsCollection
# ============================


def test_object_versions_arg_pass(gen_bucket_object_versions_collection):
    @beartype
    def func(param: BucketObjectVersionsCollection):
        pass

    func(gen_bucket_object_versions_collection)


def test_object_versions_arg_fail(gen_bucket_objects_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: BucketObjectVersionsCollection):
            pass

        func(gen_bucket_objects_collection)


def test_object_versions_return_pass(gen_bucket_object_versions_collection):
    @beartype
    def func() -> BucketObjectVersionsCollection:
        return gen_bucket_object_versions_collection

    func()


def test_object_versions_return_fail(gen_bucket_objects_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketObjectVersionsCollection:
            return gen_bucket_objects_collection

        func()


# ============================
# BucketObjectsCollection
# ============================


def test_objects_arg_pass(gen_bucket_objects_collection):
    @beartype
    def func(param: BucketObjectsCollection):
        pass

    func(gen_bucket_objects_collection)


def test_objects_arg_fail(gen_service_resource_buckets_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: BucketObjectsCollection):
            pass

        func(gen_service_resource_buckets_collection)


def test_objects_return_pass(gen_bucket_objects_collection):
    @beartype
    def func() -> BucketObjectsCollection:
        return gen_bucket_objects_collection

    func()


def test_objects_return_fail(gen_service_resource_buckets_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketObjectsCollection:
            return gen_service_resource_buckets_collection

        func()


# ============================
# MultipartUploadPartsCollection
# ============================


def test_parts_arg_pass(gen_multipart_upload_parts_collection):
    @beartype
    def func(param: MultipartUploadPartsCollection):
        pass

    func(gen_multipart_upload_parts_collection)


def test_parts_arg_fail(gen_bucket_object_versions_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: MultipartUploadPartsCollection):
            pass

        func(gen_bucket_object_versions_collection)


def test_parts_return_pass(gen_multipart_upload_parts_collection):
    @beartype
    def func() -> MultipartUploadPartsCollection:
        return gen_multipart_upload_parts_collection

    func()


def test_parts_return_fail(gen_bucket_object_versions_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> MultipartUploadPartsCollection:
            return gen_bucket_object_versions_collection

        func()
