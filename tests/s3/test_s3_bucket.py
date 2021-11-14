import pytest
from bearboto3.s3 import (Bucket, BucketAcl, BucketCors, BucketLifecycle,
                          BucketLifecycleConfiguration, BucketLogging,
                          BucketNotification, BucketPolicy,
                          BucketRequestPayment, BucketTagging,
                          BucketVersioning, BucketWebsite)
from beartype import beartype
from beartype.roar import (BeartypeCallHintPepParamException,
                           BeartypeCallHintPepReturnException,
                           BeartypeDecorHintPep484585Exception)
from tests.utils import random_str

# ============================
# BUCKET
# ============================

def test_bucket_arg_pass(gen_bucket):
    @beartype
    def func(param: Bucket):
        pass
    func(gen_bucket)

def test_bucket_arg_fail(gen_bucket_acl):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: Bucket):
            pass
        func(gen_bucket_acl)

def test_bucket_return_pass(gen_bucket):
    @beartype
    def func() -> Bucket:
        return gen_bucket
    param = func()

def test_bucket_return_fail(gen_bucket_acl):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> Bucket:
            return gen_bucket_acl
        param = func()

# ============================
# BUCKET ACL
# ============================

def test_bucket_acl_arg_pass(gen_bucket_acl):
    @beartype
    def func(param: BucketAcl):
        pass
    func(gen_bucket_acl)

def test_bucket_acl_arg_fail(gen_bucket):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketAcl):
            pass
        func(gen_bucket)

def test_bucket_acl_return_pass(gen_bucket_acl):
    @beartype
    def func() -> BucketAcl:
        return gen_bucket_acl
    param = func()

def test_bucket_acl_return_fail(gen_bucket):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketAcl:
            return gen_bucket
        param = func()

# ============================
# BUCKET CORS
# ============================

def test_bucket_cors_arg_pass(gen_bucket_cors):
    @beartype
    def func(param: BucketCors):
        pass
    func(gen_bucket_cors)

def test_bucket_cors_arg_fail(gen_bucket):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketCors):
            pass
        func(gen_bucket)

def test_bucket_cors_return_pass(gen_bucket_cors):
    @beartype
    def func() -> BucketCors:
        return gen_bucket_cors
    param = func()

def test_bucket_cors_return_fail(gen_bucket):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketCors:
            return gen_bucket
        param = func()

# ============================
# BUCKET LIFECYCLE
# ============================

def test_bucket_lifecycle_arg_pass(gen_bucket_lifecycle):
    @beartype
    def func(param: BucketLifecycle):
        pass
    func(gen_bucket_lifecycle)

def test_bucket_lifecycle_arg_fail(gen_bucket_lifecycle_configuration):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketLifecycle):
            pass
        func(gen_bucket_lifecycle_configuration)

def test_bucket_lifecycle_return_pass(gen_bucket_lifecycle):
    @beartype
    def func() -> BucketLifecycle:
        return gen_bucket_lifecycle
    param = func()

def test_bucket_lifecycle_return_fail(gen_bucket_lifecycle_configuration):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketLifecycle:
            return gen_bucket_lifecycle_configuration
        param = func()

# ===============================
# BUCKET LIFECYCLE CONFIGURATION
# ===============================

def test_bucket_lifecycle_configuration_arg_pass(gen_bucket_lifecycle_configuration):
    @beartype
    def func(param: BucketLifecycleConfiguration):
        pass
    func(gen_bucket_lifecycle_configuration)

def test_bucket_lifecycle_configuration_arg_fail(gen_bucket_lifecycle):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketLifecycleConfiguration):
            pass
        func(gen_bucket_lifecycle)

def test_bucket_lifecycle_configuration_return_pass(gen_bucket_lifecycle_configuration):
    @beartype
    def func() -> BucketLifecycleConfiguration:
        return gen_bucket_lifecycle_configuration
    param = func()

def test_bucket_lifecycle_configuration_return_fail(gen_bucket_lifecycle):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketLifecycleConfiguration:
            return gen_bucket_lifecycle
        param = func()

# ============================
# BUCKET LOGGING
# ============================

def test_bucket_logging_arg_pass(gen_bucket_logging):
    @beartype
    def func(param: BucketLogging):
        pass
    func(gen_bucket_logging)

def test_bucket_logging_arg_fail(gen_bucket_notification):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketLogging):
            pass
        func(gen_bucket_notification)

def test_bucket_logging_return_pass(gen_bucket_logging):
    @beartype
    def func() -> BucketLogging:
        return gen_bucket_logging
    param = func()

def test_bucket_logging_return_fail(gen_bucket_notification):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketLogging:
            return gen_bucket_notification
        param = func()

# ============================
# BUCKET NOTIFICATION
# ============================

def test_bucket_notification_arg_pass(gen_bucket_notification):
    @beartype
    def func(param: BucketNotification):
        pass
    func(gen_bucket_notification)

def test_bucket_notification_arg_fail(gen_bucket_logging):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketNotification):
            pass
        func(gen_bucket_logging)

def test_bucket_notification_return_pass(gen_bucket_notification):
    @beartype
    def func() -> BucketNotification:
        return gen_bucket_notification
    param = func()

def test_bucket_notification_return_fail(gen_bucket_logging):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketNotification:
            return gen_bucket_logging
        param = func()

# ============================
# BUCKET POLICY
# ============================

def test_bucket_policy_arg_pass(gen_bucket_policy):
    @beartype
    def func(param: BucketPolicy):
        pass
    func(gen_bucket_policy)

def test_bucket_policy_arg_fail(gen_bucket_request_payment):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketPolicy):
            pass
        func(gen_bucket_request_payment)

def test_bucket_policy_return_pass(gen_bucket_policy):
    @beartype
    def func() -> BucketPolicy:
        return gen_bucket_policy
    param = func()

def test_bucket_policy_return_fail(gen_bucket_request_payment):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketPolicy:
            return gen_bucket_request_payment
        param = func()

# ============================
# BUCKET REQUEST PAYMENT
# ============================

def test_bucket_request_payment_arg_pass(gen_bucket_request_payment):
    @beartype
    def func(param: BucketRequestPayment):
        pass
    func(gen_bucket_request_payment)

def test_bucket_request_payment_arg_fail(gen_bucket_policy):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketRequestPayment):
            pass
        func(gen_bucket_policy)

def test_bucket_request_payment_return_pass(gen_bucket_request_payment):
    @beartype
    def func() -> BucketRequestPayment:
        return gen_bucket_request_payment
    param = func()

def test_bucket_request_payment_return_fail(gen_bucket_policy):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketRequestPayment:
            return gen_bucket_policy
        param = func()

# ============================
# BUCKET TAGGING
# ============================

def test_bucket_tagging_arg_pass(gen_bucket_tagging):
    @beartype
    def func(param: BucketTagging):
        pass
    func(gen_bucket_tagging)

def test_bucket_tagging_arg_fail(gen_bucket_versioning):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketTagging):
            pass
        func(gen_bucket_versioning)

def test_bucket_tagging_return_pass(gen_bucket_tagging):
    @beartype
    def func() -> BucketTagging:
        return gen_bucket_tagging
    param = func()

def test_bucket_tagging_return_fail(gen_bucket_versioning):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketTagging:
            return gen_bucket_versioning
        param = func()

# ============================
# BUCKET VERSIONING
# ============================

def test_bucket_versioning_arg_pass(gen_bucket_versioning):
    @beartype
    def func(param: BucketVersioning):
        pass
    func(gen_bucket_versioning)

def test_bucket_versioning_arg_fail(gen_bucket_tagging):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketVersioning):
            pass
        func(gen_bucket_tagging)

def test_bucket_versioning_return_pass(gen_bucket_versioning):
    @beartype
    def func() -> BucketVersioning:
        return gen_bucket_versioning
    param = func()

def test_bucket_versioning_return_fail(gen_bucket_tagging):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketVersioning:
            return gen_bucket_tagging
        param = func()

# ============================
# BUCKET WEBSITE
# ============================

def test_bucket_website_arg_pass(gen_bucket_website):
    @beartype
    def func(param: BucketWebsite):
        pass
    func(gen_bucket_website)

def test_bucket_website_arg_fail(gen_bucket):
    with pytest.raises(BeartypeCallHintPepParamException):
        @beartype
        def func(param: BucketWebsite):
            pass
        func(gen_bucket)

def test_bucket_website_return_pass(gen_bucket_website):
    @beartype
    def func() -> BucketWebsite:
        return gen_bucket_website
    param = func()

def test_bucket_website_return_fail(gen_bucket):
    with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
        @beartype
        def func() -> BucketWebsite:
            return gen_bucket
        param = func()
