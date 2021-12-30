from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_sqs import (
        ListDeadLetterSourceQueuesPaginator,
        ListQueuesPaginator,
        SQSClient,
    )
    from mypy_boto3_sqs.service_resource import (
        Message,
        Queue,
        QueueDeadLetterSourceQueuesCollection,
        SQSServiceResource,
        ServiceResourceQueuesCollection,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    ListDeadLetterSourceQueuesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["SQS.Paginator.ListDeadLetterSourceQueues"]],
        ],
    ]

    ListQueuesPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["SQS.Paginator.ListQueues"]]],
    ]

    Message = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["sqs.Message"]]]
    ]

    Queue = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["sqs.Queue"]]]
    ]

    QueueDeadLetterSourceQueuesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["sqs.Queue.dead_letter_source_queuesCollection"]
            ],
        ],
    ]

    SQSClient = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["SQS"]]]
    ]

    SQSServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sqs.ServiceResource"]]],
    ]

    ServiceResourceQueuesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sqs.queuesCollection"]]],
    ]
