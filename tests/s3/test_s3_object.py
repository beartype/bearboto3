import pytest
from bearboto3.s3 import Object, ObjectAcl, ObjectSummary, ObjectVersion
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)

# ============================
# OBJECT
# ============================


def test_object_arg_pass(gen_object):
    @beartype
    def func(obj: Object):
        pass

    func(gen_object)


def test_object_arg_fail(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(obj: Object):
            pass

        func(s3_resource)


def test_object_return_pass(gen_object):
    @beartype
    def func() -> Object:
        return gen_object

    obj = func()


def test_object_return_fail(s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Object:
            return s3_resource

        obj = func()


# ============================
# OBJECT ACL
# ============================


def test_object_acl_arg_pass(gen_object_acl):
    @beartype
    def func(obj: ObjectAcl):
        pass

    func(gen_object_acl)


def test_object_acl_arg_fail(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(obj: ObjectAcl):
            pass

        func(s3_resource)


def test_object_acl_return_pass(gen_object_acl):
    @beartype
    def func() -> ObjectAcl:
        return gen_object_acl

    obj = func()


def test_object_acl_return_fail(s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectAcl:
            return s3_resource

        obj = func()


# ============================
# OBJECT SUMMARY
# ============================


def test_object_summary_arg_pass(gen_object_summary):
    @beartype
    def func(obj: ObjectSummary):
        pass

    func(gen_object_summary)


def test_object_summary_arg_fail(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(obj: ObjectSummary):
            pass

        func(s3_resource)


def test_object_summary_return_pass(gen_object_summary):
    @beartype
    def func() -> ObjectSummary:
        return gen_object_summary

    obj = func()


def test_object_summary_return_fail(s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectSummary:
            return s3_resource

        obj = func()


# ============================
# OBJECT VERSION
# ============================


def test_object_version_arg_pass(gen_object_version):
    @beartype
    def func(obj: ObjectVersion):
        pass

    func(gen_object_version)


def test_object_version_arg_fail(s3_resource):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(obj: ObjectVersion):
            pass

        func(s3_resource)


def test_object_version_return_pass(gen_object_version):
    @beartype
    def func() -> ObjectVersion:
        return gen_object_version

    obj = func()


def test_object_version_return_fail(s3_resource):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ObjectVersion:
            return s3_resource

        obj = func()
