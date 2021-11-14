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


def test_buckets_collection_pass(s3_resource):
    @beartype
    def func(collection: ServiceResourceBucketsCollection):
        pass
    func(s3_resource.buckets.all())

def test_bucket_multipart_uploads_collection_pass(s3_bucket):
    @beartype
    def func(collection: BucketMultipartUploadsCollection):
        pass
    func(s3_bucket.multipart_uploads.all())

def test_multipart_upload_parts_collection_pass(s3_resource):
    multipart_upload = s3_resource.MultipartUpload(random_str(), random_str(), random_str())
    @beartype
    def func(collection: MultipartUploadPartsCollection):
        pass
    func(multipart_upload.parts.all())

def test_bucket_objects_collection_pass(s3_bucket):
    @beartype
    def func(collection: BucketObjectsCollection):
        pass
    func(s3_bucket.objects.all())

def test_bucket_object_versions_collection_pass(s3_bucket):
    @beartype
    def func(collection: BucketObjectVersionsCollection):
        pass
    func(s3_bucket.object_versions.all())
