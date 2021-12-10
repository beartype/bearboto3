import boto3
import pytest
from moto import mock_s3
from tests.utils import random_str


@pytest.fixture
def gen_s3_client(aws_setup):
    with mock_s3():
        yield boto3.client("s3")


@pytest.fixture
def gen_s3_resource(aws_setup):
    with mock_s3():
        yield boto3.resource("s3")


# ============================
# WAITER
# ============================


@pytest.fixture
def gen_bucket_exists_waiter(gen_s3_client):
    return gen_s3_client.get_waiter("bucket_exists")


@pytest.fixture
def gen_bucket_not_exists_waiter(gen_s3_client):
    return gen_s3_client.get_waiter("bucket_not_exists")


@pytest.fixture
def gen_object_exists_waiter(gen_s3_client):
    return gen_s3_client.get_waiter("object_exists")


@pytest.fixture
def gen_object_not_exists_waiter(gen_s3_client):
    return gen_s3_client.get_waiter("object_not_exists")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_list_multipart_uploads_paginator(gen_s3_client):
    return gen_s3_client.get_paginator("list_multipart_uploads")


@pytest.fixture
def gen_list_object_versions_paginator(gen_s3_client):
    return gen_s3_client.get_paginator("list_object_versions")


@pytest.fixture
def gen_list_objects_paginator(gen_s3_client):
    return gen_s3_client.get_paginator("list_objects")


@pytest.fixture
def gen_list_objects_v2_paginator(gen_s3_client):
    return gen_s3_client.get_paginator("list_objects_v2")


@pytest.fixture
def gen_list_parts_paginator(gen_s3_client):
    return gen_s3_client.get_paginator("list_parts")


# ============================
# RESOURCES
# ============================


@pytest.fixture
def gen_bucket(gen_s3_resource):
    return gen_s3_resource.Bucket(random_str())


@pytest.fixture
def gen_bucket_acl(gen_s3_resource):
    return gen_s3_resource.BucketAcl(random_str())


@pytest.fixture
def gen_bucket_cors(gen_s3_resource):
    return gen_s3_resource.BucketCors(random_str())


@pytest.fixture
def gen_bucket_lifecycle(gen_s3_resource):
    return gen_s3_resource.BucketLifecycle(random_str())


@pytest.fixture
def gen_bucket_lifecycle_configuration(gen_s3_resource):
    return gen_s3_resource.BucketLifecycleConfiguration(random_str())


@pytest.fixture
def gen_bucket_logging(gen_s3_resource):
    return gen_s3_resource.BucketLogging(random_str())


@pytest.fixture
def gen_bucket_notification(gen_s3_resource):
    return gen_s3_resource.BucketNotification(random_str())


@pytest.fixture
def gen_bucket_policy(gen_s3_resource):
    return gen_s3_resource.BucketPolicy(random_str())


@pytest.fixture
def gen_bucket_request_payment(gen_s3_resource):
    return gen_s3_resource.BucketRequestPayment(random_str())


@pytest.fixture
def gen_bucket_tagging(gen_s3_resource):
    return gen_s3_resource.BucketTagging(random_str())


@pytest.fixture
def gen_bucket_versioning(gen_s3_resource):
    return gen_s3_resource.BucketVersioning(random_str())


@pytest.fixture
def gen_bucket_website(gen_s3_resource):
    return gen_s3_resource.BucketWebsite(random_str())


@pytest.fixture
def gen_multipart_upload(gen_s3_resource):
    return gen_s3_resource.MultipartUpload(random_str(), random_str(), random_str())


@pytest.fixture
def gen_multipart_upload_part(gen_s3_resource):
    return gen_s3_resource.MultipartUploadPart(
        random_str(), random_str(), random_str(), random_str()
    )


@pytest.fixture
def gen_object(gen_s3_resource):
    return gen_s3_resource.Object(random_str(), random_str())


@pytest.fixture
def gen_object_acl(gen_s3_resource):
    return gen_s3_resource.ObjectAcl(random_str(), random_str())


@pytest.fixture
def gen_object_summary(gen_s3_resource):
    return gen_s3_resource.ObjectSummary(random_str(), random_str())


@pytest.fixture
def gen_object_version(gen_s3_resource):
    return gen_s3_resource.ObjectVersion(random_str(), random_str(), random_str())


# ============================
# COLLECTIONS
# ============================


@pytest.fixture
def gen_service_resource_buckets_collection(gen_s3_resource):
    return gen_s3_resource.buckets.all()


@pytest.fixture
def gen_bucket_multipart_uploads_collection(gen_bucket):
    return gen_bucket.multipart_uploads.all()


@pytest.fixture
def gen_bucket_object_versions_collection(gen_bucket):
    return gen_bucket.object_versions.all()


@pytest.fixture
def gen_bucket_objects_collection(gen_bucket):
    return gen_bucket.objects.all()


@pytest.fixture
def gen_multipart_upload_parts_collection(gen_multipart_upload):
    return gen_multipart_upload.parts.all()
