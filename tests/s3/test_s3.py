import random

import boto3
import pytest
from bearboto3.s3 import (MultipartUpload, MultipartUploadPart, S3Client,
                          S3ServiceResource)
from beartype import beartype
from beartype.roar import BeartypeCallHintPepParamException
from moto import mock_ec2
from tests.utils import random_str

MIN_MULTIPART_NUM = 1
MAX_MULTIPART_NUM = 10000


def test_s3_client_pass(s3_client):
    @beartype
    def func(client: S3Client):
        pass
    func(s3_client)

def test_s3_client_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(client: S3Client):
            pass
        func(random_str())

def test_s3_client_fail_similar(aws_setup):
    with mock_ec2():
        bad_client = boto3.client('ec2')
        with pytest.raises(BeartypeCallHintPepParamException):
            @beartype
            def func(client: S3Client):
                pass
            func(bad_client)

def test_s3_resource_pass(s3_resource):
    @beartype
    def func(resource: S3ServiceResource):
        pass
    func(s3_resource)

def test_s3_resource_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(client: S3ServiceResource):
            pass
        func(random_str())

def test_s3_resource_fail_similar(aws_setup):
    with mock_ec2():
        bad_resource = boto3.resource('ec2')
        with pytest.raises(BeartypeCallHintPepParamException):
            @beartype
            def func(client: S3ServiceResource):
                pass
            func(bad_resource)

def test_multipart_upload_pass(s3_resource):
    @beartype
    def func(multipart: MultipartUpload):
        pass
    func(s3_resource.MultipartUpload(random_str(), random_str(), random_str()))

def test_multipart_upload_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUpload):
            pass
        func(random_str())
    
def test_multipart_upload_fail_similar(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUpload):
            pass
        func(s3_resource)

def test_multipart_upload_part_pass(s3_resource):
    @beartype
    def func(multipart: MultipartUploadPart):
        pass
    func(s3_resource.MultipartUploadPart(random_str(), random_str(), random_str(), random.randint(MIN_MULTIPART_NUM, MAX_MULTIPART_NUM)))

def test_multipart_upload_part_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUploadPart):
            pass
        func(random_str())

def test_multipart_upload_part_fail_similar(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUploadPart):
            pass
        func(s3_resource)
