from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_s3 import (
        BucketExistsWaiter,
        BucketNotExistsWaiter,
        Client,
        ListMultipartUploadsPaginator,
        ListObjectVersionsPaginator,
        ListObjectsPaginator,
        ListObjectsV2Paginator,
        ListPartsPaginator,
        ObjectExistsWaiter,
        ObjectNotExistsWaiter,
        S3Client,
        S3ServiceResource,
        ServiceResource,
    )
    from mypy_boto3_s3.service_resource import (
        S3ServiceResource,
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
        ServiceResourceBucketsCollection,
        BucketMultipartUploadsCollection,
        BucketObjectVersionsCollection,
        BucketObjectsCollection,
        MultipartUploadPartsCollection,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from bearboto3 import Annotated

    BucketExistsWaiter = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.BucketExists"]]]]
    BucketNotExistsWaiter = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.BucketNotExists"]]]
    ]
    ListMultipartUploadsPaginator = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListMultipartUploads"]]]
    ]
    ListObjectVersionsPaginator = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListObjectVersions"]]]
    ]
    ListObjectsPaginator = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListObjects"]]]
    ]
    ListObjectsV2Paginator = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListObjectsV2"]]]
    ]
    ListPartsPaginator = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Paginator.ListParts"]]]]
    ObjectExistsWaiter = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.ObjectExists"]]]]
    ObjectNotExistsWaiter = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3.Waiter.ObjectNotExists"]]]
    ]
    S3Client = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["S3"]]]]
    Client = S3Client
    S3ServiceResource = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ServiceResource"]]]]
    ServiceResource = S3ServiceResource

    Bucket = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.Bucket"]]]]
    BucketAcl = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketAcl"]]]]
    BucketCors = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketCors"]]]]
    BucketLifecycle = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketLifecycle"]]]]
    BucketLifecycleConfiguration = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketLifecycleConfiguration"]]]
    ]
    BucketLogging = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketLogging"]]]]
    BucketNotification = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketNotification"]]]]
    BucketPolicy = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketPolicy"]]]]
    BucketRequestPayment = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketRequestPayment"]]]
    ]
    BucketTagging = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketTagging"]]]]
    BucketVersioning = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketVersioning"]]]]
    BucketWebsite = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketWebsite"]]]]
    MultipartUpload = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.MultipartUpload"]]]]
    MultipartUploadPart = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.MultipartUploadPart"]]]]
    Object = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.Object"]]]]
    ObjectAcl = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ObjectAcl"]]]]
    ObjectSummary = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ObjectSummary"]]]]
    ObjectVersion = Annotated[object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ObjectVersion"]]]]
    ServiceResourceBucketsCollection = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.ServiceResourceBucketsCollection"]]]
    ]
    BucketMultipartUploadsCollection = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketMultipartUploadsCollection"]]]
    ]
    BucketObjectVersionsCollection = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketObjectVersionsCollection"]]]
    ]
    BucketObjectsCollection = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.BucketObjectsCollection"]]]
    ]
    MultipartUploadPartsCollection = Annotated[
        object, IsAttr["__class__", IsAttr["__name__", IsEqual["s3.MultipartUploadPartsCollection"]]]
    ]
