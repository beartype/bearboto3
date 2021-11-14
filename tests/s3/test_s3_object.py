from bearboto3.s3 import Object, ObjectAcl, ObjectSummary, ObjectVersion
from beartype import beartype
from beartype.roar import (BeartypeCallHintPepParamException,
                           BeartypeCallHintPepReturnException,
                           BeartypeDecorHintPep484585Exception)
from tests.utils import random_str


def test_object_arg_pass(s3_resource):
    @beartype
    def func(obj: Object):
        pass
    func(s3_resource.Object(random_str(), random_str()))

def test_object_return_pass(s3_resource):
    pass

def test_object_arg_fail():
    pass

def test_object_return_fail():
    pass

def test_object_arg_fail_similar(s3_resource):
    pass

def test_object_return_fail_similar(s3_resource):
    pass

def test_object_acl_arg_pass(s3_resource):
    @beartype
    def func(obj: ObjectAcl):
        pass
    func(s3_resource.ObjectAcl(random_str(), random_str()))

def test_object_acl_return_pass(s3_resource):
    pass

def test_object_acl_arg_fail():
    pass

def test_object_acl_return_fail():
    pass

def test_object_acl_arg_fail_similar(s3_resource):
    pass

def test_object_acl_return_fail_similar(s3_resource):
    pass

def test_object_summary_arg_pass(s3_resource):
    @beartype
    def func(obj: ObjectSummary):
        pass
    func(s3_resource.ObjectSummary(random_str(), random_str()))

def test_object_summary_return_pass(s3_resource):
    pass

def test_object_summary_arg_fail():
    pass

def test_object_summary_return_fail():
    pass

def test_object_summary_arg_fail_similar(s3_resource):
    pass

def test_object_summary_return_fail_similar(s3_resource):
    pass

def test_object_version_arg_pass(s3_resource):
    @beartype
    def func(obj: ObjectVersion):
        pass
    func(s3_resource.ObjectVersion(random_str(), random_str(), random_str()))

def test_object_version_return_pass(s3_resource):
    pass

def test_object_version_arg_fail():
    pass

def test_object_version_return_fail():
    pass

def test_object_version_arg_fail_similar(s3_resource):
    pass

def test_object_version_return_fail_similar(s3_resource):
    pass
