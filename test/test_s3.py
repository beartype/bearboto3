import boto3
import pytest
from bearboto3.s3 import (Bucket, BucketAcl, BucketCors, BucketExistsWaiter,
                          BucketLifecycle, BucketLifecycleConfiguration,
                          BucketLogging, BucketMultipartUploadsCollection,
                          BucketNotExistsWaiter, BucketNotification,
                          BucketObjectsCollection,
                          BucketObjectVersionsCollection, BucketPolicy,
                          BucketRequestPayment, BucketTagging,
                          BucketVersioning, BucketWebsite, Client,
                          ListMultipartUploadsPaginator, ListObjectsPaginator,
                          ListObjectsV2Paginator, ListObjectVersionsPaginator,
                          ListPartsPaginator, MultipartUpload,
                          MultipartUploadPart, MultipartUploadPartsCollection,
                          Object, ObjectAcl, ObjectExistsWaiter,
                          ObjectNotExistsWaiter, ObjectSummary, ObjectVersion,
                          S3Client, S3ServiceResource, ServiceResource,
                          ServiceResourceBucketsCollection)
from beartype import beartype
from moto import mock_s3

from utils import random_str


@pytest.fixture
def s3_client(aws_setup):
    with mock_s3():
        yield boto3.client('s3')

@pytest.fixture
def s3_resource(aws_setup):
    with mock_s3():
        yield boto3.resource('s3')

def test_s3_client(s3_client):
    @beartype
    def func(client1: S3Client, client2: Client):
        pass
    func(s3_client, s3_client)

def test_s3_resource(s3_resource):
    @beartype
    def func(resource1: S3ServiceResource, resource2: ServiceResource):
        pass
    func(s3_resource, s3_resource)

def test_bucket_exists_waiter(s3_client):
    @beartype
    def func(waiter: BucketExistsWaiter):
        pass
    func(s3_client.get_waiter('bucket_exists'))

def test_bucket_not_exists_waiter(s3_client):
    @beartype
    def func(waiter: BucketNotExistsWaiter):
        pass
    func(s3_client.get_waiter('bucket_not_exists'))

def test_object_exists_waiter(s3_client):
    @beartype
    def func(waiter: ObjectExistsWaiter):
        pass
    func(s3_client.get_waiter('object_exists'))

def test_object_not_exists_waiter(s3_client):
    @beartype
    def func(waiter: ObjectNotExistsWaiter):
        pass
    func(s3_client.get_waiter('object_not_exists'))

def test_list_multipart_uploads_paginator(s3_client):
    @beartype
    def func(paginator: ListMultipartUploadsPaginator):
        pass
    func(s3_client.get_paginator('list_multipart_uploads'))

def test_list_object_versions_paginator(s3_client):
    @beartype
    def func(paginator: ListObjectVersionsPaginator):
        pass
    func(s3_client.get_paginator('list_object_versions'))

def test_list_objects_paginator(s3_client):
    @beartype
    def func(paginator: ListObjectsPaginator):
        pass
    func(s3_client.get_paginator('list_objects'))

def test_list_objects_v2_paginator(s3_client):
    @beartype
    def func(paginator: ListObjectsV2Paginator):
        pass
    func(s3_client.get_paginator('list_objects_v2'))

def test_list_parts_paginator(s3_client):
    @beartype
    def func(paginator: ListPartsPaginator):
        pass
    func(s3_client.get_paginator('list_parts'))

def test_bucket(s3_resource):
    @beartype
    def func(bucket: Bucket):
        pass
    func(s3_resource.Bucket(random_str()))

def test_bucket_acl(s3_resource):
    @beartype
    def func(bucket: BucketAcl):
        pass
    func(s3_resource.BucketAcl(random_str()))

def test_bucket_cors(s3_resource):
    @beartype
    def func(bucket: BucketCors):
        pass
    func(s3_resource.BucketCors(random_str()))

def test_bucket_lifecycle(s3_resource):
    @beartype
    def func(bucket: BucketLifecycle):
        pass
    func(s3_resource.BucketLifecycle(random_str()))

def test_bucket_lifecycle_configuration(s3_resource):
    @beartype
    def func(bucket: BucketLifecycleConfiguration):
        pass
    func(s3_resource.BucketLifecycleConfiguration(random_str()))

def test_bucket_logging(s3_resource):
    @beartype
    def func(bucket: BucketLogging):
        pass
    func(s3_resource.BucketLogging(random_str()))

def test_bucket_notification(s3_resource):
    @beartype
    def func(bucket: BucketNotification):
        pass
    func(s3_resource.BucketNotification(random_str()))

def test_bucket_policy(s3_resource):
    @beartype
    def func(bucket: BucketPolicy):
        pass
    func(s3_resource.BucketPolicy(random_str()))

def test_bucket_request_payment(s3_resource):
    @beartype
    def func(bucket: BucketRequestPayment):
        pass
    func(s3_resource.BucketRequestPayment(random_str()))

def test_bucket_tagging(s3_resource):
    @beartype
    def func(bucket: BucketTagging):
        pass
    func(s3_resource.BucketTagging(random_str()))

def test_bucket_versioning(s3_resource):
    @beartype
    def func(bucket: BucketVersioning):
        pass
    func(s3_resource.BucketVersioning(random_str()))

def test_bucket_website(s3_resource):
    @beartype
    def func(bucket: BucketWebsite):
        pass
    func(s3_resource.BucketWebsite(random_str()))
