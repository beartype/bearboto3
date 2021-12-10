from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_s3 import (
        BucketExistsWaiter,
        BucketNotExistsWaiter,
        ListMultipartUploadsPaginator,
        ListObjectVersionsPaginator,
        ListObjectsPaginator,
        ListObjectsV2Paginator,
        ListPartsPaginator,
        ObjectExistsWaiter,
        ObjectNotExistsWaiter,
        S3Client,
    )
    from mypy_boto3_s3.service_resource import (
        Bucket,
        BucketAcl,
        BucketCors,
        BucketLifecycle,
        BucketLifecycleConfiguration,
        BucketLogging,
        BucketMultipartUploadsCollection,
        BucketNotification,
        BucketObjectVersionsCollection,
        BucketObjectsCollection,
        BucketPolicy,
        BucketRequestPayment,
        BucketTagging,
        BucketVersioning,
        BucketWebsite,
        MultipartUpload,
        MultipartUploadPart,
        MultipartUploadPartsCollection,
        Object,
        ObjectAcl,
        ObjectSummary,
        ObjectVersion,
        S3ServiceResource,
        ServiceResourceBucketsCollection,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    Bucket = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.Bucket"]]]
    ]

    BucketAcl = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketAcl"]]],
    ]

    BucketCors = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketCors"]]],
    ]

    BucketExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.BucketExists"]]],
    ]

    BucketLifecycle = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketLifecycle"]]],
    ]

    BucketLifecycleConfiguration = Annotated[
        ServiceResource,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["s3.BucketLifecycleConfiguration"]]
        ],
    ]

    BucketLogging = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketLogging"]]],
    ]

    BucketMultipartUploadsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["s3.Bucket.multipart_uploadsCollection"]],
        ],
    ]

    BucketNotExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.BucketNotExists"]]],
    ]

    BucketNotification = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketNotification"]]],
    ]

    BucketObjectVersionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["s3.Bucket.object_versionsCollection"]],
        ],
    ]

    BucketObjectsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.Bucket.objectsCollection"]]],
    ]

    BucketPolicy = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketPolicy"]]],
    ]

    BucketRequestPayment = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketRequestPayment"]]],
    ]

    BucketTagging = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketTagging"]]],
    ]

    BucketVersioning = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketVersioning"]]],
    ]

    BucketWebsite = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketWebsite"]]],
    ]

    ListMultipartUploadsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["S3.Paginator.ListMultipartUploads"]],
        ],
    ]

    ListObjectVersionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListObjectVersions"]]
        ],
    ]

    ListObjectsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListObjects"]]],
    ]

    ListObjectsV2Paginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListObjectsV2"]]],
    ]

    ListPartsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListParts"]]],
    ]

    MultipartUpload = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.MultipartUpload"]]],
    ]

    MultipartUploadPart = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.MultipartUploadPart"]]],
    ]

    MultipartUploadPartsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["s3.MultipartUpload.partsCollection"]],
        ],
    ]

    Object = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.Object"]]]
    ]

    ObjectAcl = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ObjectAcl"]]],
    ]

    ObjectExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.ObjectExists"]]],
    ]

    ObjectNotExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.ObjectNotExists"]]],
    ]

    ObjectSummary = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ObjectSummary"]]],
    ]

    ObjectVersion = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ObjectVersion"]]],
    ]

    S3Client = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["S3"]]]
    ]

    S3ServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ServiceResource"]]],
    ]

    ServiceResourceBucketsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["s3.bucketsCollection"]]],
    ]
