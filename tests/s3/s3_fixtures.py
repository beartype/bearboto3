import random

import boto3
import pytest
from moto import mock_s3
from tests.utils import random_str

MIN_MULTIPART_NUM = 1
MAX_MULTIPART_NUM = 10000


@pytest.fixture
def s3_client(aws_setup):
    with mock_s3():
        yield boto3.client("s3")


@pytest.fixture
def s3_resource(aws_setup):
    with mock_s3():
        yield boto3.resource("s3")


# ============================
# MULTIPART
# ============================


@pytest.fixture
def gen_multipart_upload(s3_resource):
    return s3_resource.MultipartUpload(random_str(), random_str(), random_str())


@pytest.fixture
def gen_multipart_upload_part(s3_resource):
    return s3_resource.MultipartUploadPart(
        random_str(),
        random_str(),
        random_str(),
        random.randint(MIN_MULTIPART_NUM, MAX_MULTIPART_NUM),
    )


# ============================
# OBJECT
# ============================


@pytest.fixture
def gen_object(s3_resource):
    return s3_resource.Object(random_str(), random_str())


@pytest.fixture
def gen_object_acl(s3_resource):
    return s3_resource.ObjectAcl(random_str(), random_str())


@pytest.fixture
def gen_object_summary(s3_resource):
    return s3_resource.ObjectSummary(random_str(), random_str())


@pytest.fixture
def gen_object_version(s3_resource):
    return s3_resource.ObjectVersion(random_str(), random_str(), random_str())


# ============================
# WAITER
# ============================


@pytest.fixture
def gen_bucket_exists_waiter(s3_client):
    return s3_client.get_waiter("bucket_exists")


@pytest.fixture
def gen_bucket_not_exists_waiter(s3_client):
    return s3_client.get_waiter("bucket_not_exists")


@pytest.fixture
def gen_object_exists_waiter(s3_client):
    return s3_client.get_waiter("object_exists")


@pytest.fixture
def gen_object_not_exists_waiter(s3_client):
    return s3_client.get_waiter("object_not_exists")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_list_multipart_uploads_paginator(s3_client):
    return s3_client.get_paginator("list_multipart_uploads")


@pytest.fixture
def get_list_object_versions_paginator(s3_client):
    return s3_client.get_paginator("list_object_versions")


@pytest.fixture
def gen_list_objects_paginator(s3_client):
    return s3_client.get_paginator("list_objects")


@pytest.fixture
def gen_list_objects_v2_paginator(s3_client):
    return s3_client.get_paginator("list_objects_v2")


@pytest.fixture
def gen_list_parts_paginator(s3_client):
    return s3_client.get_paginator("list_parts")


# ============================
# COLLECTIONS
# ============================


@pytest.fixture
def gen_buckets_collection(s3_resource):
    return s3_resource.buckets.all()


@pytest.fixture
def gen_bucket_multipart_uploads_collection(gen_bucket):
    return gen_bucket.multipart_uploads.all()


@pytest.fixture
def gen_multipart_upload_parts_collection(s3_resource):
    multipart_upload = s3_resource.MultipartUpload(
        random_str(), random_str(), random_str()
    )
    return multipart_upload.parts.all()


@pytest.fixture
def gen_bucket_objects_collection(gen_bucket):
    return gen_bucket.objects.all()


@pytest.fixture
def gen_bucket_object_versions_collection(gen_bucket):
    return gen_bucket.object_versions.all()


# ============================
# BUCKET
# ============================


@pytest.fixture
def gen_bucket(s3_resource):
    return s3_resource.create_bucket(Bucket=random_str())


@pytest.fixture
def gen_bucket_acl(s3_resource):
    return s3_resource.BucketAcl(random_str())


@pytest.fixture
def gen_bucket_cors(s3_resource):
    return s3_resource.BucketCors(random_str())


@pytest.fixture
def gen_bucket_lifecycle(s3_resource):
    return s3_resource.BucketLifecycle(random_str())


@pytest.fixture
def gen_bucket_lifecycle_configuration(s3_resource):
    return s3_resource.BucketLifecycleConfiguration(random_str())


@pytest.fixture
def gen_bucket_logging(s3_resource):
    return s3_resource.BucketLogging(random_str())


@pytest.fixture
def gen_bucket_notification(s3_resource):
    return s3_resource.BucketNotification(random_str())


@pytest.fixture
def gen_bucket_policy(s3_resource):
    return s3_resource.BucketPolicy(random_str())


@pytest.fixture
def gen_bucket_request_payment(s3_resource):
    return s3_resource.BucketRequestPayment(random_str())


@pytest.fixture
def gen_bucket_tagging(s3_resource):
    return s3_resource.BucketTagging(random_str())


@pytest.fixture
def gen_bucket_versioning(s3_resource):
    return s3_resource.BucketVersioning(random_str())


@pytest.fixture
def gen_bucket_website(s3_resource):
    return s3_resource.BucketWebsite(random_str())
