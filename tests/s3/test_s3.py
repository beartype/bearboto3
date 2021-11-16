import boto3
import pytest
from bearboto3.s3 import (
    MultipartUpload,
    MultipartUploadPart,
    S3Client,
    S3ServiceResource,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)
from moto import mock_ec2, mock_s3

# ============================
# CLIENT
# ============================


def test_s3_client_arg_pass(s3_client):
    @beartype
    def func(client: S3Client):
        pass

    func(s3_client)


def test_s3_client_arg_fail(aws_setup):
    with mock_ec2():
        with pytest.raises(BeartypeCallHintPepParamException):

            @beartype
            def func(client: S3Client):
                pass

            func(boto3.client("ec2"))


def test_s3_client_return_pass(aws_setup):
    @beartype
    def func() -> S3Client:
        with mock_s3():
            return boto3.client("s3")

    client = func()


def test_s3_client_return_fail(aws_setup):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> S3Client:
            with mock_ec2():
                yield boto3.client("ec2")

        client = func()


# ============================
# RESOURCE
# ============================


def test_s3_resource_arg_pass(s3_resource):
    @beartype
    def func(resource: S3ServiceResource):
        pass

    func(s3_resource)


def test_s3_resource_arg_fail(aws_setup):
    with mock_ec2():
        with pytest.raises(BeartypeCallHintPepParamException):

            @beartype
            def func(client: S3ServiceResource):
                pass

            func(boto3.resource("ec2"))


def test_s3_resource_return_pass(aws_setup):
    @beartype
    def func() -> S3ServiceResource:
        with mock_s3():
            return boto3.resource("s3")

    resource = func()


def test_s3_resource_return_fail(aws_setup):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> S3ServiceResource:
            with mock_ec2():
                yield boto3.resource("ec2")

        resource = func()


# ============================
# MULTIPART UPLOAD
# ============================


def test_multipart_upload_arg_pass(gen_multipart_upload):
    @beartype
    def func(multipart: MultipartUpload):
        pass

    func(gen_multipart_upload)


def test_multipart_upload_arg_fail(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(multipart: MultipartUpload):
            pass

        func(s3_resource)


def test_multipart_upload_return_pass(gen_multipart_upload):
    @beartype
    def func() -> MultipartUpload:
        return gen_multipart_upload

    multipart = func()


def test_multipart_upload_return_fail(s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> MultipartUpload:
            return s3_resource

        multipart = func()


# ============================
# MULTIPART UPLOAD PART
# ============================


def test_multipart_upload_part_arg_pass(gen_multipart_upload_part):
    @beartype
    def func(multipart: MultipartUploadPart):
        pass

    func(gen_multipart_upload_part)


def test_multipart_upload_part_arg_fail(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(multipart: MultipartUploadPart):
            pass

        func(s3_resource)


def test_multipart_upload_part_return_pass(gen_multipart_upload_part):
    @beartype
    def func() -> MultipartUploadPart:
        return gen_multipart_upload_part

    multipart = func()


def test_multipart_upload_part_return_fail(s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> MultipartUploadPart:
            return s3_resource

        multipart = func()
