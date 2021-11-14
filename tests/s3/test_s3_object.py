from bearboto3.s3 import Object, ObjectAcl, ObjectSummary, ObjectVersion
from beartype import beartype
from tests.utils import random_str


def test_object_pass(s3_resource):
    @beartype
    def func(obj: Object):
        pass
    func(s3_resource.Object(random_str(), random_str()))

def test_object_acl_pass(s3_resource):
    @beartype
    def func(obj: ObjectAcl):
        pass
    func(s3_resource.ObjectAcl(random_str(), random_str()))

def test_object_summary_pass(s3_resource):
    @beartype
    def func(obj: ObjectSummary):
        pass
    func(s3_resource.ObjectSummary(random_str(), random_str()))

def test_object_version_pass(s3_resource):
    @beartype
    def func(obj: ObjectVersion):
        pass
    func(s3_resource.ObjectVersion(random_str(), random_str(), random_str()))
