from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_ec2 import (
        BundleTaskCompleteWaiter,
        ConversionTaskCancelledWaiter,
        ConversionTaskCompletedWaiter,
        ConversionTaskDeletedWaiter,
        CustomerGatewayAvailableWaiter,
        DescribeAddressesAttributePaginator,
        DescribeByoipCidrsPaginator,
        DescribeCapacityReservationFleetsPaginator,
        DescribeCapacityReservationsPaginator,
        DescribeCarrierGatewaysPaginator,
        DescribeClassicLinkInstancesPaginator,
        DescribeClientVpnAuthorizationRulesPaginator,
        DescribeClientVpnConnectionsPaginator,
        DescribeClientVpnEndpointsPaginator,
        DescribeClientVpnRoutesPaginator,
        DescribeClientVpnTargetNetworksPaginator,
        DescribeCoipPoolsPaginator,
        DescribeDhcpOptionsPaginator,
        DescribeEgressOnlyInternetGatewaysPaginator,
        DescribeExportImageTasksPaginator,
        DescribeFastSnapshotRestoresPaginator,
        DescribeFleetsPaginator,
        DescribeFlowLogsPaginator,
        DescribeFpgaImagesPaginator,
        DescribeHostReservationOfferingsPaginator,
        DescribeHostReservationsPaginator,
        DescribeHostsPaginator,
        DescribeIamInstanceProfileAssociationsPaginator,
        DescribeImportImageTasksPaginator,
        DescribeImportSnapshotTasksPaginator,
        DescribeInstanceCreditSpecificationsPaginator,
        DescribeInstanceEventWindowsPaginator,
        DescribeInstancesPaginator,
        DescribeInstanceStatusPaginator,
        DescribeInstanceTypeOfferingsPaginator,
        DescribeInstanceTypesPaginator,
        DescribeInternetGatewaysPaginator,
        DescribeIpv6PoolsPaginator,
        DescribeLaunchTemplatesPaginator,
        DescribeLaunchTemplateVersionsPaginator,
        DescribeLocalGatewayRouteTablesPaginator,
        DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
        DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
        DescribeLocalGatewaysPaginator,
        DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
        DescribeLocalGatewayVirtualInterfacesPaginator,
        DescribeManagedPrefixListsPaginator,
        DescribeMovingAddressesPaginator,
        DescribeNatGatewaysPaginator,
        DescribeNetworkAclsPaginator,
        DescribeNetworkInsightsAnalysesPaginator,
        DescribeNetworkInsightsPathsPaginator,
        DescribeNetworkInterfacePermissionsPaginator,
        DescribeNetworkInterfacesPaginator,
        DescribePrefixListsPaginator,
        DescribePrincipalIdFormatPaginator,
        DescribePublicIpv4PoolsPaginator,
        DescribeReplaceRootVolumeTasksPaginator,
        DescribeReservedInstancesModificationsPaginator,
        DescribeReservedInstancesOfferingsPaginator,
        DescribeRouteTablesPaginator,
        DescribeScheduledInstanceAvailabilityPaginator,
        DescribeScheduledInstancesPaginator,
        DescribeSecurityGroupRulesPaginator,
        DescribeSecurityGroupsPaginator,
        DescribeSnapshotsPaginator,
        DescribeSpotFleetInstancesPaginator,
        DescribeSpotFleetRequestsPaginator,
        DescribeSpotInstanceRequestsPaginator,
        DescribeSpotPriceHistoryPaginator,
        DescribeStaleSecurityGroupsPaginator,
        DescribeStoreImageTasksPaginator,
        DescribeSubnetsPaginator,
        DescribeTagsPaginator,
        DescribeTrafficMirrorFiltersPaginator,
        DescribeTrafficMirrorSessionsPaginator,
        DescribeTrafficMirrorTargetsPaginator,
        DescribeTransitGatewayAttachmentsPaginator,
        DescribeTransitGatewayConnectPeersPaginator,
        DescribeTransitGatewayConnectsPaginator,
        DescribeTransitGatewayMulticastDomainsPaginator,
        DescribeTransitGatewayPeeringAttachmentsPaginator,
        DescribeTransitGatewayRouteTablesPaginator,
        DescribeTransitGatewaysPaginator,
        DescribeTransitGatewayVpcAttachmentsPaginator,
        DescribeTrunkInterfaceAssociationsPaginator,
        DescribeVolumesModificationsPaginator,
        DescribeVolumesPaginator,
        DescribeVolumeStatusPaginator,
        DescribeVpcClassicLinkDnsSupportPaginator,
        DescribeVpcEndpointConnectionNotificationsPaginator,
        DescribeVpcEndpointConnectionsPaginator,
        DescribeVpcEndpointServiceConfigurationsPaginator,
        DescribeVpcEndpointServicePermissionsPaginator,
        DescribeVpcEndpointServicesPaginator,
        DescribeVpcEndpointsPaginator,
        DescribeVpcPeeringConnectionsPaginator,
        DescribeVpcsPaginator,
        EC2Client,
        ExportTaskCancelledWaiter,
        ExportTaskCompletedWaiter,
        GetAssociatedIpv6PoolCidrsPaginator,
        GetGroupsForCapacityReservationPaginator,
        GetInstanceTypesFromInstanceRequirementsPaginator,
        GetManagedPrefixListAssociationsPaginator,
        GetManagedPrefixListEntriesPaginator,
        GetSpotPlacementScoresPaginator,
        GetTransitGatewayAttachmentPropagationsPaginator,
        GetTransitGatewayMulticastDomainAssociationsPaginator,
        GetTransitGatewayPrefixListReferencesPaginator,
        GetTransitGatewayRouteTableAssociationsPaginator,
        GetTransitGatewayRouteTablePropagationsPaginator,
        GetVpnConnectionDeviceTypesPaginator,
        ImageAvailableWaiter,
        ImageExistsWaiter,
        InstanceExistsWaiter,
        InstanceRunningWaiter,
        InstanceStatusOkWaiter,
        InstanceStoppedWaiter,
        InstanceTerminatedWaiter,
        KeyPairExistsWaiter,
        NatGatewayAvailableWaiter,
        NetworkInterfaceAvailableWaiter,
        PasswordDataAvailableWaiter,
        SearchLocalGatewayRoutesPaginator,
        SearchTransitGatewayMulticastGroupsPaginator,
        SecurityGroupExistsWaiter,
        SnapshotCompletedWaiter,
        SpotInstanceRequestFulfilledWaiter,
        SubnetAvailableWaiter,
        SystemStatusOkWaiter,
        VolumeAvailableWaiter,
        VolumeDeletedWaiter,
        VolumeInUseWaiter,
        VpcAvailableWaiter,
        VpcExistsWaiter,
        VpcPeeringConnectionDeletedWaiter,
        VpcPeeringConnectionExistsWaiter,
        VpnConnectionAvailableWaiter,
        VpnConnectionDeletedWaiter,
    )
    from mypy_boto3_ec2.service_resource import (
        ClassicAddress,
        DhcpOptions,
        EC2ServiceResource,
        Image,
        Instance,
        InstanceVolumesCollection,
        InstanceVpcAddressesCollection,
        InternetGateway,
        KeyPair,
        KeyPairInfo,
        NetworkAcl,
        NetworkInterface,
        NetworkInterfaceAssociation,
        PlacementGroup,
        PlacementGroupInstancesCollection,
        Route,
        RouteTable,
        RouteTableAssociation,
        SecurityGroup,
        ServiceResourceClassicAddressesCollection,
        ServiceResourceDhcpOptionsSetsCollection,
        ServiceResourceImagesCollection,
        ServiceResourceInstancesCollection,
        ServiceResourceInternetGatewaysCollection,
        ServiceResourceKeyPairsCollection,
        ServiceResourceNetworkAclsCollection,
        ServiceResourceNetworkInterfacesCollection,
        ServiceResourcePlacementGroupsCollection,
        ServiceResourceRouteTablesCollection,
        ServiceResourceSecurityGroupsCollection,
        ServiceResourceSnapshotsCollection,
        ServiceResourceSubnetsCollection,
        ServiceResourceVolumesCollection,
        ServiceResourceVpcAddressesCollection,
        ServiceResourceVpcPeeringConnectionsCollection,
        ServiceResourceVpcsCollection,
        Snapshot,
        Subnet,
        SubnetInstancesCollection,
        SubnetNetworkInterfacesCollection,
        Tag,
        Volume,
        VolumeSnapshotsCollection,
        Vpc,
        VpcAcceptedVpcPeeringConnectionsCollection,
        VpcAddress,
        VpcInstancesCollection,
        VpcInternetGatewaysCollection,
        VpcNetworkAclsCollection,
        VpcNetworkInterfacesCollection,
        VpcPeeringConnection,
        VpcRequestedVpcPeeringConnectionsCollection,
        VpcRouteTablesCollection,
        VpcSecurityGroupsCollection,
        VpcSubnetsCollection,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    BundleTaskCompleteWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.BundleTaskComplete"]]
        ],
    ]

    ClassicAddress = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.ClassicAddress"]]],
    ]

    ConversionTaskCancelledWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.ConversionTaskCancelled"]],
        ],
    ]

    ConversionTaskCompletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.ConversionTaskCompleted"]],
        ],
    ]

    ConversionTaskDeletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ConversionTaskDeleted"]]
        ],
    ]

    CustomerGatewayAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.CustomerGatewayAvailable"]],
        ],
    ]

    DescribeAddressesAttributePaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeAddressesAttribute"]],
        ],
    ]

    DescribeByoipCidrsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeByoipCidrs"]]
        ],
    ]

    DescribeCapacityReservationFleetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeCapacityReservationFleets"]
            ],
        ],
    ]

    DescribeCapacityReservationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeCapacityReservations"]],
        ],
    ]

    DescribeCarrierGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeCarrierGateways"]],
        ],
    ]

    DescribeClassicLinkInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClassicLinkInstances"]],
        ],
    ]

    DescribeClientVpnAuthorizationRulesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeClientVpnAuthorizationRules"]
            ],
        ],
    ]

    DescribeClientVpnConnectionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClientVpnConnections"]],
        ],
    ]

    DescribeClientVpnEndpointsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClientVpnEndpoints"]],
        ],
    ]

    DescribeClientVpnRoutesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeClientVpnRoutes"]],
        ],
    ]

    DescribeClientVpnTargetNetworksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeClientVpnTargetNetworks"]
            ],
        ],
    ]

    DescribeCoipPoolsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeCoipPools"]]
        ],
    ]

    DescribeDhcpOptionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeDhcpOptions"]],
        ],
    ]

    DescribeEgressOnlyInternetGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeEgressOnlyInternetGateways"]
            ],
        ],
    ]

    DescribeExportImageTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeExportImageTasks"]],
        ],
    ]

    DescribeFastSnapshotRestoresPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFastSnapshotRestores"]],
        ],
    ]

    DescribeFleetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFleets"]]
        ],
    ]

    DescribeFlowLogsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFlowLogs"]]
        ],
    ]

    DescribeFpgaImagesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeFpgaImages"]]
        ],
    ]

    DescribeHostReservationOfferingsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeHostReservationOfferings"]
            ],
        ],
    ]

    DescribeHostReservationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeHostReservations"]],
        ],
    ]

    DescribeHostsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeHosts"]]],
    ]

    DescribeIamInstanceProfileAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeIamInstanceProfileAssociations"],
            ],
        ],
    ]

    DescribeImportImageTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeImportImageTasks"]],
        ],
    ]

    DescribeImportSnapshotTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeImportSnapshotTasks"]],
        ],
    ]

    DescribeInstanceCreditSpecificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeInstanceCreditSpecifications"],
            ],
        ],
    ]

    DescribeInstanceEventWindowsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceEventWindows"]],
        ],
    ]

    DescribeInstanceStatusPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceStatus"]],
        ],
    ]

    DescribeInstanceTypeOfferingsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceTypeOfferings"]],
        ],
    ]

    DescribeInstanceTypesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstanceTypes"]],
        ],
    ]

    DescribeInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInstances"]]
        ],
    ]

    DescribeInternetGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeInternetGateways"]],
        ],
    ]

    DescribeIpv6PoolsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeIpv6Pools"]]
        ],
    ]

    DescribeLaunchTemplateVersionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeLaunchTemplateVersions"]],
        ],
    ]

    DescribeLaunchTemplatesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeLaunchTemplates"]],
        ],
    ]

    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual[
                    "EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations"
                ],
            ],
        ],
    ]

    DescribeLocalGatewayRouteTableVpcAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations"],
            ],
        ],
    ]

    DescribeLocalGatewayRouteTablesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeLocalGatewayRouteTables"]
            ],
        ],
    ]

    DescribeLocalGatewayVirtualInterfaceGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups"],
            ],
        ],
    ]

    DescribeLocalGatewayVirtualInterfacesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeLocalGatewayVirtualInterfaces"],
            ],
        ],
    ]

    DescribeLocalGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeLocalGateways"]],
        ],
    ]

    DescribeManagedPrefixListsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeManagedPrefixLists"]],
        ],
    ]

    DescribeMovingAddressesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeMovingAddresses"]],
        ],
    ]

    DescribeNatGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNatGateways"]],
        ],
    ]

    DescribeNetworkAclsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNetworkAcls"]],
        ],
    ]

    DescribeNetworkInsightsAnalysesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeNetworkInsightsAnalyses"]
            ],
        ],
    ]

    DescribeNetworkInsightsPathsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNetworkInsightsPaths"]],
        ],
    ]

    DescribeNetworkInterfacePermissionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeNetworkInterfacePermissions"]
            ],
        ],
    ]

    DescribeNetworkInterfacesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeNetworkInterfaces"]],
        ],
    ]

    DescribePrefixListsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribePrefixLists"]],
        ],
    ]

    DescribePrincipalIdFormatPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribePrincipalIdFormat"]],
        ],
    ]

    DescribePublicIpv4PoolsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribePublicIpv4Pools"]],
        ],
    ]

    DescribeReplaceRootVolumeTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeReplaceRootVolumeTasks"]],
        ],
    ]

    DescribeReservedInstancesModificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeReservedInstancesModifications"],
            ],
        ],
    ]

    DescribeReservedInstancesOfferingsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeReservedInstancesOfferings"]
            ],
        ],
    ]

    DescribeRouteTablesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeRouteTables"]],
        ],
    ]

    DescribeScheduledInstanceAvailabilityPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeScheduledInstanceAvailability"],
            ],
        ],
    ]

    DescribeScheduledInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeScheduledInstances"]],
        ],
    ]

    DescribeSecurityGroupRulesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSecurityGroupRules"]],
        ],
    ]

    DescribeSecurityGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSecurityGroups"]],
        ],
    ]

    DescribeSnapshotsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSnapshots"]]
        ],
    ]

    DescribeSpotFleetInstancesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotFleetInstances"]],
        ],
    ]

    DescribeSpotFleetRequestsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotFleetRequests"]],
        ],
    ]

    DescribeSpotInstanceRequestsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotInstanceRequests"]],
        ],
    ]

    DescribeSpotPriceHistoryPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSpotPriceHistory"]],
        ],
    ]

    DescribeStaleSecurityGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeStaleSecurityGroups"]],
        ],
    ]

    DescribeStoreImageTasksPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeStoreImageTasks"]],
        ],
    ]

    DescribeSubnetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeSubnets"]]
        ],
    ]

    DescribeTagsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTags"]]],
    ]

    DescribeTrafficMirrorFiltersPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTrafficMirrorFilters"]],
        ],
    ]

    DescribeTrafficMirrorSessionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTrafficMirrorSessions"]],
        ],
    ]

    DescribeTrafficMirrorTargetsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTrafficMirrorTargets"]],
        ],
    ]

    DescribeTransitGatewayAttachmentsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayAttachments"]
            ],
        ],
    ]

    DescribeTransitGatewayConnectPeersPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayConnectPeers"]
            ],
        ],
    ]

    DescribeTransitGatewayConnectsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayConnects"]],
        ],
    ]

    DescribeTransitGatewayMulticastDomainsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeTransitGatewayMulticastDomains"],
            ],
        ],
    ]

    DescribeTransitGatewayPeeringAttachmentsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeTransitGatewayPeeringAttachments"],
            ],
        ],
    ]

    DescribeTransitGatewayRouteTablesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTransitGatewayRouteTables"]
            ],
        ],
    ]

    DescribeTransitGatewayVpcAttachmentsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeTransitGatewayVpcAttachments"],
            ],
        ],
    ]

    DescribeTransitGatewaysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeTransitGateways"]],
        ],
    ]

    DescribeTrunkInterfaceAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeTrunkInterfaceAssociations"]
            ],
        ],
    ]

    DescribeVolumeStatusPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVolumeStatus"]],
        ],
    ]

    DescribeVolumesModificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVolumesModifications"]],
        ],
    ]

    DescribeVolumesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVolumes"]]
        ],
    ]

    DescribeVpcClassicLinkDnsSupportPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.DescribeVpcClassicLinkDnsSupport"]
            ],
        ],
    ]

    DescribeVpcEndpointConnectionNotificationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeVpcEndpointConnectionNotifications"],
            ],
        ],
    ]

    DescribeVpcEndpointConnectionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcEndpointConnections"]],
        ],
    ]

    DescribeVpcEndpointServiceConfigurationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeVpcEndpointServiceConfigurations"],
            ],
        ],
    ]

    DescribeVpcEndpointServicePermissionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.DescribeVpcEndpointServicePermissions"],
            ],
        ],
    ]

    DescribeVpcEndpointServicesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcEndpointServices"]],
        ],
    ]

    DescribeVpcEndpointsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcEndpoints"]],
        ],
    ]

    DescribeVpcPeeringConnectionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcPeeringConnections"]],
        ],
    ]

    DescribeVpcsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Paginator.DescribeVpcs"]]],
    ]

    DhcpOptions = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.DhcpOptions"]]],
    ]

    EC2Client = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2"]]]
    ]

    EC2ServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.ServiceResource"]]],
    ]

    ExportTaskCancelledWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ExportTaskCancelled"]]
        ],
    ]

    ExportTaskCompletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ExportTaskCompleted"]]
        ],
    ]

    GetAssociatedIpv6PoolCidrsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetAssociatedIpv6PoolCidrs"]],
        ],
    ]

    GetGroupsForCapacityReservationPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.GetGroupsForCapacityReservation"]
            ],
        ],
    ]

    GetInstanceTypesFromInstanceRequirementsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetInstanceTypesFromInstanceRequirements"],
            ],
        ],
    ]

    GetManagedPrefixListAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.GetManagedPrefixListAssociations"]
            ],
        ],
    ]

    GetManagedPrefixListEntriesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetManagedPrefixListEntries"]],
        ],
    ]

    GetSpotPlacementScoresPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetSpotPlacementScores"]],
        ],
    ]

    GetTransitGatewayAttachmentPropagationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayAttachmentPropagations"],
            ],
        ],
    ]

    GetTransitGatewayMulticastDomainAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayMulticastDomainAssociations"],
            ],
        ],
    ]

    GetTransitGatewayPrefixListReferencesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayPrefixListReferences"],
            ],
        ],
    ]

    GetTransitGatewayRouteTableAssociationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayRouteTableAssociations"],
            ],
        ],
    ]

    GetTransitGatewayRouteTablePropagationsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["EC2.Paginator.GetTransitGatewayRouteTablePropagations"],
            ],
        ],
    ]

    GetVpnConnectionDeviceTypesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.GetVpnConnectionDeviceTypes"]],
        ],
    ]

    Image = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Image"]]]
    ]

    ImageAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ImageAvailable"]]],
    ]

    ImageExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.ImageExists"]]],
    ]

    Instance = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Instance"]]],
    ]

    InstanceExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceExists"]]],
    ]

    InstanceRunningWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceRunning"]]],
    ]

    InstanceStatusOkWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceStatusOk"]]],
    ]

    InstanceStoppedWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceStopped"]]],
    ]

    InstanceTerminatedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.InstanceTerminated"]]
        ],
    ]

    InstanceVolumesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Instance.volumesCollection"]]
        ],
    ]

    InstanceVpcAddressesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Instance.vpc_addressesCollection"]],
        ],
    ]

    InternetGateway = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.InternetGateway"]]],
    ]

    KeyPairExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.KeyPairExists"]]],
    ]

    KeyPairInfo = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.KeyPairInfo"]]],
    ]

    # `KeyPair` is not an actual type in boto. The type is `KeyPairInfo`,
    # but it is created via `service_resource.KeyPair()`.
    # See https://github.com/boto/boto3/issues/1945
    KeyPair = KeyPairInfo

    NatGatewayAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.NatGatewayAvailable"]]
        ],
    ]

    NetworkAcl = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.NetworkAcl"]]],
    ]

    NetworkInterface = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.NetworkInterface"]]],
    ]

    NetworkInterfaceAssociation = Annotated[
        ServiceResource,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.NetworkInterfaceAssociation"]]
        ],
    ]

    NetworkInterfaceAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.NetworkInterfaceAvailable"]],
        ],
    ]

    PasswordDataAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.PasswordDataAvailable"]]
        ],
    ]

    PlacementGroup = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.PlacementGroup"]]],
    ]

    PlacementGroupInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.PlacementGroup.instancesCollection"]],
        ],
    ]

    Route = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Route"]]]
    ]

    RouteTable = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.RouteTable"]]],
    ]

    RouteTableAssociation = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.RouteTableAssociation"]]],
    ]

    SearchLocalGatewayRoutesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Paginator.SearchLocalGatewayRoutes"]],
        ],
    ]

    SearchTransitGatewayMulticastGroupsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["EC2.Paginator.SearchTransitGatewayMulticastGroups"]
            ],
        ],
    ]

    SecurityGroup = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.SecurityGroup"]]],
    ]

    SecurityGroupExistsWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SecurityGroupExists"]]
        ],
    ]

    ServiceResourceClassicAddressesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.classic_addressesCollection"]]
        ],
    ]

    ServiceResourceDhcpOptionsSetsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.dhcp_options_setsCollection"]]
        ],
    ]

    ServiceResourceImagesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.imagesCollection"]]],
    ]

    ServiceResourceInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.instancesCollection"]]],
    ]

    ServiceResourceInternetGatewaysCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.internet_gatewaysCollection"]]
        ],
    ]

    ServiceResourceKeyPairsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.key_pairsCollection"]]],
    ]

    ServiceResourceNetworkAclsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.network_aclsCollection"]]],
    ]

    ServiceResourceNetworkInterfacesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.network_interfacesCollection"]]
        ],
    ]

    ServiceResourcePlacementGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.placement_groupsCollection"]]
        ],
    ]

    ServiceResourceRouteTablesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.route_tablesCollection"]]],
    ]

    ServiceResourceSecurityGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.security_groupsCollection"]]
        ],
    ]

    ServiceResourceSnapshotsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.snapshotsCollection"]]],
    ]

    ServiceResourceSubnetsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.subnetsCollection"]]],
    ]

    ServiceResourceVolumesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.volumesCollection"]]],
    ]

    ServiceResourceVpcAddressesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.vpc_addressesCollection"]]],
    ]

    ServiceResourceVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.vpc_peering_connectionsCollection"]],
        ],
    ]

    ServiceResourceVpcsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.vpcsCollection"]]],
    ]

    Snapshot = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Snapshot"]]],
    ]

    SnapshotCompletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SnapshotCompleted"]]
        ],
    ]

    SpotInstanceRequestFulfilledWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.SpotInstanceRequestFulfilled"]],
        ],
    ]

    Subnet = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Subnet"]]]
    ]

    SubnetAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SubnetAvailable"]]],
    ]

    SubnetInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Subnet.instancesCollection"]]
        ],
    ]

    SubnetNetworkInterfacesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Subnet.network_interfacesCollection"]],
        ],
    ]

    SystemStatusOkWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.SystemStatusOk"]]],
    ]

    Tag = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Tag"]]]
    ]

    Volume = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Volume"]]]
    ]

    VolumeAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VolumeAvailable"]]],
    ]

    VolumeDeletedWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VolumeDeleted"]]],
    ]

    VolumeInUseWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VolumeInUse"]]],
    ]

    VolumeSnapshotsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Volume.snapshotsCollection"]]
        ],
    ]

    Vpc = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Vpc"]]]
    ]

    VpcAcceptedVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["ec2.Vpc.accepted_vpc_peering_connectionsCollection"],
            ],
        ],
    ]

    VpcAddress = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.VpcAddress"]]],
    ]

    VpcAvailableWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VpcAvailable"]]],
    ]

    VpcExistsWaiter = Annotated[
        Waiter, IsAttr["__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VpcExists"]]]
    ]

    VpcInstancesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Vpc.instancesCollection"]]],
    ]

    VpcInternetGatewaysCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Vpc.internet_gatewaysCollection"]],
        ],
    ]

    VpcNetworkAclsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Vpc.network_aclsCollection"]]
        ],
    ]

    VpcNetworkInterfacesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Vpc.network_interfacesCollection"]],
        ],
    ]

    VpcPeeringConnection = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.VpcPeeringConnection"]]],
    ]

    VpcPeeringConnectionDeletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.VpcPeeringConnectionDeleted"]],
        ],
    ]

    VpcPeeringConnectionExistsWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.VpcPeeringConnectionExists"]],
        ],
    ]

    VpcRequestedVpcPeeringConnectionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__",
                IsEqual["ec2.Vpc.requested_vpc_peering_connectionsCollection"],
            ],
        ],
    ]

    VpcRouteTablesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["ec2.Vpc.route_tablesCollection"]]
        ],
    ]

    VpcSecurityGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["ec2.Vpc.security_groupsCollection"]],
        ],
    ]

    VpcSubnetsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["ec2.Vpc.subnetsCollection"]]],
    ]

    VpnConnectionAvailableWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["EC2.Waiter.VpnConnectionAvailable"]],
        ],
    ]

    VpnConnectionDeletedWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["EC2.Waiter.VpnConnectionDeleted"]]
        ],
    ]
