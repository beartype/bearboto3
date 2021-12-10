from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_lambda import (
        FunctionActiveWaiter,
        FunctionExistsWaiter,
        FunctionUpdatedWaiter,
        LambdaClient,
        ListAliasesPaginator,
        ListCodeSigningConfigsPaginator,
        ListEventSourceMappingsPaginator,
        ListFunctionEventInvokeConfigsPaginator,
        ListFunctionsByCodeSigningConfigPaginator,
        ListFunctionsPaginator,
        ListLayerVersionsPaginator,
        ListLayersPaginator,
        ListProvisionedConcurrencyConfigsPaginator,
        ListVersionsByFunctionPaginator,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    FunctionActiveWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["Lambda.Waiter.FunctionActive"]]
        ],
    ]

    FunctionExistsWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["Lambda.Waiter.FunctionExists"]]
        ],
    ]

    FunctionUpdatedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["Lambda.Waiter.FunctionUpdated"]]
        ],
    ]

    LambdaClient = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["Lambda"]]]
    ]

    ListAliasesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["Lambda.Paginator.ListAliases"]]
        ],
    ]

    ListCodeSigningConfigsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["Lambda.Paginator.ListCodeSigningConfigs"]],
        ],
    ]

    ListEventSourceMappingsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["Lambda.Paginator.ListEventSourceMappings"]],
        ],
    ]

    ListFunctionEventInvokeConfigsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["Lambda.Paginator.ListFunctionEventInvokeConfigs"]
            ],
        ],
    ]

    ListFunctionsByCodeSigningConfigPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["Lambda.Paginator.ListFunctionsByCodeSigningConfig"]
            ],
        ],
    ]

    ListFunctionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["Lambda.Paginator.ListFunctions"]]
        ],
    ]

    ListLayerVersionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["Lambda.Paginator.ListLayerVersions"]],
        ],
    ]

    ListLayersPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["Lambda.Paginator.ListLayers"]]],
    ]

    ListProvisionedConcurrencyConfigsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["Lambda.Paginator.ListProvisionedConcurrencyConfigs"],
            ],
        ],
    ]

    ListVersionsByFunctionPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["Lambda.Paginator.ListVersionsByFunction"]],
        ],
    ]
