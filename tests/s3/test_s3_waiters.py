from bearboto3.s3 import (BucketExistsWaiter, BucketNotExistsWaiter,
                          ObjectExistsWaiter, ObjectNotExistsWaiter)
from beartype import beartype
from beartype.roar import (BeartypeCallHintPepParamException,
                           BeartypeCallHintPepReturnException,
                           BeartypeDecorHintPep484585Exception)


def test_bucket_exists_waiter_pass(s3_client):
    @beartype
    def func(waiter: BucketExistsWaiter):
        pass
    func(s3_client.get_waiter('bucket_exists'))

def test_bucket_not_exists_waiter_pass(s3_client):
    @beartype
    def func(waiter: BucketNotExistsWaiter):
        pass
    func(s3_client.get_waiter('bucket_not_exists'))

def test_object_exists_waiter_pass(s3_client):
    @beartype
    def func(waiter: ObjectExistsWaiter):
        pass
    func(s3_client.get_waiter('object_exists'))

def test_object_not_exists_waiter_pass(s3_client):
    @beartype
    def func(waiter: ObjectNotExistsWaiter):
        pass
    func(s3_client.get_waiter('object_not_exists'))
