import pytest
from bearboto3.s3 import (BucketMultipartUploadsCollection,
                          BucketObjectsCollection,
                          BucketObjectVersionsCollection,
                          MultipartUploadPartsCollection,
                          ServiceResourceBucketsCollection)
from beartype import beartype
from beartype.roar import (BeartypeCallHintPepParamException,
                           BeartypeCallHintPepReturnException,
                           BeartypeDecorHintPep484585Exception)
from tests.utils import random_str

# ============================
# BUCKETS
# ============================

def test_buckets_collection_arg_pass(gen_buckets_collection):
    @beartype
    def func(collection: ServiceResourceBucketsCollection):
        pass
    func(gen_buckets_collection)

def test_buckets_collection_arg_fail(gen_bucket_objects_collection):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: ServiceResourceBucketsCollection):
            pass
        func(gen_bucket_objects_collection)

def test_buckets_collection_return_pass(gen_buckets_collection):
    @beartype
    def func() -> ServiceResourceBucketsCollection:
        return gen_buckets_collection
    param = func()

def test_buckets_collection_return_fail(gen_bucket_objects_collection):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> ServiceResourceBucketsCollection:
            return gen_bucket_objects_collection
        param = func()

# ============================
# BUCKET MULTIPART UPLOADS
# ============================

def test_bucket_multipart_uploads_collection_arg_pass(gen_bucket_multipart_uploads_collection):
    @beartype
    def func(collection: BucketMultipartUploadsCollection):
        pass
    func(gen_bucket_multipart_uploads_collection)

def test_bucket_multipart_uploads_collection_arg_fail(gen_multipart_upload_parts_collection):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketMultipartUploadsCollection):
            pass
        func(gen_multipart_upload_parts_collection)

def test_bucket_multipart_uploads_collection_return_pass(gen_bucket_multipart_uploads_collection):
    @beartype
    def func() -> BucketMultipartUploadsCollection:
        return gen_bucket_multipart_uploads_collection
    param = func()

def test_bucket_multipart_uploads_collection_return_fail(gen_multipart_upload_parts_collection):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketMultipartUploadsCollection:
            return gen_multipart_upload_parts_collection
        param = func()

# ============================
# MULTIPART UPLOAD PARTS
# ============================

def test_multipart_upload_parts_collection_arg_pass(gen_multipart_upload_parts_collection):
    @beartype
    def func(collection: MultipartUploadPartsCollection):
        pass
    func(gen_multipart_upload_parts_collection)

def test_multipart_upload_parts_collection_arg_fail(gen_bucket_multipart_uploads_collection):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: MultipartUploadPartsCollection):
            pass
        func(gen_bucket_multipart_uploads_collection)

def test_multipart_upload_parts_collection_return_pass(gen_multipart_upload_parts_collection):
    @beartype
    def func() -> MultipartUploadPartsCollection:
        return gen_multipart_upload_parts_collection
    param = func()

def test_multipart_upload_parts_collection_return_fail(gen_bucket_multipart_uploads_collection):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> MultipartUploadPartsCollection:
            return gen_bucket_multipart_uploads_collection
        param = func()

# ============================
# BUCKET OBJECTS
# ============================

def test_bucket_objects_collection_arg_pass(gen_bucket_objects_collection):
    @beartype
    def func(collection: BucketObjectsCollection):
        pass
    func(gen_bucket_objects_collection)

def test_bucket_objects_collection_arg_fail(gen_bucket_object_versions_collection):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketObjectsCollection):
            pass
        func(gen_bucket_object_versions_collection)

def test_bucket_objects_collection_return_pass(gen_bucket_objects_collection):
    @beartype
    def func() -> BucketObjectsCollection:
        return gen_bucket_objects_collection
    param = func()

def test_bucket_objects_collection_return_fail(gen_bucket_object_versions_collection):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketObjectsCollection:
            return gen_bucket_object_versions_collection
        param = func()

# ============================
# BUCKET OBJECT VERSIONS
# ============================

def test_bucket_object_versions_collection_arg_pass(gen_bucket_object_versions_collection):
    @beartype
    def func(collection: BucketObjectVersionsCollection):
        pass
    func(gen_bucket_object_versions_collection)

def test_bucket_object_versions_collection_arg_fail(gen_bucket_objects_collection):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketObjectVersionsCollection):
            pass
        func(gen_bucket_objects_collection)

def test_bucket_object_versions_collection_return_pass(gen_bucket_object_versions_collection):
    @beartype
    def func() -> BucketObjectVersionsCollection:
        return gen_bucket_object_versions_collection
    param = func()

def test_bucket_object_versions_collection_return_fail(gen_bucket_objects_collection):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketObjectVersionsCollection:
            return gen_bucket_objects_collection
        param = func()
