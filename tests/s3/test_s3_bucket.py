from bearboto3.s3 import (Bucket, BucketAcl, BucketCors, BucketLifecycle,
                          BucketLifecycleConfiguration, BucketLogging,
                          BucketNotification, BucketPolicy,
                          BucketRequestPayment, BucketTagging,
                          BucketVersioning, BucketWebsite)
from beartype import beartype
from tests.utils import random_str


def test_bucket_pass(s3_resource):
    @beartype
    def func(bucket: Bucket):
        pass
    func(s3_resource.Bucket(random_str()))

def test_bucket_acl_pass(s3_resource):
    @beartype
    def func(bucket: BucketAcl):
        pass
    func(s3_resource.BucketAcl(random_str()))

def test_bucket_cors_pass(s3_resource):
    @beartype
    def func(bucket: BucketCors):
        pass
    func(s3_resource.BucketCors(random_str()))

def test_bucket_lifecycle_pass(s3_resource):
    @beartype
    def func(bucket: BucketLifecycle):
        pass
    func(s3_resource.BucketLifecycle(random_str()))

def test_bucket_lifecycle_configuration_pass(s3_resource):
    @beartype
    def func(bucket: BucketLifecycleConfiguration):
        pass
    func(s3_resource.BucketLifecycleConfiguration(random_str()))

def test_bucket_logging_pass(s3_resource):
    @beartype
    def func(bucket: BucketLogging):
        pass
    func(s3_resource.BucketLogging(random_str()))

def test_bucket_notification_pass(s3_resource):
    @beartype
    def func(bucket: BucketNotification):
        pass
    func(s3_resource.BucketNotification(random_str()))

def test_bucket_policy_pass(s3_resource):
    @beartype
    def func(bucket: BucketPolicy):
        pass
    func(s3_resource.BucketPolicy(random_str()))

def test_bucket_request_payment_pass(s3_resource):
    @beartype
    def func(bucket: BucketRequestPayment):
        pass
    func(s3_resource.BucketRequestPayment(random_str()))

def test_bucket_tagging_pass(s3_resource):
    @beartype
    def func(bucket: BucketTagging):
        pass
    func(s3_resource.BucketTagging(random_str()))

def test_bucket_versioning_pass(s3_resource):
    @beartype
    def func(bucket: BucketVersioning):
        pass
    func(s3_resource.BucketVersioning(random_str()))

def test_bucket_website_pass(s3_resource):
    @beartype
    def func(bucket: BucketWebsite):
        pass
    func(s3_resource.BucketWebsite(random_str()))
