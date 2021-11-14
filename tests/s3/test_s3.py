import random

from bearboto3.s3 import (MultipartUpload, MultipartUploadPart, S3Client,
                          S3ServiceResource)
from beartype import beartype
from tests.utils import random_str

MIN_MULTIPART_NUM = 1
MAX_MULTIPART_NUM = 10000


def test_s3_client_pass(s3_client):
    @beartype
    def func(client: S3Client):
        pass
    func(s3_client)

def test_s3_resource_pass(s3_resource):
    @beartype
    def func(resource: S3ServiceResource):
        pass
    func(s3_resource)


def test_multipart_upload_pass(s3_resource):
    @beartype
    def func(multipart: MultipartUpload):
        pass
    func(s3_resource.MultipartUpload(random_str(), random_str(), random_str()))

def test_multipart_upload_part_pass(s3_resource):
    @beartype
    def func(multipart: MultipartUploadPart):
        pass
    func(s3_resource.MultipartUploadPart(random_str(), random_str(), random_str(), random.randint(MIN_MULTIPART_NUM, MAX_MULTIPART_NUM)))
