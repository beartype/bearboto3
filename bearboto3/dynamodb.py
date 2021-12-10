from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_dynamodb import (
        DynamoDBClient,
        ListBackupsPaginator,
        ListTablesPaginator,
        ListTagsOfResourcePaginator,
        QueryPaginator,
        ScanPaginator,
        TableExistsWaiter,
        TableNotExistsWaiter,
    )
    from mypy_boto3_dynamodb.service_resource import (
        DynamoDBServiceResource,
        ServiceResourceTablesCollection,
        Table,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    DynamoDBClient = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["DynamoDB"]]]
    ]

    DynamoDBServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["dynamodb.ServiceResource"]]],
    ]

    ListBackupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["DynamoDB.Paginator.ListBackups"]]
        ],
    ]

    ListTablesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["DynamoDB.Paginator.ListTables"]]
        ],
    ]

    ListTagsOfResourcePaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["DynamoDB.Paginator.ListTagsOfResource"]],
        ],
    ]

    QueryPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["DynamoDB.Paginator.Query"]]],
    ]

    ScanPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["DynamoDB.Paginator.Scan"]]],
    ]

    ServiceResourceTablesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["dynamodb.tablesCollection"]]],
    ]

    Table = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["dynamodb.Table"]]],
    ]

    TableExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["DynamoDB.Waiter.TableExists"]]],
    ]

    TableNotExistsWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["DynamoDB.Waiter.TableNotExists"]]
        ],
    ]
