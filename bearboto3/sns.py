from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_sns import (
        ListEndpointsByPlatformApplicationPaginator,
        ListOriginationNumbersPaginator,
        ListPhoneNumbersOptedOutPaginator,
        ListPlatformApplicationsPaginator,
        ListSMSSandboxPhoneNumbersPaginator,
        ListSubscriptionsByTopicPaginator,
        ListSubscriptionsPaginator,
        ListTopicsPaginator,
        SNSClient,
    )
    from mypy_boto3_sns.service_resource import (
        PlatformApplication,
        PlatformApplicationEndpointsCollection,
        PlatformEndpoint,
        SNSServiceResource,
        ServiceResourcePlatformApplicationsCollection,
        ServiceResourceSubscriptionsCollection,
        ServiceResourceTopicsCollection,
        Subscription,
        Topic,
        TopicSubscriptionsCollection,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    ListEndpointsByPlatformApplicationPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["SNS.Paginator.ListEndpointsByPlatformApplication"]
            ],
        ],
    ]

    ListOriginationNumbersPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["SNS.Paginator.ListOriginationNumbers"]],
        ],
    ]

    ListPhoneNumbersOptedOutPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["SNS.Paginator.ListPhoneNumbersOptedOut"]],
        ],
    ]

    ListPlatformApplicationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["SNS.Paginator.ListPlatformApplications"]],
        ],
    ]

    ListSMSSandboxPhoneNumbersPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["SNS.Paginator.ListSMSSandboxPhoneNumbers"]],
        ],
    ]

    ListSubscriptionsByTopicPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["SNS.Paginator.ListSubscriptionsByTopic"]],
        ],
    ]

    ListSubscriptionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["SNS.Paginator.ListSubscriptions"]]
        ],
    ]

    ListTopicsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["SNS.Paginator.ListTopics"]]],
    ]

    PlatformApplication = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sns.PlatformApplication"]]],
    ]

    PlatformApplicationEndpointsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["sns.PlatformApplication.endpointsCollection"]],
        ],
    ]

    PlatformEndpoint = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sns.PlatformEndpoint"]]],
    ]

    SNSClient = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["SNS"]]]
    ]

    SNSServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sns.ServiceResource"]]],
    ]

    ServiceResourcePlatformApplicationsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["sns.platform_applicationsCollection"]],
        ],
    ]

    ServiceResourceSubscriptionsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sns.subscriptionsCollection"]]],
    ]

    ServiceResourceTopicsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sns.topicsCollection"]]],
    ]

    Subscription = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["sns.Subscription"]]],
    ]

    Topic = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["sns.Topic"]]]
    ]

    TopicSubscriptionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["sns.Topic.subscriptionsCollection"]],
        ],
    ]
