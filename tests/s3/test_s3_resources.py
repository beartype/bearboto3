import pytest
from bearboto3.s3 import (
    Bucket,
    BucketAcl,
    BucketCors,
    BucketLifecycle,
    BucketLifecycleConfiguration,
    BucketLogging,
    BucketNotification,
    BucketPolicy,
    BucketRequestPayment,
    BucketTagging,
    BucketVersioning,
    BucketWebsite,
    MultipartUpload,
    MultipartUploadPart,
    Object,
    ObjectAcl,
    ObjectSummary,
    ObjectVersion,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# Bucket
# ============================


def test_bucket_arg_pass(gen_bucket):
    @beartype
    def func(param: Bucket):
        pass

    func(gen_bucket)


def test_bucket_arg_fail(gen_bucket_versioning):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Bucket):
            pass

        func(gen_bucket_versioning)


def test_bucket_return_pass(gen_bucket):
    @beartype
    def func() -> Bucket:
        return gen_bucket

    func()


def test_bucket_return_fail(gen_bucket_versioning):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Bucket:
            return gen_bucket_versioning

        func()


# ============================
# BucketAcl
# ============================


def test_bucket_acl_arg_pass(gen_bucket_acl):
    @beartype
    def func(param: BucketAcl):
        pass

    func(gen_bucket_acl)


def test_bucket_acl_arg_fail(gen_bucket_lifecycle_configuration):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketAcl):
            pass

        func(gen_bucket_lifecycle_configuration)


def test_bucket_acl_return_pass(gen_bucket_acl):
    @beartype
    def func() -> BucketAcl:
        return gen_bucket_acl

    func()


def test_bucket_acl_return_fail(gen_bucket_lifecycle_configuration):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketAcl:
            return gen_bucket_lifecycle_configuration

        func()


# ============================
# BucketCors
# ============================


def test_bucket_cors_arg_pass(gen_bucket_cors):
    @beartype
    def func(param: BucketCors):
        pass

    func(gen_bucket_cors)


def test_bucket_cors_arg_fail(gen_multipart_upload):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketCors):
            pass

        func(gen_multipart_upload)


def test_bucket_cors_return_pass(gen_bucket_cors):
    @beartype
    def func() -> BucketCors:
        return gen_bucket_cors

    func()


def test_bucket_cors_return_fail(gen_multipart_upload):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketCors:
            return gen_multipart_upload

        func()


# ============================
# BucketLifecycle
# ============================


def test_bucket_lifecycle_arg_pass(gen_bucket_lifecycle):
    @beartype
    def func(param: BucketLifecycle):
        pass

    func(gen_bucket_lifecycle)


def test_bucket_lifecycle_arg_fail(gen_bucket_logging):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketLifecycle):
            pass

        func(gen_bucket_logging)


def test_bucket_lifecycle_return_pass(gen_bucket_lifecycle):
    @beartype
    def func() -> BucketLifecycle:
        return gen_bucket_lifecycle

    func()


def test_bucket_lifecycle_return_fail(gen_bucket_logging):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketLifecycle:
            return gen_bucket_logging

        func()


# ============================
# BucketLifecycleConfiguration
# ============================


def test_bucket_lifecycle_configuration_arg_pass(gen_bucket_lifecycle_configuration):
    @beartype
    def func(param: BucketLifecycleConfiguration):
        pass

    func(gen_bucket_lifecycle_configuration)


def test_bucket_lifecycle_configuration_arg_fail(gen_bucket_notification):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketLifecycleConfiguration):
            pass

        func(gen_bucket_notification)


def test_bucket_lifecycle_configuration_return_pass(gen_bucket_lifecycle_configuration):
    @beartype
    def func() -> BucketLifecycleConfiguration:
        return gen_bucket_lifecycle_configuration

    func()


def test_bucket_lifecycle_configuration_return_fail(gen_bucket_notification):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketLifecycleConfiguration:
            return gen_bucket_notification

        func()


# ============================
# BucketLogging
# ============================


def test_bucket_logging_arg_pass(gen_bucket_logging):
    @beartype
    def func(param: BucketLogging):
        pass

    func(gen_bucket_logging)


def test_bucket_logging_arg_fail(gen_object_acl):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketLogging):
            pass

        func(gen_object_acl)


def test_bucket_logging_return_pass(gen_bucket_logging):
    @beartype
    def func() -> BucketLogging:
        return gen_bucket_logging

    func()


def test_bucket_logging_return_fail(gen_object_acl):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketLogging:
            return gen_object_acl

        func()


# ============================
# BucketNotification
# ============================


def test_bucket_notification_arg_pass(gen_bucket_notification):
    @beartype
    def func(param: BucketNotification):
        pass

    func(gen_bucket_notification)


def test_bucket_notification_arg_fail(gen_bucket_tagging):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketNotification):
            pass

        func(gen_bucket_tagging)


def test_bucket_notification_return_pass(gen_bucket_notification):
    @beartype
    def func() -> BucketNotification:
        return gen_bucket_notification

    func()


def test_bucket_notification_return_fail(gen_bucket_tagging):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketNotification:
            return gen_bucket_tagging

        func()


# ============================
# BucketPolicy
# ============================


def test_bucket_policy_arg_pass(gen_bucket_policy):
    @beartype
    def func(param: BucketPolicy):
        pass

    func(gen_bucket_policy)


def test_bucket_policy_arg_fail(gen_bucket):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketPolicy):
            pass

        func(gen_bucket)


def test_bucket_policy_return_pass(gen_bucket_policy):
    @beartype
    def func() -> BucketPolicy:
        return gen_bucket_policy

    func()


def test_bucket_policy_return_fail(gen_bucket):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketPolicy:
            return gen_bucket

        func()


# ============================
# BucketRequestPayment
# ============================


def test_bucket_request_payment_arg_pass(gen_bucket_request_payment):
    @beartype
    def func(param: BucketRequestPayment):
        pass

    func(gen_bucket_request_payment)


def test_bucket_request_payment_arg_fail(gen_bucket_cors):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketRequestPayment):
            pass

        func(gen_bucket_cors)


def test_bucket_request_payment_return_pass(gen_bucket_request_payment):
    @beartype
    def func() -> BucketRequestPayment:
        return gen_bucket_request_payment

    func()


def test_bucket_request_payment_return_fail(gen_bucket_cors):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketRequestPayment:
            return gen_bucket_cors

        func()


# ============================
# BucketTagging
# ============================


def test_bucket_tagging_arg_pass(gen_bucket_tagging):
    @beartype
    def func(param: BucketTagging):
        pass

    func(gen_bucket_tagging)


def test_bucket_tagging_arg_fail(gen_multipart_upload_part):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketTagging):
            pass

        func(gen_multipart_upload_part)


def test_bucket_tagging_return_pass(gen_bucket_tagging):
    @beartype
    def func() -> BucketTagging:
        return gen_bucket_tagging

    func()


def test_bucket_tagging_return_fail(gen_multipart_upload_part):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketTagging:
            return gen_multipart_upload_part

        func()


# ============================
# BucketVersioning
# ============================


def test_bucket_versioning_arg_pass(gen_bucket_versioning):
    @beartype
    def func(param: BucketVersioning):
        pass

    func(gen_bucket_versioning)


def test_bucket_versioning_arg_fail(gen_object_summary):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketVersioning):
            pass

        func(gen_object_summary)


def test_bucket_versioning_return_pass(gen_bucket_versioning):
    @beartype
    def func() -> BucketVersioning:
        return gen_bucket_versioning

    func()


def test_bucket_versioning_return_fail(gen_object_summary):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketVersioning:
            return gen_object_summary

        func()


# ============================
# BucketWebsite
# ============================


def test_bucket_website_arg_pass(gen_bucket_website):
    @beartype
    def func(param: BucketWebsite):
        pass

    func(gen_bucket_website)


def test_bucket_website_arg_fail(gen_bucket_logging):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: BucketWebsite):
            pass

        func(gen_bucket_logging)


def test_bucket_website_return_pass(gen_bucket_website):
    @beartype
    def func() -> BucketWebsite:
        return gen_bucket_website

    func()


def test_bucket_website_return_fail(gen_bucket_logging):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BucketWebsite:
            return gen_bucket_logging

        func()


# ============================
# MultipartUpload
# ============================


def test_multipart_upload_arg_pass(gen_multipart_upload):
    @beartype
    def func(param: MultipartUpload):
        pass

    func(gen_multipart_upload)


def test_multipart_upload_arg_fail(gen_bucket_logging):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: MultipartUpload):
            pass

        func(gen_bucket_logging)


def test_multipart_upload_return_pass(gen_multipart_upload):
    @beartype
    def func() -> MultipartUpload:
        return gen_multipart_upload

    func()


def test_multipart_upload_return_fail(gen_bucket_logging):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> MultipartUpload:
            return gen_bucket_logging

        func()


# ============================
# MultipartUploadPart
# ============================


def test_multipart_upload_part_arg_pass(gen_multipart_upload_part):
    @beartype
    def func(param: MultipartUploadPart):
        pass

    func(gen_multipart_upload_part)


def test_multipart_upload_part_arg_fail(gen_bucket_cors):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: MultipartUploadPart):
            pass

        func(gen_bucket_cors)


def test_multipart_upload_part_return_pass(gen_multipart_upload_part):
    @beartype
    def func() -> MultipartUploadPart:
        return gen_multipart_upload_part

    func()


def test_multipart_upload_part_return_fail(gen_bucket_cors):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> MultipartUploadPart:
            return gen_bucket_cors

        func()


# ============================
# Object
# ============================


def test_object_arg_pass(gen_object):
    @beartype
    def func(param: Object):
        pass

    func(gen_object)


def test_object_arg_fail(gen_bucket_request_payment):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Object):
            pass

        func(gen_bucket_request_payment)


def test_object_return_pass(gen_object):
    @beartype
    def func() -> Object:
        return gen_object

    func()


def test_object_return_fail(gen_bucket_request_payment):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Object:
            return gen_bucket_request_payment

        func()


# ============================
# ObjectAcl
# ============================


def test_object_acl_arg_pass(gen_object_acl):
    @beartype
    def func(param: ObjectAcl):
        pass

    func(gen_object_acl)


def test_object_acl_arg_fail(gen_object_summary):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ObjectAcl):
            pass

        func(gen_object_summary)


def test_object_acl_return_pass(gen_object_acl):
    @beartype
    def func() -> ObjectAcl:
        return gen_object_acl

    func()


def test_object_acl_return_fail(gen_object_summary):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectAcl:
            return gen_object_summary

        func()


# ============================
# ObjectSummary
# ============================


def test_object_summary_arg_pass(gen_object_summary):
    @beartype
    def func(param: ObjectSummary):
        pass

    func(gen_object_summary)


def test_object_summary_arg_fail(gen_object_acl):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ObjectSummary):
            pass

        func(gen_object_acl)


def test_object_summary_return_pass(gen_object_summary):
    @beartype
    def func() -> ObjectSummary:
        return gen_object_summary

    func()


def test_object_summary_return_fail(gen_object_acl):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectSummary:
            return gen_object_acl

        func()


# ============================
# ObjectVersion
# ============================


def test_object_version_arg_pass(gen_object_version):
    @beartype
    def func(param: ObjectVersion):
        pass

    func(gen_object_version)


def test_object_version_arg_fail(gen_bucket_request_payment):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ObjectVersion):
            pass

        func(gen_bucket_request_payment)


def test_object_version_return_pass(gen_object_version):
    @beartype
    def func() -> ObjectVersion:
        return gen_object_version

    func()


def test_object_version_return_fail(gen_bucket_request_payment):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectVersion:
            return gen_bucket_request_payment

        func()
