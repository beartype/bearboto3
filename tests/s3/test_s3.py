import random

import boto3
import pytest
from bearboto3.s3 import (MultipartUpload, MultipartUploadPart, S3Client,
                          S3ServiceResource)
from beartype import beartype
from beartype.roar import (BeartypeCallHintPepParamException,
                           BeartypeCallHintPepReturnException,
                           BeartypeDecorHintPep484585Exception)
from moto import mock_ec2, mock_s3
from tests.utils import random_str

MIN_MULTIPART_NUM = 1
MAX_MULTIPART_NUM = 10000


def test_s3_client_arg_pass(s3_client):
    @beartype
    def func(client: S3Client):
        pass
    func(s3_client)

def test_s3_client_return_pass(aws_setup):
    @beartype
    def func() -> S3Client:
        with mock_s3():
            return boto3.client('s3')
    client = func()

def test_s3_client_arg_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(client: S3Client):
            pass
        func(random_str())

def test_s3_client_return_fail():
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> S3Client:
            return random_str()
        client = func()

def test_s3_client_arg_fail_similar(aws_setup):
    with mock_ec2():
        bad_client = boto3.client('ec2')
        with pytest.raises(BeartypeCallHintPepParamException):
            @beartype
            def func(client: S3Client):
                pass
            func(bad_client)

def test_s3_client_return_fail_similar(aws_setup):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> S3Client:
            with mock_ec2():
                yield boto3.client('ec2')
        client = func()

def test_s3_resource_arg_pass(s3_resource):
    @beartype
    def func(resource: S3ServiceResource):
        pass
    func(s3_resource)

def test_s3_resource_return_pass(aws_setup):
    @beartype
    def func() -> S3ServiceResource:
        with mock_s3():
            return boto3.resource('s3')
    resource = func()

def test_s3_resource_arg_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(client: S3ServiceResource):
            pass
        func(random_str())

def test_s3_resource_return_fail():
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> S3ServiceResource:
            return random_str()
        resource = func()

def test_s3_resource_arg_fail_similar(aws_setup):
    with mock_ec2():
        bad_resource = boto3.resource('ec2')
        with pytest.raises(BeartypeCallHintPepParamException):
            @beartype
            def func(client: S3ServiceResource):
                pass
            func(bad_resource)

def test_s3_resource_return_fail_similar(aws_setup):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> S3ServiceResource:
            with mock_ec2():
                yield boto3.resource('ec2')
        resource = func()

def test_multipart_upload_arg_pass(s3_resource):
    @beartype
    def func(multipart: MultipartUpload):
        pass
    func(s3_resource.MultipartUpload(random_str(), random_str(), random_str()))

def test_multipart_upload_return_pass(s3_resource):
    @beartype
    def func() -> MultipartUpload:
        return s3_resource.MultipartUpload(random_str(), random_str(), random_str())
    multipart = func()

def test_multipart_upload_arg_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUpload):
            pass
        func(random_str())

def test_multipart_upload_return_fail():
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> MultipartUpload:
            return random_str()
        multipart = func()
    
def test_multipart_upload_arg_fail_similar(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUpload):
            pass
        func(s3_resource)

def test_multipart_upload_return_fail_similar(s3_resource):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> MultipartUpload:
            return s3_resource
        multipart = func()

def test_multipart_upload_part_arg_pass(s3_resource):
    @beartype
    def func(multipart: MultipartUploadPart):
        pass
    func(s3_resource.MultipartUploadPart(random_str(), random_str(), random_str(), random.randint(MIN_MULTIPART_NUM, MAX_MULTIPART_NUM)))

def test_multipart_upload_part_return_pass(s3_resource):
    @beartype
    def func() -> MultipartUploadPart:
        return s3_resource.MultipartUploadPart(random_str(), random_str(), random_str(), random.randint(MIN_MULTIPART_NUM, MAX_MULTIPART_NUM))
    multipart = func()

def test_multipart_upload_part_arg_fail():
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUploadPart):
            pass
        func(random_str())

def test_multipart_upload_part_return_fail():
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> MultipartUploadPart:
            return random_str()
        multipart = func()

def test_multipart_upload_part_arg_fail_similar(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(multipart: MultipartUploadPart):
            pass
        func(s3_resource)

def test_multipart_upload_part_return_fail_similar(s3_resource):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> MultipartUploadPart:
            return s3_resource
        multipart = func()
