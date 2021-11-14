from bearboto3.s3 import (ListMultipartUploadsPaginator, ListObjectsPaginator,
                          ListObjectsV2Paginator, ListObjectVersionsPaginator,
                          ListPartsPaginator)
from beartype import beartype
from beartype.roar import (BeartypeCallHintPepParamException,
                           BeartypeCallHintPepReturnException,
                           BeartypeDecorHintPep484585Exception)


def test_list_multipart_uploads_paginator_pass(s3_client):
    @beartype
    def func(paginator: ListMultipartUploadsPaginator):
        pass
    func(s3_client.get_paginator('list_multipart_uploads'))

def test_list_object_versions_paginator_pass(s3_client):
    @beartype
    def func(paginator: ListObjectVersionsPaginator):
        pass
    func(s3_client.get_paginator('list_object_versions'))

def test_list_objects_paginator_pass(s3_client):
    @beartype
    def func(paginator: ListObjectsPaginator):
        pass
    func(s3_client.get_paginator('list_objects'))

def test_list_objects_v2_paginator_pass(s3_client):
    @beartype
    def func(paginator: ListObjectsV2Paginator):
        pass
    func(s3_client.get_paginator('list_objects_v2'))

def test_list_parts_paginator_pass(s3_client):
    @beartype
    def func(paginator: ListPartsPaginator):
        pass
    func(s3_client.get_paginator('list_parts'))
