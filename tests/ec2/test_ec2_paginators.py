import pytest
from bearboto3.ec2 import (
    DescribeRouteTablesPaginator,
    DescribeIamInstanceProfileAssociationsPaginator,
    DescribeInstanceStatusPaginator,
    DescribeInstancesPaginator,
    DescribeReservedInstancesOfferingsPaginator,
    DescribeReservedInstancesModificationsPaginator,
    DescribeSecurityGroupsPaginator,
    DescribeSnapshotsPaginator,
    DescribeSpotFleetInstancesPaginator,
    DescribeSpotFleetRequestsPaginator,
    DescribeSpotPriceHistoryPaginator,
    DescribeTagsPaginator,
    DescribeVolumeStatusPaginator,
    DescribeVolumesPaginator,
    DescribeNatGatewaysPaginator,
    DescribeNetworkInterfacesPaginator,
    DescribeVpcEndpointsPaginator,
    DescribeVpcEndpointServicesPaginator,
    DescribeVpcEndpointConnectionsPaginator,
    DescribeByoipCidrsPaginator,
    DescribeCapacityReservationsPaginator,
    DescribeClassicLinkInstancesPaginator,
    DescribeClientVpnAuthorizationRulesPaginator,
    DescribeClientVpnConnectionsPaginator,
    DescribeClientVpnEndpointsPaginator,
    DescribeClientVpnRoutesPaginator,
    DescribeClientVpnTargetNetworksPaginator,
    DescribeEgressOnlyInternetGatewaysPaginator,
    DescribeFleetsPaginator,
    DescribeFlowLogsPaginator,
    DescribeFpgaImagesPaginator,
    DescribeHostReservationOfferingsPaginator,
    DescribeHostReservationsPaginator,
    DescribeHostsPaginator,
    DescribeImportImageTasksPaginator,
    DescribeImportSnapshotTasksPaginator,
    DescribeInstanceCreditSpecificationsPaginator,
    DescribeLaunchTemplateVersionsPaginator,
    DescribeLaunchTemplatesPaginator,
    DescribeMovingAddressesPaginator,
    DescribeNetworkInterfacePermissionsPaginator,
    DescribePrefixListsPaginator,
    DescribePrincipalIdFormatPaginator,
    DescribePublicIpv4PoolsPaginator,
    DescribeScheduledInstanceAvailabilityPaginator,
    DescribeScheduledInstancesPaginator,
    DescribeStaleSecurityGroupsPaginator,
    DescribeTransitGatewayAttachmentsPaginator,
    DescribeTransitGatewayRouteTablesPaginator,
    DescribeTransitGatewayVpcAttachmentsPaginator,
    DescribeTransitGatewaysPaginator,
    DescribeVolumesModificationsPaginator,
    DescribeVpcClassicLinkDnsSupportPaginator,
    DescribeVpcEndpointConnectionNotificationsPaginator,
    DescribeVpcEndpointServiceConfigurationsPaginator,
    DescribeVpcEndpointServicePermissionsPaginator,
    DescribeVpcPeeringConnectionsPaginator,
    GetTransitGatewayAttachmentPropagationsPaginator,
    GetTransitGatewayRouteTableAssociationsPaginator,
    GetTransitGatewayRouteTablePropagationsPaginator,
    DescribeInternetGatewaysPaginator,
    DescribeNetworkAclsPaginator,
    DescribeVpcsPaginator,
    DescribeSpotInstanceRequestsPaginator,
    DescribeDhcpOptionsPaginator,
    DescribeSubnetsPaginator,
    DescribeTrafficMirrorFiltersPaginator,
    DescribeTrafficMirrorSessionsPaginator,
    DescribeTrafficMirrorTargetsPaginator,
    DescribeExportImageTasksPaginator,
    DescribeFastSnapshotRestoresPaginator,
    DescribeIpv6PoolsPaginator,
    GetAssociatedIpv6PoolCidrsPaginator,
    DescribeCoipPoolsPaginator,
    DescribeInstanceTypeOfferingsPaginator,
    DescribeInstanceTypesPaginator,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
    DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
    DescribeLocalGatewayRouteTablesPaginator,
    DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
    DescribeLocalGatewayVirtualInterfacesPaginator,
    DescribeLocalGatewaysPaginator,
    DescribeTransitGatewayMulticastDomainsPaginator,
    DescribeTransitGatewayPeeringAttachmentsPaginator,
    GetTransitGatewayMulticastDomainAssociationsPaginator,
    SearchLocalGatewayRoutesPaginator,
    SearchTransitGatewayMulticastGroupsPaginator,
    DescribeManagedPrefixListsPaginator,
    GetManagedPrefixListAssociationsPaginator,
    GetManagedPrefixListEntriesPaginator,
    GetGroupsForCapacityReservationPaginator,
    DescribeCarrierGatewaysPaginator,
    GetTransitGatewayPrefixListReferencesPaginator,
    DescribeNetworkInsightsAnalysesPaginator,
    DescribeNetworkInsightsPathsPaginator,
    DescribeTransitGatewayConnectPeersPaginator,
    DescribeTransitGatewayConnectsPaginator,
    DescribeAddressesAttributePaginator,
    DescribeReplaceRootVolumeTasksPaginator,
    DescribeStoreImageTasksPaginator,
    DescribeSecurityGroupRulesPaginator,
    DescribeInstanceEventWindowsPaginator,
    DescribeTrunkInterfaceAssociationsPaginator,
    GetVpnConnectionDeviceTypesPaginator,
    DescribeCapacityReservationFleetsPaginator,
    GetInstanceTypesFromInstanceRequirementsPaginator,
    GetSpotPlacementScoresPaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# DescribeRouteTablesPaginator
# ============================


def test_describe_route_tables_arg_pass(gen_describe_route_tables_paginator):
    @beartype
    def func(param: DescribeRouteTablesPaginator):
        pass

    func(gen_describe_route_tables_paginator)


def test_describe_route_tables_arg_fail(
    gen_describe_transit_gateway_attachments_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeRouteTablesPaginator):
            pass

        func(gen_describe_transit_gateway_attachments_paginator)


def test_describe_route_tables_return_pass(gen_describe_route_tables_paginator):
    @beartype
    def func() -> DescribeRouteTablesPaginator:
        return gen_describe_route_tables_paginator

    func()


def test_describe_route_tables_return_fail(
    gen_describe_transit_gateway_attachments_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeRouteTablesPaginator:
            return gen_describe_transit_gateway_attachments_paginator

        func()


# ============================
# DescribeIamInstanceProfileAssociationsPaginator
# ============================


def test_describe_iam_instance_profile_associations_arg_pass(
    gen_describe_iam_instance_profile_associations_paginator,
):
    @beartype
    def func(param: DescribeIamInstanceProfileAssociationsPaginator):
        pass

    func(gen_describe_iam_instance_profile_associations_paginator)


def test_describe_iam_instance_profile_associations_arg_fail(
    gen_describe_vpcs_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeIamInstanceProfileAssociationsPaginator):
            pass

        func(gen_describe_vpcs_paginator)


def test_describe_iam_instance_profile_associations_return_pass(
    gen_describe_iam_instance_profile_associations_paginator,
):
    @beartype
    def func() -> DescribeIamInstanceProfileAssociationsPaginator:
        return gen_describe_iam_instance_profile_associations_paginator

    func()


def test_describe_iam_instance_profile_associations_return_fail(
    gen_describe_vpcs_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeIamInstanceProfileAssociationsPaginator:
            return gen_describe_vpcs_paginator

        func()


# ============================
# DescribeInstanceStatusPaginator
# ============================


def test_describe_instance_status_arg_pass(gen_describe_instance_status_paginator):
    @beartype
    def func(param: DescribeInstanceStatusPaginator):
        pass

    func(gen_describe_instance_status_paginator)


def test_describe_instance_status_arg_fail(gen_search_local_gateway_routes_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeInstanceStatusPaginator):
            pass

        func(gen_search_local_gateway_routes_paginator)


def test_describe_instance_status_return_pass(gen_describe_instance_status_paginator):
    @beartype
    def func() -> DescribeInstanceStatusPaginator:
        return gen_describe_instance_status_paginator

    func()


def test_describe_instance_status_return_fail(
    gen_search_local_gateway_routes_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeInstanceStatusPaginator:
            return gen_search_local_gateway_routes_paginator

        func()


# ============================
# DescribeInstancesPaginator
# ============================


def test_describe_instances_arg_pass(gen_describe_instances_paginator):
    @beartype
    def func(param: DescribeInstancesPaginator):
        pass

    func(gen_describe_instances_paginator)


def test_describe_instances_arg_fail(gen_describe_replace_root_volume_tasks_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeInstancesPaginator):
            pass

        func(gen_describe_replace_root_volume_tasks_paginator)


def test_describe_instances_return_pass(gen_describe_instances_paginator):
    @beartype
    def func() -> DescribeInstancesPaginator:
        return gen_describe_instances_paginator

    func()


def test_describe_instances_return_fail(
    gen_describe_replace_root_volume_tasks_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeInstancesPaginator:
            return gen_describe_replace_root_volume_tasks_paginator

        func()


# ============================
# DescribeReservedInstancesOfferingsPaginator
# ============================


def test_describe_reserved_instances_offerings_arg_pass(
    gen_describe_reserved_instances_offerings_paginator,
):
    @beartype
    def func(param: DescribeReservedInstancesOfferingsPaginator):
        pass

    func(gen_describe_reserved_instances_offerings_paginator)


def test_describe_reserved_instances_offerings_arg_fail(
    gen_describe_trunk_interface_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeReservedInstancesOfferingsPaginator):
            pass

        func(gen_describe_trunk_interface_associations_paginator)


def test_describe_reserved_instances_offerings_return_pass(
    gen_describe_reserved_instances_offerings_paginator,
):
    @beartype
    def func() -> DescribeReservedInstancesOfferingsPaginator:
        return gen_describe_reserved_instances_offerings_paginator

    func()


def test_describe_reserved_instances_offerings_return_fail(
    gen_describe_trunk_interface_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeReservedInstancesOfferingsPaginator:
            return gen_describe_trunk_interface_associations_paginator

        func()


# ============================
# DescribeReservedInstancesModificationsPaginator
# ============================


def test_describe_reserved_instances_modifications_arg_pass(
    gen_describe_reserved_instances_modifications_paginator,
):
    @beartype
    def func(param: DescribeReservedInstancesModificationsPaginator):
        pass

    func(gen_describe_reserved_instances_modifications_paginator)


def test_describe_reserved_instances_modifications_arg_fail(
    gen_describe_dhcp_options_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeReservedInstancesModificationsPaginator):
            pass

        func(gen_describe_dhcp_options_paginator)


def test_describe_reserved_instances_modifications_return_pass(
    gen_describe_reserved_instances_modifications_paginator,
):
    @beartype
    def func() -> DescribeReservedInstancesModificationsPaginator:
        return gen_describe_reserved_instances_modifications_paginator

    func()


def test_describe_reserved_instances_modifications_return_fail(
    gen_describe_dhcp_options_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeReservedInstancesModificationsPaginator:
            return gen_describe_dhcp_options_paginator

        func()


# ============================
# DescribeSecurityGroupsPaginator
# ============================


def test_describe_security_groups_arg_pass(gen_describe_security_groups_paginator):
    @beartype
    def func(param: DescribeSecurityGroupsPaginator):
        pass

    func(gen_describe_security_groups_paginator)


def test_describe_security_groups_arg_fail(gen_describe_spot_fleet_instances_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSecurityGroupsPaginator):
            pass

        func(gen_describe_spot_fleet_instances_paginator)


def test_describe_security_groups_return_pass(gen_describe_security_groups_paginator):
    @beartype
    def func() -> DescribeSecurityGroupsPaginator:
        return gen_describe_security_groups_paginator

    func()


def test_describe_security_groups_return_fail(
    gen_describe_spot_fleet_instances_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSecurityGroupsPaginator:
            return gen_describe_spot_fleet_instances_paginator

        func()


# ============================
# DescribeSnapshotsPaginator
# ============================


def test_describe_snapshots_arg_pass(gen_describe_snapshots_paginator):
    @beartype
    def func(param: DescribeSnapshotsPaginator):
        pass

    func(gen_describe_snapshots_paginator)


def test_describe_snapshots_arg_fail(gen_describe_client_vpn_endpoints_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSnapshotsPaginator):
            pass

        func(gen_describe_client_vpn_endpoints_paginator)


def test_describe_snapshots_return_pass(gen_describe_snapshots_paginator):
    @beartype
    def func() -> DescribeSnapshotsPaginator:
        return gen_describe_snapshots_paginator

    func()


def test_describe_snapshots_return_fail(gen_describe_client_vpn_endpoints_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSnapshotsPaginator:
            return gen_describe_client_vpn_endpoints_paginator

        func()


# ============================
# DescribeSpotFleetInstancesPaginator
# ============================


def test_describe_spot_fleet_instances_arg_pass(
    gen_describe_spot_fleet_instances_paginator,
):
    @beartype
    def func(param: DescribeSpotFleetInstancesPaginator):
        pass

    func(gen_describe_spot_fleet_instances_paginator)


def test_describe_spot_fleet_instances_arg_fail(
    gen_describe_security_group_rules_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSpotFleetInstancesPaginator):
            pass

        func(gen_describe_security_group_rules_paginator)


def test_describe_spot_fleet_instances_return_pass(
    gen_describe_spot_fleet_instances_paginator,
):
    @beartype
    def func() -> DescribeSpotFleetInstancesPaginator:
        return gen_describe_spot_fleet_instances_paginator

    func()


def test_describe_spot_fleet_instances_return_fail(
    gen_describe_security_group_rules_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSpotFleetInstancesPaginator:
            return gen_describe_security_group_rules_paginator

        func()


# ============================
# DescribeSpotFleetRequestsPaginator
# ============================


def test_describe_spot_fleet_requests_arg_pass(
    gen_describe_spot_fleet_requests_paginator,
):
    @beartype
    def func(param: DescribeSpotFleetRequestsPaginator):
        pass

    func(gen_describe_spot_fleet_requests_paginator)


def test_describe_spot_fleet_requests_arg_fail(
    gen_describe_local_gateway_route_table_vpc_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSpotFleetRequestsPaginator):
            pass

        func(gen_describe_local_gateway_route_table_vpc_associations_paginator)


def test_describe_spot_fleet_requests_return_pass(
    gen_describe_spot_fleet_requests_paginator,
):
    @beartype
    def func() -> DescribeSpotFleetRequestsPaginator:
        return gen_describe_spot_fleet_requests_paginator

    func()


def test_describe_spot_fleet_requests_return_fail(
    gen_describe_local_gateway_route_table_vpc_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSpotFleetRequestsPaginator:
            return gen_describe_local_gateway_route_table_vpc_associations_paginator

        func()


# ============================
# DescribeSpotPriceHistoryPaginator
# ============================


def test_describe_spot_price_history_arg_pass(
    gen_describe_spot_price_history_paginator,
):
    @beartype
    def func(param: DescribeSpotPriceHistoryPaginator):
        pass

    func(gen_describe_spot_price_history_paginator)


def test_describe_spot_price_history_arg_fail(
    gen_describe_replace_root_volume_tasks_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSpotPriceHistoryPaginator):
            pass

        func(gen_describe_replace_root_volume_tasks_paginator)


def test_describe_spot_price_history_return_pass(
    gen_describe_spot_price_history_paginator,
):
    @beartype
    def func() -> DescribeSpotPriceHistoryPaginator:
        return gen_describe_spot_price_history_paginator

    func()


def test_describe_spot_price_history_return_fail(
    gen_describe_replace_root_volume_tasks_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSpotPriceHistoryPaginator:
            return gen_describe_replace_root_volume_tasks_paginator

        func()


# ============================
# DescribeTagsPaginator
# ============================


def test_describe_tags_arg_pass(gen_describe_tags_paginator):
    @beartype
    def func(param: DescribeTagsPaginator):
        pass

    func(gen_describe_tags_paginator)


def test_describe_tags_arg_fail(gen_describe_flow_logs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTagsPaginator):
            pass

        func(gen_describe_flow_logs_paginator)


def test_describe_tags_return_pass(gen_describe_tags_paginator):
    @beartype
    def func() -> DescribeTagsPaginator:
        return gen_describe_tags_paginator

    func()


def test_describe_tags_return_fail(gen_describe_flow_logs_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTagsPaginator:
            return gen_describe_flow_logs_paginator

        func()


# ============================
# DescribeVolumeStatusPaginator
# ============================


def test_describe_volume_status_arg_pass(gen_describe_volume_status_paginator):
    @beartype
    def func(param: DescribeVolumeStatusPaginator):
        pass

    func(gen_describe_volume_status_paginator)


def test_describe_volume_status_arg_fail(gen_describe_network_insights_paths_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVolumeStatusPaginator):
            pass

        func(gen_describe_network_insights_paths_paginator)


def test_describe_volume_status_return_pass(gen_describe_volume_status_paginator):
    @beartype
    def func() -> DescribeVolumeStatusPaginator:
        return gen_describe_volume_status_paginator

    func()


def test_describe_volume_status_return_fail(
    gen_describe_network_insights_paths_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVolumeStatusPaginator:
            return gen_describe_network_insights_paths_paginator

        func()


# ============================
# DescribeVolumesPaginator
# ============================


def test_describe_volumes_arg_pass(gen_describe_volumes_paginator):
    @beartype
    def func(param: DescribeVolumesPaginator):
        pass

    func(gen_describe_volumes_paginator)


def test_describe_volumes_arg_fail(gen_describe_instance_event_windows_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVolumesPaginator):
            pass

        func(gen_describe_instance_event_windows_paginator)


def test_describe_volumes_return_pass(gen_describe_volumes_paginator):
    @beartype
    def func() -> DescribeVolumesPaginator:
        return gen_describe_volumes_paginator

    func()


def test_describe_volumes_return_fail(gen_describe_instance_event_windows_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVolumesPaginator:
            return gen_describe_instance_event_windows_paginator

        func()


# ============================
# DescribeNatGatewaysPaginator
# ============================


def test_describe_nat_gateways_arg_pass(gen_describe_nat_gateways_paginator):
    @beartype
    def func(param: DescribeNatGatewaysPaginator):
        pass

    func(gen_describe_nat_gateways_paginator)


def test_describe_nat_gateways_arg_fail(
    gen_describe_scheduled_instance_availability_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeNatGatewaysPaginator):
            pass

        func(gen_describe_scheduled_instance_availability_paginator)


def test_describe_nat_gateways_return_pass(gen_describe_nat_gateways_paginator):
    @beartype
    def func() -> DescribeNatGatewaysPaginator:
        return gen_describe_nat_gateways_paginator

    func()


def test_describe_nat_gateways_return_fail(
    gen_describe_scheduled_instance_availability_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeNatGatewaysPaginator:
            return gen_describe_scheduled_instance_availability_paginator

        func()


# ============================
# DescribeNetworkInterfacesPaginator
# ============================


def test_describe_network_interfaces_arg_pass(
    gen_describe_network_interfaces_paginator,
):
    @beartype
    def func(param: DescribeNetworkInterfacesPaginator):
        pass

    func(gen_describe_network_interfaces_paginator)


def test_describe_network_interfaces_arg_fail(
    gen_describe_client_vpn_connections_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeNetworkInterfacesPaginator):
            pass

        func(gen_describe_client_vpn_connections_paginator)


def test_describe_network_interfaces_return_pass(
    gen_describe_network_interfaces_paginator,
):
    @beartype
    def func() -> DescribeNetworkInterfacesPaginator:
        return gen_describe_network_interfaces_paginator

    func()


def test_describe_network_interfaces_return_fail(
    gen_describe_client_vpn_connections_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeNetworkInterfacesPaginator:
            return gen_describe_client_vpn_connections_paginator

        func()


# ============================
# DescribeVpcEndpointsPaginator
# ============================


def test_describe_vpc_endpoints_arg_pass(gen_describe_vpc_endpoints_paginator):
    @beartype
    def func(param: DescribeVpcEndpointsPaginator):
        pass

    func(gen_describe_vpc_endpoints_paginator)


def test_describe_vpc_endpoints_arg_fail(gen_describe_byoip_cidrs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcEndpointsPaginator):
            pass

        func(gen_describe_byoip_cidrs_paginator)


def test_describe_vpc_endpoints_return_pass(gen_describe_vpc_endpoints_paginator):
    @beartype
    def func() -> DescribeVpcEndpointsPaginator:
        return gen_describe_vpc_endpoints_paginator

    func()


def test_describe_vpc_endpoints_return_fail(gen_describe_byoip_cidrs_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcEndpointsPaginator:
            return gen_describe_byoip_cidrs_paginator

        func()


# ============================
# DescribeVpcEndpointServicesPaginator
# ============================


def test_describe_vpc_endpoint_services_arg_pass(
    gen_describe_vpc_endpoint_services_paginator,
):
    @beartype
    def func(param: DescribeVpcEndpointServicesPaginator):
        pass

    func(gen_describe_vpc_endpoint_services_paginator)


def test_describe_vpc_endpoint_services_arg_fail(
    gen_describe_public_ipv4_pools_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcEndpointServicesPaginator):
            pass

        func(gen_describe_public_ipv4_pools_paginator)


def test_describe_vpc_endpoint_services_return_pass(
    gen_describe_vpc_endpoint_services_paginator,
):
    @beartype
    def func() -> DescribeVpcEndpointServicesPaginator:
        return gen_describe_vpc_endpoint_services_paginator

    func()


def test_describe_vpc_endpoint_services_return_fail(
    gen_describe_public_ipv4_pools_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcEndpointServicesPaginator:
            return gen_describe_public_ipv4_pools_paginator

        func()


# ============================
# DescribeVpcEndpointConnectionsPaginator
# ============================


def test_describe_vpc_endpoint_connections_arg_pass(
    gen_describe_vpc_endpoint_connections_paginator,
):
    @beartype
    def func(param: DescribeVpcEndpointConnectionsPaginator):
        pass

    func(gen_describe_vpc_endpoint_connections_paginator)


def test_describe_vpc_endpoint_connections_arg_fail(
    gen_describe_spot_instance_requests_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcEndpointConnectionsPaginator):
            pass

        func(gen_describe_spot_instance_requests_paginator)


def test_describe_vpc_endpoint_connections_return_pass(
    gen_describe_vpc_endpoint_connections_paginator,
):
    @beartype
    def func() -> DescribeVpcEndpointConnectionsPaginator:
        return gen_describe_vpc_endpoint_connections_paginator

    func()


def test_describe_vpc_endpoint_connections_return_fail(
    gen_describe_spot_instance_requests_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcEndpointConnectionsPaginator:
            return gen_describe_spot_instance_requests_paginator

        func()


# ============================
# DescribeByoipCidrsPaginator
# ============================


def test_describe_byoip_cidrs_arg_pass(gen_describe_byoip_cidrs_paginator):
    @beartype
    def func(param: DescribeByoipCidrsPaginator):
        pass

    func(gen_describe_byoip_cidrs_paginator)


def test_describe_byoip_cidrs_arg_fail(gen_get_associated_ipv6_pool_cidrs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeByoipCidrsPaginator):
            pass

        func(gen_get_associated_ipv6_pool_cidrs_paginator)


def test_describe_byoip_cidrs_return_pass(gen_describe_byoip_cidrs_paginator):
    @beartype
    def func() -> DescribeByoipCidrsPaginator:
        return gen_describe_byoip_cidrs_paginator

    func()


def test_describe_byoip_cidrs_return_fail(gen_get_associated_ipv6_pool_cidrs_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeByoipCidrsPaginator:
            return gen_get_associated_ipv6_pool_cidrs_paginator

        func()


# ============================
# DescribeCapacityReservationsPaginator
# ============================


def test_describe_capacity_reservations_arg_pass(
    gen_describe_capacity_reservations_paginator,
):
    @beartype
    def func(param: DescribeCapacityReservationsPaginator):
        pass

    func(gen_describe_capacity_reservations_paginator)


def test_describe_capacity_reservations_arg_fail(
    gen_describe_transit_gateway_connects_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeCapacityReservationsPaginator):
            pass

        func(gen_describe_transit_gateway_connects_paginator)


def test_describe_capacity_reservations_return_pass(
    gen_describe_capacity_reservations_paginator,
):
    @beartype
    def func() -> DescribeCapacityReservationsPaginator:
        return gen_describe_capacity_reservations_paginator

    func()


def test_describe_capacity_reservations_return_fail(
    gen_describe_transit_gateway_connects_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeCapacityReservationsPaginator:
            return gen_describe_transit_gateway_connects_paginator

        func()


# ============================
# DescribeClassicLinkInstancesPaginator
# ============================


def test_describe_classic_link_instances_arg_pass(
    gen_describe_classic_link_instances_paginator,
):
    @beartype
    def func(param: DescribeClassicLinkInstancesPaginator):
        pass

    func(gen_describe_classic_link_instances_paginator)


def test_describe_classic_link_instances_arg_fail(
    gen_describe_vpc_endpoint_service_permissions_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeClassicLinkInstancesPaginator):
            pass

        func(gen_describe_vpc_endpoint_service_permissions_paginator)


def test_describe_classic_link_instances_return_pass(
    gen_describe_classic_link_instances_paginator,
):
    @beartype
    def func() -> DescribeClassicLinkInstancesPaginator:
        return gen_describe_classic_link_instances_paginator

    func()


def test_describe_classic_link_instances_return_fail(
    gen_describe_vpc_endpoint_service_permissions_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeClassicLinkInstancesPaginator:
            return gen_describe_vpc_endpoint_service_permissions_paginator

        func()


# ============================
# DescribeClientVpnAuthorizationRulesPaginator
# ============================


def test_describe_client_vpn_authorization_rules_arg_pass(
    gen_describe_client_vpn_authorization_rules_paginator,
):
    @beartype
    def func(param: DescribeClientVpnAuthorizationRulesPaginator):
        pass

    func(gen_describe_client_vpn_authorization_rules_paginator)


def test_describe_client_vpn_authorization_rules_arg_fail(
    gen_describe_fpga_images_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeClientVpnAuthorizationRulesPaginator):
            pass

        func(gen_describe_fpga_images_paginator)


def test_describe_client_vpn_authorization_rules_return_pass(
    gen_describe_client_vpn_authorization_rules_paginator,
):
    @beartype
    def func() -> DescribeClientVpnAuthorizationRulesPaginator:
        return gen_describe_client_vpn_authorization_rules_paginator

    func()


def test_describe_client_vpn_authorization_rules_return_fail(
    gen_describe_fpga_images_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeClientVpnAuthorizationRulesPaginator:
            return gen_describe_fpga_images_paginator

        func()


# ============================
# DescribeClientVpnConnectionsPaginator
# ============================


def test_describe_client_vpn_connections_arg_pass(
    gen_describe_client_vpn_connections_paginator,
):
    @beartype
    def func(param: DescribeClientVpnConnectionsPaginator):
        pass

    func(gen_describe_client_vpn_connections_paginator)


def test_describe_client_vpn_connections_arg_fail(gen_describe_route_tables_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeClientVpnConnectionsPaginator):
            pass

        func(gen_describe_route_tables_paginator)


def test_describe_client_vpn_connections_return_pass(
    gen_describe_client_vpn_connections_paginator,
):
    @beartype
    def func() -> DescribeClientVpnConnectionsPaginator:
        return gen_describe_client_vpn_connections_paginator

    func()


def test_describe_client_vpn_connections_return_fail(
    gen_describe_route_tables_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeClientVpnConnectionsPaginator:
            return gen_describe_route_tables_paginator

        func()


# ============================
# DescribeClientVpnEndpointsPaginator
# ============================


def test_describe_client_vpn_endpoints_arg_pass(
    gen_describe_client_vpn_endpoints_paginator,
):
    @beartype
    def func(param: DescribeClientVpnEndpointsPaginator):
        pass

    func(gen_describe_client_vpn_endpoints_paginator)


def test_describe_client_vpn_endpoints_arg_fail(gen_describe_byoip_cidrs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeClientVpnEndpointsPaginator):
            pass

        func(gen_describe_byoip_cidrs_paginator)


def test_describe_client_vpn_endpoints_return_pass(
    gen_describe_client_vpn_endpoints_paginator,
):
    @beartype
    def func() -> DescribeClientVpnEndpointsPaginator:
        return gen_describe_client_vpn_endpoints_paginator

    func()


def test_describe_client_vpn_endpoints_return_fail(gen_describe_byoip_cidrs_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeClientVpnEndpointsPaginator:
            return gen_describe_byoip_cidrs_paginator

        func()


# ============================
# DescribeClientVpnRoutesPaginator
# ============================


def test_describe_client_vpn_routes_arg_pass(gen_describe_client_vpn_routes_paginator):
    @beartype
    def func(param: DescribeClientVpnRoutesPaginator):
        pass

    func(gen_describe_client_vpn_routes_paginator)


def test_describe_client_vpn_routes_arg_fail(gen_describe_snapshots_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeClientVpnRoutesPaginator):
            pass

        func(gen_describe_snapshots_paginator)


def test_describe_client_vpn_routes_return_pass(
    gen_describe_client_vpn_routes_paginator,
):
    @beartype
    def func() -> DescribeClientVpnRoutesPaginator:
        return gen_describe_client_vpn_routes_paginator

    func()


def test_describe_client_vpn_routes_return_fail(gen_describe_snapshots_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeClientVpnRoutesPaginator:
            return gen_describe_snapshots_paginator

        func()


# ============================
# DescribeClientVpnTargetNetworksPaginator
# ============================


def test_describe_client_vpn_target_networks_arg_pass(
    gen_describe_client_vpn_target_networks_paginator,
):
    @beartype
    def func(param: DescribeClientVpnTargetNetworksPaginator):
        pass

    func(gen_describe_client_vpn_target_networks_paginator)


def test_describe_client_vpn_target_networks_arg_fail(gen_describe_subnets_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeClientVpnTargetNetworksPaginator):
            pass

        func(gen_describe_subnets_paginator)


def test_describe_client_vpn_target_networks_return_pass(
    gen_describe_client_vpn_target_networks_paginator,
):
    @beartype
    def func() -> DescribeClientVpnTargetNetworksPaginator:
        return gen_describe_client_vpn_target_networks_paginator

    func()


def test_describe_client_vpn_target_networks_return_fail(
    gen_describe_subnets_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeClientVpnTargetNetworksPaginator:
            return gen_describe_subnets_paginator

        func()


# ============================
# DescribeEgressOnlyInternetGatewaysPaginator
# ============================


def test_describe_egress_only_internet_gateways_arg_pass(
    gen_describe_egress_only_internet_gateways_paginator,
):
    @beartype
    def func(param: DescribeEgressOnlyInternetGatewaysPaginator):
        pass

    func(gen_describe_egress_only_internet_gateways_paginator)


def test_describe_egress_only_internet_gateways_arg_fail(
    gen_describe_traffic_mirror_targets_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeEgressOnlyInternetGatewaysPaginator):
            pass

        func(gen_describe_traffic_mirror_targets_paginator)


def test_describe_egress_only_internet_gateways_return_pass(
    gen_describe_egress_only_internet_gateways_paginator,
):
    @beartype
    def func() -> DescribeEgressOnlyInternetGatewaysPaginator:
        return gen_describe_egress_only_internet_gateways_paginator

    func()


def test_describe_egress_only_internet_gateways_return_fail(
    gen_describe_traffic_mirror_targets_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeEgressOnlyInternetGatewaysPaginator:
            return gen_describe_traffic_mirror_targets_paginator

        func()


# ============================
# DescribeFleetsPaginator
# ============================


def test_describe_fleets_arg_pass(gen_describe_fleets_paginator):
    @beartype
    def func(param: DescribeFleetsPaginator):
        pass

    func(gen_describe_fleets_paginator)


def test_describe_fleets_arg_fail(gen_describe_security_groups_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeFleetsPaginator):
            pass

        func(gen_describe_security_groups_paginator)


def test_describe_fleets_return_pass(gen_describe_fleets_paginator):
    @beartype
    def func() -> DescribeFleetsPaginator:
        return gen_describe_fleets_paginator

    func()


def test_describe_fleets_return_fail(gen_describe_security_groups_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeFleetsPaginator:
            return gen_describe_security_groups_paginator

        func()


# ============================
# DescribeFlowLogsPaginator
# ============================


def test_describe_flow_logs_arg_pass(gen_describe_flow_logs_paginator):
    @beartype
    def func(param: DescribeFlowLogsPaginator):
        pass

    func(gen_describe_flow_logs_paginator)


def test_describe_flow_logs_arg_fail(gen_describe_coip_pools_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeFlowLogsPaginator):
            pass

        func(gen_describe_coip_pools_paginator)


def test_describe_flow_logs_return_pass(gen_describe_flow_logs_paginator):
    @beartype
    def func() -> DescribeFlowLogsPaginator:
        return gen_describe_flow_logs_paginator

    func()


def test_describe_flow_logs_return_fail(gen_describe_coip_pools_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeFlowLogsPaginator:
            return gen_describe_coip_pools_paginator

        func()


# ============================
# DescribeFpgaImagesPaginator
# ============================


def test_describe_fpga_images_arg_pass(gen_describe_fpga_images_paginator):
    @beartype
    def func(param: DescribeFpgaImagesPaginator):
        pass

    func(gen_describe_fpga_images_paginator)


def test_describe_fpga_images_arg_fail(gen_describe_moving_addresses_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeFpgaImagesPaginator):
            pass

        func(gen_describe_moving_addresses_paginator)


def test_describe_fpga_images_return_pass(gen_describe_fpga_images_paginator):
    @beartype
    def func() -> DescribeFpgaImagesPaginator:
        return gen_describe_fpga_images_paginator

    func()


def test_describe_fpga_images_return_fail(gen_describe_moving_addresses_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeFpgaImagesPaginator:
            return gen_describe_moving_addresses_paginator

        func()


# ============================
# DescribeHostReservationOfferingsPaginator
# ============================


def test_describe_host_reservation_offerings_arg_pass(
    gen_describe_host_reservation_offerings_paginator,
):
    @beartype
    def func(param: DescribeHostReservationOfferingsPaginator):
        pass

    func(gen_describe_host_reservation_offerings_paginator)


def test_describe_host_reservation_offerings_arg_fail(
    gen_describe_client_vpn_target_networks_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeHostReservationOfferingsPaginator):
            pass

        func(gen_describe_client_vpn_target_networks_paginator)


def test_describe_host_reservation_offerings_return_pass(
    gen_describe_host_reservation_offerings_paginator,
):
    @beartype
    def func() -> DescribeHostReservationOfferingsPaginator:
        return gen_describe_host_reservation_offerings_paginator

    func()


def test_describe_host_reservation_offerings_return_fail(
    gen_describe_client_vpn_target_networks_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeHostReservationOfferingsPaginator:
            return gen_describe_client_vpn_target_networks_paginator

        func()


# ============================
# DescribeHostReservationsPaginator
# ============================


def test_describe_host_reservations_arg_pass(gen_describe_host_reservations_paginator):
    @beartype
    def func(param: DescribeHostReservationsPaginator):
        pass

    func(gen_describe_host_reservations_paginator)


def test_describe_host_reservations_arg_fail(gen_describe_volume_status_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeHostReservationsPaginator):
            pass

        func(gen_describe_volume_status_paginator)


def test_describe_host_reservations_return_pass(
    gen_describe_host_reservations_paginator,
):
    @beartype
    def func() -> DescribeHostReservationsPaginator:
        return gen_describe_host_reservations_paginator

    func()


def test_describe_host_reservations_return_fail(gen_describe_volume_status_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeHostReservationsPaginator:
            return gen_describe_volume_status_paginator

        func()


# ============================
# DescribeHostsPaginator
# ============================


def test_describe_hosts_arg_pass(gen_describe_hosts_paginator):
    @beartype
    def func(param: DescribeHostsPaginator):
        pass

    func(gen_describe_hosts_paginator)


def test_describe_hosts_arg_fail(gen_describe_store_image_tasks_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeHostsPaginator):
            pass

        func(gen_describe_store_image_tasks_paginator)


def test_describe_hosts_return_pass(gen_describe_hosts_paginator):
    @beartype
    def func() -> DescribeHostsPaginator:
        return gen_describe_hosts_paginator

    func()


def test_describe_hosts_return_fail(gen_describe_store_image_tasks_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeHostsPaginator:
            return gen_describe_store_image_tasks_paginator

        func()


# ============================
# DescribeImportImageTasksPaginator
# ============================


def test_describe_import_image_tasks_arg_pass(
    gen_describe_import_image_tasks_paginator,
):
    @beartype
    def func(param: DescribeImportImageTasksPaginator):
        pass

    func(gen_describe_import_image_tasks_paginator)


def test_describe_import_image_tasks_arg_fail(gen_describe_tags_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeImportImageTasksPaginator):
            pass

        func(gen_describe_tags_paginator)


def test_describe_import_image_tasks_return_pass(
    gen_describe_import_image_tasks_paginator,
):
    @beartype
    def func() -> DescribeImportImageTasksPaginator:
        return gen_describe_import_image_tasks_paginator

    func()


def test_describe_import_image_tasks_return_fail(gen_describe_tags_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeImportImageTasksPaginator:
            return gen_describe_tags_paginator

        func()


# ============================
# DescribeImportSnapshotTasksPaginator
# ============================


def test_describe_import_snapshot_tasks_arg_pass(
    gen_describe_import_snapshot_tasks_paginator,
):
    @beartype
    def func(param: DescribeImportSnapshotTasksPaginator):
        pass

    func(gen_describe_import_snapshot_tasks_paginator)


def test_describe_import_snapshot_tasks_arg_fail(
    gen_describe_addresses_attribute_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeImportSnapshotTasksPaginator):
            pass

        func(gen_describe_addresses_attribute_paginator)


def test_describe_import_snapshot_tasks_return_pass(
    gen_describe_import_snapshot_tasks_paginator,
):
    @beartype
    def func() -> DescribeImportSnapshotTasksPaginator:
        return gen_describe_import_snapshot_tasks_paginator

    func()


def test_describe_import_snapshot_tasks_return_fail(
    gen_describe_addresses_attribute_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeImportSnapshotTasksPaginator:
            return gen_describe_addresses_attribute_paginator

        func()


# ============================
# DescribeInstanceCreditSpecificationsPaginator
# ============================


def test_describe_instance_credit_specifications_arg_pass(
    gen_describe_instance_credit_specifications_paginator,
):
    @beartype
    def func(param: DescribeInstanceCreditSpecificationsPaginator):
        pass

    func(gen_describe_instance_credit_specifications_paginator)


def test_describe_instance_credit_specifications_arg_fail(
    gen_describe_network_interfaces_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeInstanceCreditSpecificationsPaginator):
            pass

        func(gen_describe_network_interfaces_paginator)


def test_describe_instance_credit_specifications_return_pass(
    gen_describe_instance_credit_specifications_paginator,
):
    @beartype
    def func() -> DescribeInstanceCreditSpecificationsPaginator:
        return gen_describe_instance_credit_specifications_paginator

    func()


def test_describe_instance_credit_specifications_return_fail(
    gen_describe_network_interfaces_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeInstanceCreditSpecificationsPaginator:
            return gen_describe_network_interfaces_paginator

        func()


# ============================
# DescribeLaunchTemplateVersionsPaginator
# ============================


def test_describe_launch_template_versions_arg_pass(
    gen_describe_launch_template_versions_paginator,
):
    @beartype
    def func(param: DescribeLaunchTemplateVersionsPaginator):
        pass

    func(gen_describe_launch_template_versions_paginator)


def test_describe_launch_template_versions_arg_fail(
    gen_describe_spot_instance_requests_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeLaunchTemplateVersionsPaginator):
            pass

        func(gen_describe_spot_instance_requests_paginator)


def test_describe_launch_template_versions_return_pass(
    gen_describe_launch_template_versions_paginator,
):
    @beartype
    def func() -> DescribeLaunchTemplateVersionsPaginator:
        return gen_describe_launch_template_versions_paginator

    func()


def test_describe_launch_template_versions_return_fail(
    gen_describe_spot_instance_requests_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLaunchTemplateVersionsPaginator:
            return gen_describe_spot_instance_requests_paginator

        func()


# ============================
# DescribeLaunchTemplatesPaginator
# ============================


def test_describe_launch_templates_arg_pass(gen_describe_launch_templates_paginator):
    @beartype
    def func(param: DescribeLaunchTemplatesPaginator):
        pass

    func(gen_describe_launch_templates_paginator)


def test_describe_launch_templates_arg_fail(gen_describe_coip_pools_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeLaunchTemplatesPaginator):
            pass

        func(gen_describe_coip_pools_paginator)


def test_describe_launch_templates_return_pass(gen_describe_launch_templates_paginator):
    @beartype
    def func() -> DescribeLaunchTemplatesPaginator:
        return gen_describe_launch_templates_paginator

    func()


def test_describe_launch_templates_return_fail(gen_describe_coip_pools_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLaunchTemplatesPaginator:
            return gen_describe_coip_pools_paginator

        func()


# ============================
# DescribeMovingAddressesPaginator
# ============================


def test_describe_moving_addresses_arg_pass(gen_describe_moving_addresses_paginator):
    @beartype
    def func(param: DescribeMovingAddressesPaginator):
        pass

    func(gen_describe_moving_addresses_paginator)


def test_describe_moving_addresses_arg_fail(gen_describe_fpga_images_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeMovingAddressesPaginator):
            pass

        func(gen_describe_fpga_images_paginator)


def test_describe_moving_addresses_return_pass(gen_describe_moving_addresses_paginator):
    @beartype
    def func() -> DescribeMovingAddressesPaginator:
        return gen_describe_moving_addresses_paginator

    func()


def test_describe_moving_addresses_return_fail(gen_describe_fpga_images_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeMovingAddressesPaginator:
            return gen_describe_fpga_images_paginator

        func()


# ============================
# DescribeNetworkInterfacePermissionsPaginator
# ============================


def test_describe_network_interface_permissions_arg_pass(
    gen_describe_network_interface_permissions_paginator,
):
    @beartype
    def func(param: DescribeNetworkInterfacePermissionsPaginator):
        pass

    func(gen_describe_network_interface_permissions_paginator)


def test_describe_network_interface_permissions_arg_fail(
    gen_describe_network_insights_paths_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeNetworkInterfacePermissionsPaginator):
            pass

        func(gen_describe_network_insights_paths_paginator)


def test_describe_network_interface_permissions_return_pass(
    gen_describe_network_interface_permissions_paginator,
):
    @beartype
    def func() -> DescribeNetworkInterfacePermissionsPaginator:
        return gen_describe_network_interface_permissions_paginator

    func()


def test_describe_network_interface_permissions_return_fail(
    gen_describe_network_insights_paths_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeNetworkInterfacePermissionsPaginator:
            return gen_describe_network_insights_paths_paginator

        func()


# ============================
# DescribePrefixListsPaginator
# ============================


def test_describe_prefix_lists_arg_pass(gen_describe_prefix_lists_paginator):
    @beartype
    def func(param: DescribePrefixListsPaginator):
        pass

    func(gen_describe_prefix_lists_paginator)


def test_describe_prefix_lists_arg_fail(gen_describe_volumes_modifications_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribePrefixListsPaginator):
            pass

        func(gen_describe_volumes_modifications_paginator)


def test_describe_prefix_lists_return_pass(gen_describe_prefix_lists_paginator):
    @beartype
    def func() -> DescribePrefixListsPaginator:
        return gen_describe_prefix_lists_paginator

    func()


def test_describe_prefix_lists_return_fail(
    gen_describe_volumes_modifications_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribePrefixListsPaginator:
            return gen_describe_volumes_modifications_paginator

        func()


# ============================
# DescribePrincipalIdFormatPaginator
# ============================


def test_describe_principal_id_format_arg_pass(
    gen_describe_principal_id_format_paginator,
):
    @beartype
    def func(param: DescribePrincipalIdFormatPaginator):
        pass

    func(gen_describe_principal_id_format_paginator)


def test_describe_principal_id_format_arg_fail(
    gen_get_associated_ipv6_pool_cidrs_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribePrincipalIdFormatPaginator):
            pass

        func(gen_get_associated_ipv6_pool_cidrs_paginator)


def test_describe_principal_id_format_return_pass(
    gen_describe_principal_id_format_paginator,
):
    @beartype
    def func() -> DescribePrincipalIdFormatPaginator:
        return gen_describe_principal_id_format_paginator

    func()


def test_describe_principal_id_format_return_fail(
    gen_get_associated_ipv6_pool_cidrs_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribePrincipalIdFormatPaginator:
            return gen_get_associated_ipv6_pool_cidrs_paginator

        func()


# ============================
# DescribePublicIpv4PoolsPaginator
# ============================


def test_describe_public_ipv4_pools_arg_pass(gen_describe_public_ipv4_pools_paginator):
    @beartype
    def func(param: DescribePublicIpv4PoolsPaginator):
        pass

    func(gen_describe_public_ipv4_pools_paginator)


def test_describe_public_ipv4_pools_arg_fail(
    gen_describe_local_gateway_virtual_interfaces_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribePublicIpv4PoolsPaginator):
            pass

        func(gen_describe_local_gateway_virtual_interfaces_paginator)


def test_describe_public_ipv4_pools_return_pass(
    gen_describe_public_ipv4_pools_paginator,
):
    @beartype
    def func() -> DescribePublicIpv4PoolsPaginator:
        return gen_describe_public_ipv4_pools_paginator

    func()


def test_describe_public_ipv4_pools_return_fail(
    gen_describe_local_gateway_virtual_interfaces_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribePublicIpv4PoolsPaginator:
            return gen_describe_local_gateway_virtual_interfaces_paginator

        func()


# ============================
# DescribeScheduledInstanceAvailabilityPaginator
# ============================


def test_describe_scheduled_instance_availability_arg_pass(
    gen_describe_scheduled_instance_availability_paginator,
):
    @beartype
    def func(param: DescribeScheduledInstanceAvailabilityPaginator):
        pass

    func(gen_describe_scheduled_instance_availability_paginator)


def test_describe_scheduled_instance_availability_arg_fail(
    gen_get_vpn_connection_device_types_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeScheduledInstanceAvailabilityPaginator):
            pass

        func(gen_get_vpn_connection_device_types_paginator)


def test_describe_scheduled_instance_availability_return_pass(
    gen_describe_scheduled_instance_availability_paginator,
):
    @beartype
    def func() -> DescribeScheduledInstanceAvailabilityPaginator:
        return gen_describe_scheduled_instance_availability_paginator

    func()


def test_describe_scheduled_instance_availability_return_fail(
    gen_get_vpn_connection_device_types_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeScheduledInstanceAvailabilityPaginator:
            return gen_get_vpn_connection_device_types_paginator

        func()


# ============================
# DescribeScheduledInstancesPaginator
# ============================


def test_describe_scheduled_instances_arg_pass(
    gen_describe_scheduled_instances_paginator,
):
    @beartype
    def func(param: DescribeScheduledInstancesPaginator):
        pass

    func(gen_describe_scheduled_instances_paginator)


def test_describe_scheduled_instances_arg_fail(gen_describe_instance_status_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeScheduledInstancesPaginator):
            pass

        func(gen_describe_instance_status_paginator)


def test_describe_scheduled_instances_return_pass(
    gen_describe_scheduled_instances_paginator,
):
    @beartype
    def func() -> DescribeScheduledInstancesPaginator:
        return gen_describe_scheduled_instances_paginator

    func()


def test_describe_scheduled_instances_return_fail(
    gen_describe_instance_status_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeScheduledInstancesPaginator:
            return gen_describe_instance_status_paginator

        func()


# ============================
# DescribeStaleSecurityGroupsPaginator
# ============================


def test_describe_stale_security_groups_arg_pass(
    gen_describe_stale_security_groups_paginator,
):
    @beartype
    def func(param: DescribeStaleSecurityGroupsPaginator):
        pass

    func(gen_describe_stale_security_groups_paginator)


def test_describe_stale_security_groups_arg_fail(
    gen_get_associated_ipv6_pool_cidrs_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeStaleSecurityGroupsPaginator):
            pass

        func(gen_get_associated_ipv6_pool_cidrs_paginator)


def test_describe_stale_security_groups_return_pass(
    gen_describe_stale_security_groups_paginator,
):
    @beartype
    def func() -> DescribeStaleSecurityGroupsPaginator:
        return gen_describe_stale_security_groups_paginator

    func()


def test_describe_stale_security_groups_return_fail(
    gen_get_associated_ipv6_pool_cidrs_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeStaleSecurityGroupsPaginator:
            return gen_get_associated_ipv6_pool_cidrs_paginator

        func()


# ============================
# DescribeTransitGatewayAttachmentsPaginator
# ============================


def test_describe_transit_gateway_attachments_arg_pass(
    gen_describe_transit_gateway_attachments_paginator,
):
    @beartype
    def func(param: DescribeTransitGatewayAttachmentsPaginator):
        pass

    func(gen_describe_transit_gateway_attachments_paginator)


def test_describe_transit_gateway_attachments_arg_fail(
    gen_describe_local_gateway_route_tables_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewayAttachmentsPaginator):
            pass

        func(gen_describe_local_gateway_route_tables_paginator)


def test_describe_transit_gateway_attachments_return_pass(
    gen_describe_transit_gateway_attachments_paginator,
):
    @beartype
    def func() -> DescribeTransitGatewayAttachmentsPaginator:
        return gen_describe_transit_gateway_attachments_paginator

    func()


def test_describe_transit_gateway_attachments_return_fail(
    gen_describe_local_gateway_route_tables_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewayAttachmentsPaginator:
            return gen_describe_local_gateway_route_tables_paginator

        func()


# ============================
# DescribeTransitGatewayRouteTablesPaginator
# ============================


def test_describe_transit_gateway_route_tables_arg_pass(
    gen_describe_transit_gateway_route_tables_paginator,
):
    @beartype
    def func(param: DescribeTransitGatewayRouteTablesPaginator):
        pass

    func(gen_describe_transit_gateway_route_tables_paginator)


def test_describe_transit_gateway_route_tables_arg_fail(
    gen_describe_launch_templates_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewayRouteTablesPaginator):
            pass

        func(gen_describe_launch_templates_paginator)


def test_describe_transit_gateway_route_tables_return_pass(
    gen_describe_transit_gateway_route_tables_paginator,
):
    @beartype
    def func() -> DescribeTransitGatewayRouteTablesPaginator:
        return gen_describe_transit_gateway_route_tables_paginator

    func()


def test_describe_transit_gateway_route_tables_return_fail(
    gen_describe_launch_templates_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewayRouteTablesPaginator:
            return gen_describe_launch_templates_paginator

        func()


# ============================
# DescribeTransitGatewayVpcAttachmentsPaginator
# ============================


def test_describe_transit_gateway_vpc_attachments_arg_pass(
    gen_describe_transit_gateway_vpc_attachments_paginator,
):
    @beartype
    def func(param: DescribeTransitGatewayVpcAttachmentsPaginator):
        pass

    func(gen_describe_transit_gateway_vpc_attachments_paginator)


def test_describe_transit_gateway_vpc_attachments_arg_fail(
    gen_get_instance_types_from_instance_requirements_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewayVpcAttachmentsPaginator):
            pass

        func(gen_get_instance_types_from_instance_requirements_paginator)


def test_describe_transit_gateway_vpc_attachments_return_pass(
    gen_describe_transit_gateway_vpc_attachments_paginator,
):
    @beartype
    def func() -> DescribeTransitGatewayVpcAttachmentsPaginator:
        return gen_describe_transit_gateway_vpc_attachments_paginator

    func()


def test_describe_transit_gateway_vpc_attachments_return_fail(
    gen_get_instance_types_from_instance_requirements_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewayVpcAttachmentsPaginator:
            return gen_get_instance_types_from_instance_requirements_paginator

        func()


# ============================
# DescribeTransitGatewaysPaginator
# ============================


def test_describe_transit_gateways_arg_pass(gen_describe_transit_gateways_paginator):
    @beartype
    def func(param: DescribeTransitGatewaysPaginator):
        pass

    func(gen_describe_transit_gateways_paginator)


def test_describe_transit_gateways_arg_fail(gen_describe_route_tables_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewaysPaginator):
            pass

        func(gen_describe_route_tables_paginator)


def test_describe_transit_gateways_return_pass(gen_describe_transit_gateways_paginator):
    @beartype
    def func() -> DescribeTransitGatewaysPaginator:
        return gen_describe_transit_gateways_paginator

    func()


def test_describe_transit_gateways_return_fail(gen_describe_route_tables_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewaysPaginator:
            return gen_describe_route_tables_paginator

        func()


# ============================
# DescribeVolumesModificationsPaginator
# ============================


def test_describe_volumes_modifications_arg_pass(
    gen_describe_volumes_modifications_paginator,
):
    @beartype
    def func(param: DescribeVolumesModificationsPaginator):
        pass

    func(gen_describe_volumes_modifications_paginator)


def test_describe_volumes_modifications_arg_fail(gen_describe_instance_types_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVolumesModificationsPaginator):
            pass

        func(gen_describe_instance_types_paginator)


def test_describe_volumes_modifications_return_pass(
    gen_describe_volumes_modifications_paginator,
):
    @beartype
    def func() -> DescribeVolumesModificationsPaginator:
        return gen_describe_volumes_modifications_paginator

    func()


def test_describe_volumes_modifications_return_fail(
    gen_describe_instance_types_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVolumesModificationsPaginator:
            return gen_describe_instance_types_paginator

        func()


# ============================
# DescribeVpcClassicLinkDnsSupportPaginator
# ============================


def test_describe_vpc_classic_link_dns_support_arg_pass(
    gen_describe_vpc_classic_link_dns_support_paginator,
):
    @beartype
    def func(param: DescribeVpcClassicLinkDnsSupportPaginator):
        pass

    func(gen_describe_vpc_classic_link_dns_support_paginator)


def test_describe_vpc_classic_link_dns_support_arg_fail(
    gen_get_transit_gateway_multicast_domain_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcClassicLinkDnsSupportPaginator):
            pass

        func(gen_get_transit_gateway_multicast_domain_associations_paginator)


def test_describe_vpc_classic_link_dns_support_return_pass(
    gen_describe_vpc_classic_link_dns_support_paginator,
):
    @beartype
    def func() -> DescribeVpcClassicLinkDnsSupportPaginator:
        return gen_describe_vpc_classic_link_dns_support_paginator

    func()


def test_describe_vpc_classic_link_dns_support_return_fail(
    gen_get_transit_gateway_multicast_domain_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcClassicLinkDnsSupportPaginator:
            return gen_get_transit_gateway_multicast_domain_associations_paginator

        func()


# ============================
# DescribeVpcEndpointConnectionNotificationsPaginator
# ============================


def test_describe_vpc_endpoint_connection_notifications_arg_pass(
    gen_describe_vpc_endpoint_connection_notifications_paginator,
):
    @beartype
    def func(param: DescribeVpcEndpointConnectionNotificationsPaginator):
        pass

    func(gen_describe_vpc_endpoint_connection_notifications_paginator)


def test_describe_vpc_endpoint_connection_notifications_arg_fail(
    gen_describe_launch_templates_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcEndpointConnectionNotificationsPaginator):
            pass

        func(gen_describe_launch_templates_paginator)


def test_describe_vpc_endpoint_connection_notifications_return_pass(
    gen_describe_vpc_endpoint_connection_notifications_paginator,
):
    @beartype
    def func() -> DescribeVpcEndpointConnectionNotificationsPaginator:
        return gen_describe_vpc_endpoint_connection_notifications_paginator

    func()


def test_describe_vpc_endpoint_connection_notifications_return_fail(
    gen_describe_launch_templates_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcEndpointConnectionNotificationsPaginator:
            return gen_describe_launch_templates_paginator

        func()


# ============================
# DescribeVpcEndpointServiceConfigurationsPaginator
# ============================


def test_describe_vpc_endpoint_service_configurations_arg_pass(
    gen_describe_vpc_endpoint_service_configurations_paginator,
):
    @beartype
    def func(param: DescribeVpcEndpointServiceConfigurationsPaginator):
        pass

    func(gen_describe_vpc_endpoint_service_configurations_paginator)


def test_describe_vpc_endpoint_service_configurations_arg_fail(
    gen_describe_vpcs_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcEndpointServiceConfigurationsPaginator):
            pass

        func(gen_describe_vpcs_paginator)


def test_describe_vpc_endpoint_service_configurations_return_pass(
    gen_describe_vpc_endpoint_service_configurations_paginator,
):
    @beartype
    def func() -> DescribeVpcEndpointServiceConfigurationsPaginator:
        return gen_describe_vpc_endpoint_service_configurations_paginator

    func()


def test_describe_vpc_endpoint_service_configurations_return_fail(
    gen_describe_vpcs_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcEndpointServiceConfigurationsPaginator:
            return gen_describe_vpcs_paginator

        func()


# ============================
# DescribeVpcEndpointServicePermissionsPaginator
# ============================


def test_describe_vpc_endpoint_service_permissions_arg_pass(
    gen_describe_vpc_endpoint_service_permissions_paginator,
):
    @beartype
    def func(param: DescribeVpcEndpointServicePermissionsPaginator):
        pass

    func(gen_describe_vpc_endpoint_service_permissions_paginator)


def test_describe_vpc_endpoint_service_permissions_arg_fail(
    gen_describe_vpc_peering_connections_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcEndpointServicePermissionsPaginator):
            pass

        func(gen_describe_vpc_peering_connections_paginator)


def test_describe_vpc_endpoint_service_permissions_return_pass(
    gen_describe_vpc_endpoint_service_permissions_paginator,
):
    @beartype
    def func() -> DescribeVpcEndpointServicePermissionsPaginator:
        return gen_describe_vpc_endpoint_service_permissions_paginator

    func()


def test_describe_vpc_endpoint_service_permissions_return_fail(
    gen_describe_vpc_peering_connections_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcEndpointServicePermissionsPaginator:
            return gen_describe_vpc_peering_connections_paginator

        func()


# ============================
# DescribeVpcPeeringConnectionsPaginator
# ============================


def test_describe_vpc_peering_connections_arg_pass(
    gen_describe_vpc_peering_connections_paginator,
):
    @beartype
    def func(param: DescribeVpcPeeringConnectionsPaginator):
        pass

    func(gen_describe_vpc_peering_connections_paginator)


def test_describe_vpc_peering_connections_arg_fail(
    gen_describe_network_insights_paths_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcPeeringConnectionsPaginator):
            pass

        func(gen_describe_network_insights_paths_paginator)


def test_describe_vpc_peering_connections_return_pass(
    gen_describe_vpc_peering_connections_paginator,
):
    @beartype
    def func() -> DescribeVpcPeeringConnectionsPaginator:
        return gen_describe_vpc_peering_connections_paginator

    func()


def test_describe_vpc_peering_connections_return_fail(
    gen_describe_network_insights_paths_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcPeeringConnectionsPaginator:
            return gen_describe_network_insights_paths_paginator

        func()


# ============================
# GetTransitGatewayAttachmentPropagationsPaginator
# ============================


def test_get_transit_gateway_attachment_propagations_arg_pass(
    gen_get_transit_gateway_attachment_propagations_paginator,
):
    @beartype
    def func(param: GetTransitGatewayAttachmentPropagationsPaginator):
        pass

    func(gen_get_transit_gateway_attachment_propagations_paginator)


def test_get_transit_gateway_attachment_propagations_arg_fail(
    gen_get_managed_prefix_list_entries_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetTransitGatewayAttachmentPropagationsPaginator):
            pass

        func(gen_get_managed_prefix_list_entries_paginator)


def test_get_transit_gateway_attachment_propagations_return_pass(
    gen_get_transit_gateway_attachment_propagations_paginator,
):
    @beartype
    def func() -> GetTransitGatewayAttachmentPropagationsPaginator:
        return gen_get_transit_gateway_attachment_propagations_paginator

    func()


def test_get_transit_gateway_attachment_propagations_return_fail(
    gen_get_managed_prefix_list_entries_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetTransitGatewayAttachmentPropagationsPaginator:
            return gen_get_managed_prefix_list_entries_paginator

        func()


# ============================
# GetTransitGatewayRouteTableAssociationsPaginator
# ============================


def test_get_transit_gateway_route_table_associations_arg_pass(
    gen_get_transit_gateway_route_table_associations_paginator,
):
    @beartype
    def func(param: GetTransitGatewayRouteTableAssociationsPaginator):
        pass

    func(gen_get_transit_gateway_route_table_associations_paginator)


def test_get_transit_gateway_route_table_associations_arg_fail(
    gen_describe_classic_link_instances_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetTransitGatewayRouteTableAssociationsPaginator):
            pass

        func(gen_describe_classic_link_instances_paginator)


def test_get_transit_gateway_route_table_associations_return_pass(
    gen_get_transit_gateway_route_table_associations_paginator,
):
    @beartype
    def func() -> GetTransitGatewayRouteTableAssociationsPaginator:
        return gen_get_transit_gateway_route_table_associations_paginator

    func()


def test_get_transit_gateway_route_table_associations_return_fail(
    gen_describe_classic_link_instances_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetTransitGatewayRouteTableAssociationsPaginator:
            return gen_describe_classic_link_instances_paginator

        func()


# ============================
# GetTransitGatewayRouteTablePropagationsPaginator
# ============================


def test_get_transit_gateway_route_table_propagations_arg_pass(
    gen_get_transit_gateway_route_table_propagations_paginator,
):
    @beartype
    def func(param: GetTransitGatewayRouteTablePropagationsPaginator):
        pass

    func(gen_get_transit_gateway_route_table_propagations_paginator)


def test_get_transit_gateway_route_table_propagations_arg_fail(
    gen_describe_ipv6_pools_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetTransitGatewayRouteTablePropagationsPaginator):
            pass

        func(gen_describe_ipv6_pools_paginator)


def test_get_transit_gateway_route_table_propagations_return_pass(
    gen_get_transit_gateway_route_table_propagations_paginator,
):
    @beartype
    def func() -> GetTransitGatewayRouteTablePropagationsPaginator:
        return gen_get_transit_gateway_route_table_propagations_paginator

    func()


def test_get_transit_gateway_route_table_propagations_return_fail(
    gen_describe_ipv6_pools_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetTransitGatewayRouteTablePropagationsPaginator:
            return gen_describe_ipv6_pools_paginator

        func()


# ============================
# DescribeInternetGatewaysPaginator
# ============================


def test_describe_internet_gateways_arg_pass(gen_describe_internet_gateways_paginator):
    @beartype
    def func(param: DescribeInternetGatewaysPaginator):
        pass

    func(gen_describe_internet_gateways_paginator)


def test_describe_internet_gateways_arg_fail(
    gen_describe_network_insights_analyses_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeInternetGatewaysPaginator):
            pass

        func(gen_describe_network_insights_analyses_paginator)


def test_describe_internet_gateways_return_pass(
    gen_describe_internet_gateways_paginator,
):
    @beartype
    def func() -> DescribeInternetGatewaysPaginator:
        return gen_describe_internet_gateways_paginator

    func()


def test_describe_internet_gateways_return_fail(
    gen_describe_network_insights_analyses_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeInternetGatewaysPaginator:
            return gen_describe_network_insights_analyses_paginator

        func()


# ============================
# DescribeNetworkAclsPaginator
# ============================


def test_describe_network_acls_arg_pass(gen_describe_network_acls_paginator):
    @beartype
    def func(param: DescribeNetworkAclsPaginator):
        pass

    func(gen_describe_network_acls_paginator)


def test_describe_network_acls_arg_fail(gen_describe_instance_type_offerings_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeNetworkAclsPaginator):
            pass

        func(gen_describe_instance_type_offerings_paginator)


def test_describe_network_acls_return_pass(gen_describe_network_acls_paginator):
    @beartype
    def func() -> DescribeNetworkAclsPaginator:
        return gen_describe_network_acls_paginator

    func()


def test_describe_network_acls_return_fail(
    gen_describe_instance_type_offerings_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeNetworkAclsPaginator:
            return gen_describe_instance_type_offerings_paginator

        func()


# ============================
# DescribeVpcsPaginator
# ============================


def test_describe_vpcs_arg_pass(gen_describe_vpcs_paginator):
    @beartype
    def func(param: DescribeVpcsPaginator):
        pass

    func(gen_describe_vpcs_paginator)


def test_describe_vpcs_arg_fail(gen_describe_fleets_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeVpcsPaginator):
            pass

        func(gen_describe_fleets_paginator)


def test_describe_vpcs_return_pass(gen_describe_vpcs_paginator):
    @beartype
    def func() -> DescribeVpcsPaginator:
        return gen_describe_vpcs_paginator

    func()


def test_describe_vpcs_return_fail(gen_describe_fleets_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeVpcsPaginator:
            return gen_describe_fleets_paginator

        func()


# ============================
# DescribeSpotInstanceRequestsPaginator
# ============================


def test_describe_spot_instance_requests_arg_pass(
    gen_describe_spot_instance_requests_paginator,
):
    @beartype
    def func(param: DescribeSpotInstanceRequestsPaginator):
        pass

    func(gen_describe_spot_instance_requests_paginator)


def test_describe_spot_instance_requests_arg_fail(
    gen_describe_vpc_endpoint_service_permissions_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSpotInstanceRequestsPaginator):
            pass

        func(gen_describe_vpc_endpoint_service_permissions_paginator)


def test_describe_spot_instance_requests_return_pass(
    gen_describe_spot_instance_requests_paginator,
):
    @beartype
    def func() -> DescribeSpotInstanceRequestsPaginator:
        return gen_describe_spot_instance_requests_paginator

    func()


def test_describe_spot_instance_requests_return_fail(
    gen_describe_vpc_endpoint_service_permissions_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSpotInstanceRequestsPaginator:
            return gen_describe_vpc_endpoint_service_permissions_paginator

        func()


# ============================
# DescribeDhcpOptionsPaginator
# ============================


def test_describe_dhcp_options_arg_pass(gen_describe_dhcp_options_paginator):
    @beartype
    def func(param: DescribeDhcpOptionsPaginator):
        pass

    func(gen_describe_dhcp_options_paginator)


def test_describe_dhcp_options_arg_fail(
    gen_get_transit_gateway_prefix_list_references_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeDhcpOptionsPaginator):
            pass

        func(gen_get_transit_gateway_prefix_list_references_paginator)


def test_describe_dhcp_options_return_pass(gen_describe_dhcp_options_paginator):
    @beartype
    def func() -> DescribeDhcpOptionsPaginator:
        return gen_describe_dhcp_options_paginator

    func()


def test_describe_dhcp_options_return_fail(
    gen_get_transit_gateway_prefix_list_references_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeDhcpOptionsPaginator:
            return gen_get_transit_gateway_prefix_list_references_paginator

        func()


# ============================
# DescribeSubnetsPaginator
# ============================


def test_describe_subnets_arg_pass(gen_describe_subnets_paginator):
    @beartype
    def func(param: DescribeSubnetsPaginator):
        pass

    func(gen_describe_subnets_paginator)


def test_describe_subnets_arg_fail(
    gen_describe_egress_only_internet_gateways_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSubnetsPaginator):
            pass

        func(gen_describe_egress_only_internet_gateways_paginator)


def test_describe_subnets_return_pass(gen_describe_subnets_paginator):
    @beartype
    def func() -> DescribeSubnetsPaginator:
        return gen_describe_subnets_paginator

    func()


def test_describe_subnets_return_fail(
    gen_describe_egress_only_internet_gateways_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSubnetsPaginator:
            return gen_describe_egress_only_internet_gateways_paginator

        func()


# ============================
# DescribeTrafficMirrorFiltersPaginator
# ============================


def test_describe_traffic_mirror_filters_arg_pass(
    gen_describe_traffic_mirror_filters_paginator,
):
    @beartype
    def func(param: DescribeTrafficMirrorFiltersPaginator):
        pass

    func(gen_describe_traffic_mirror_filters_paginator)


def test_describe_traffic_mirror_filters_arg_fail(
    gen_describe_transit_gateway_vpc_attachments_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTrafficMirrorFiltersPaginator):
            pass

        func(gen_describe_transit_gateway_vpc_attachments_paginator)


def test_describe_traffic_mirror_filters_return_pass(
    gen_describe_traffic_mirror_filters_paginator,
):
    @beartype
    def func() -> DescribeTrafficMirrorFiltersPaginator:
        return gen_describe_traffic_mirror_filters_paginator

    func()


def test_describe_traffic_mirror_filters_return_fail(
    gen_describe_transit_gateway_vpc_attachments_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTrafficMirrorFiltersPaginator:
            return gen_describe_transit_gateway_vpc_attachments_paginator

        func()


# ============================
# DescribeTrafficMirrorSessionsPaginator
# ============================


def test_describe_traffic_mirror_sessions_arg_pass(
    gen_describe_traffic_mirror_sessions_paginator,
):
    @beartype
    def func(param: DescribeTrafficMirrorSessionsPaginator):
        pass

    func(gen_describe_traffic_mirror_sessions_paginator)


def test_describe_traffic_mirror_sessions_arg_fail(
    gen_describe_client_vpn_connections_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTrafficMirrorSessionsPaginator):
            pass

        func(gen_describe_client_vpn_connections_paginator)


def test_describe_traffic_mirror_sessions_return_pass(
    gen_describe_traffic_mirror_sessions_paginator,
):
    @beartype
    def func() -> DescribeTrafficMirrorSessionsPaginator:
        return gen_describe_traffic_mirror_sessions_paginator

    func()


def test_describe_traffic_mirror_sessions_return_fail(
    gen_describe_client_vpn_connections_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTrafficMirrorSessionsPaginator:
            return gen_describe_client_vpn_connections_paginator

        func()


# ============================
# DescribeTrafficMirrorTargetsPaginator
# ============================


def test_describe_traffic_mirror_targets_arg_pass(
    gen_describe_traffic_mirror_targets_paginator,
):
    @beartype
    def func(param: DescribeTrafficMirrorTargetsPaginator):
        pass

    func(gen_describe_traffic_mirror_targets_paginator)


def test_describe_traffic_mirror_targets_arg_fail(
    gen_describe_vpc_endpoint_services_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTrafficMirrorTargetsPaginator):
            pass

        func(gen_describe_vpc_endpoint_services_paginator)


def test_describe_traffic_mirror_targets_return_pass(
    gen_describe_traffic_mirror_targets_paginator,
):
    @beartype
    def func() -> DescribeTrafficMirrorTargetsPaginator:
        return gen_describe_traffic_mirror_targets_paginator

    func()


def test_describe_traffic_mirror_targets_return_fail(
    gen_describe_vpc_endpoint_services_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTrafficMirrorTargetsPaginator:
            return gen_describe_vpc_endpoint_services_paginator

        func()


# ============================
# DescribeExportImageTasksPaginator
# ============================


def test_describe_export_image_tasks_arg_pass(
    gen_describe_export_image_tasks_paginator,
):
    @beartype
    def func(param: DescribeExportImageTasksPaginator):
        pass

    func(gen_describe_export_image_tasks_paginator)


def test_describe_export_image_tasks_arg_fail(
    gen_get_managed_prefix_list_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeExportImageTasksPaginator):
            pass

        func(gen_get_managed_prefix_list_associations_paginator)


def test_describe_export_image_tasks_return_pass(
    gen_describe_export_image_tasks_paginator,
):
    @beartype
    def func() -> DescribeExportImageTasksPaginator:
        return gen_describe_export_image_tasks_paginator

    func()


def test_describe_export_image_tasks_return_fail(
    gen_get_managed_prefix_list_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeExportImageTasksPaginator:
            return gen_get_managed_prefix_list_associations_paginator

        func()


# ============================
# DescribeFastSnapshotRestoresPaginator
# ============================


def test_describe_fast_snapshot_restores_arg_pass(
    gen_describe_fast_snapshot_restores_paginator,
):
    @beartype
    def func(param: DescribeFastSnapshotRestoresPaginator):
        pass

    func(gen_describe_fast_snapshot_restores_paginator)


def test_describe_fast_snapshot_restores_arg_fail(
    gen_describe_transit_gateway_multicast_domains_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeFastSnapshotRestoresPaginator):
            pass

        func(gen_describe_transit_gateway_multicast_domains_paginator)


def test_describe_fast_snapshot_restores_return_pass(
    gen_describe_fast_snapshot_restores_paginator,
):
    @beartype
    def func() -> DescribeFastSnapshotRestoresPaginator:
        return gen_describe_fast_snapshot_restores_paginator

    func()


def test_describe_fast_snapshot_restores_return_fail(
    gen_describe_transit_gateway_multicast_domains_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeFastSnapshotRestoresPaginator:
            return gen_describe_transit_gateway_multicast_domains_paginator

        func()


# ============================
# DescribeIpv6PoolsPaginator
# ============================


def test_describe_ipv6_pools_arg_pass(gen_describe_ipv6_pools_paginator):
    @beartype
    def func(param: DescribeIpv6PoolsPaginator):
        pass

    func(gen_describe_ipv6_pools_paginator)


def test_describe_ipv6_pools_arg_fail(gen_describe_launch_template_versions_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeIpv6PoolsPaginator):
            pass

        func(gen_describe_launch_template_versions_paginator)


def test_describe_ipv6_pools_return_pass(gen_describe_ipv6_pools_paginator):
    @beartype
    def func() -> DescribeIpv6PoolsPaginator:
        return gen_describe_ipv6_pools_paginator

    func()


def test_describe_ipv6_pools_return_fail(
    gen_describe_launch_template_versions_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeIpv6PoolsPaginator:
            return gen_describe_launch_template_versions_paginator

        func()


# ============================
# GetAssociatedIpv6PoolCidrsPaginator
# ============================


def test_get_associated_ipv6_pool_cidrs_arg_pass(
    gen_get_associated_ipv6_pool_cidrs_paginator,
):
    @beartype
    def func(param: GetAssociatedIpv6PoolCidrsPaginator):
        pass

    func(gen_get_associated_ipv6_pool_cidrs_paginator)


def test_get_associated_ipv6_pool_cidrs_arg_fail(
    gen_describe_spot_fleet_instances_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetAssociatedIpv6PoolCidrsPaginator):
            pass

        func(gen_describe_spot_fleet_instances_paginator)


def test_get_associated_ipv6_pool_cidrs_return_pass(
    gen_get_associated_ipv6_pool_cidrs_paginator,
):
    @beartype
    def func() -> GetAssociatedIpv6PoolCidrsPaginator:
        return gen_get_associated_ipv6_pool_cidrs_paginator

    func()


def test_get_associated_ipv6_pool_cidrs_return_fail(
    gen_describe_spot_fleet_instances_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetAssociatedIpv6PoolCidrsPaginator:
            return gen_describe_spot_fleet_instances_paginator

        func()


# ============================
# DescribeCoipPoolsPaginator
# ============================


def test_describe_coip_pools_arg_pass(gen_describe_coip_pools_paginator):
    @beartype
    def func(param: DescribeCoipPoolsPaginator):
        pass

    func(gen_describe_coip_pools_paginator)


def test_describe_coip_pools_arg_fail(gen_describe_instance_event_windows_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeCoipPoolsPaginator):
            pass

        func(gen_describe_instance_event_windows_paginator)


def test_describe_coip_pools_return_pass(gen_describe_coip_pools_paginator):
    @beartype
    def func() -> DescribeCoipPoolsPaginator:
        return gen_describe_coip_pools_paginator

    func()


def test_describe_coip_pools_return_fail(gen_describe_instance_event_windows_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeCoipPoolsPaginator:
            return gen_describe_instance_event_windows_paginator

        func()


# ============================
# DescribeInstanceTypeOfferingsPaginator
# ============================


def test_describe_instance_type_offerings_arg_pass(
    gen_describe_instance_type_offerings_paginator,
):
    @beartype
    def func(param: DescribeInstanceTypeOfferingsPaginator):
        pass

    func(gen_describe_instance_type_offerings_paginator)


def test_describe_instance_type_offerings_arg_fail(
    gen_describe_traffic_mirror_targets_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeInstanceTypeOfferingsPaginator):
            pass

        func(gen_describe_traffic_mirror_targets_paginator)


def test_describe_instance_type_offerings_return_pass(
    gen_describe_instance_type_offerings_paginator,
):
    @beartype
    def func() -> DescribeInstanceTypeOfferingsPaginator:
        return gen_describe_instance_type_offerings_paginator

    func()


def test_describe_instance_type_offerings_return_fail(
    gen_describe_traffic_mirror_targets_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeInstanceTypeOfferingsPaginator:
            return gen_describe_traffic_mirror_targets_paginator

        func()


# ============================
# DescribeInstanceTypesPaginator
# ============================


def test_describe_instance_types_arg_pass(gen_describe_instance_types_paginator):
    @beartype
    def func(param: DescribeInstanceTypesPaginator):
        pass

    func(gen_describe_instance_types_paginator)


def test_describe_instance_types_arg_fail(gen_describe_flow_logs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeInstanceTypesPaginator):
            pass

        func(gen_describe_flow_logs_paginator)


def test_describe_instance_types_return_pass(gen_describe_instance_types_paginator):
    @beartype
    def func() -> DescribeInstanceTypesPaginator:
        return gen_describe_instance_types_paginator

    func()


def test_describe_instance_types_return_fail(gen_describe_flow_logs_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeInstanceTypesPaginator:
            return gen_describe_flow_logs_paginator

        func()


# ============================
# DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator
# ============================


def test_describe_local_gateway_route_table_virtual_interface_group_associations_arg_pass(
    gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator,
):
    @beartype
    def func(
        param: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
    ):
        pass

    func(
        gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator
    )


def test_describe_local_gateway_route_table_virtual_interface_group_associations_arg_fail(
    gen_describe_security_groups_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(
            param: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
        ):
            pass

        func(gen_describe_security_groups_paginator)


def test_describe_local_gateway_route_table_virtual_interface_group_associations_return_pass(
    gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator,
):
    @beartype
    def func() -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator:
        return gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator

    func()


def test_describe_local_gateway_route_table_virtual_interface_group_associations_return_fail(
    gen_describe_security_groups_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator:
            return gen_describe_security_groups_paginator

        func()


# ============================
# DescribeLocalGatewayRouteTableVpcAssociationsPaginator
# ============================


def test_describe_local_gateway_route_table_vpc_associations_arg_pass(
    gen_describe_local_gateway_route_table_vpc_associations_paginator,
):
    @beartype
    def func(param: DescribeLocalGatewayRouteTableVpcAssociationsPaginator):
        pass

    func(gen_describe_local_gateway_route_table_vpc_associations_paginator)


def test_describe_local_gateway_route_table_vpc_associations_arg_fail(
    gen_get_managed_prefix_list_entries_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeLocalGatewayRouteTableVpcAssociationsPaginator):
            pass

        func(gen_get_managed_prefix_list_entries_paginator)


def test_describe_local_gateway_route_table_vpc_associations_return_pass(
    gen_describe_local_gateway_route_table_vpc_associations_paginator,
):
    @beartype
    def func() -> DescribeLocalGatewayRouteTableVpcAssociationsPaginator:
        return gen_describe_local_gateway_route_table_vpc_associations_paginator

    func()


def test_describe_local_gateway_route_table_vpc_associations_return_fail(
    gen_get_managed_prefix_list_entries_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLocalGatewayRouteTableVpcAssociationsPaginator:
            return gen_get_managed_prefix_list_entries_paginator

        func()


# ============================
# DescribeLocalGatewayRouteTablesPaginator
# ============================


def test_describe_local_gateway_route_tables_arg_pass(
    gen_describe_local_gateway_route_tables_paginator,
):
    @beartype
    def func(param: DescribeLocalGatewayRouteTablesPaginator):
        pass

    func(gen_describe_local_gateway_route_tables_paginator)


def test_describe_local_gateway_route_tables_arg_fail(
    gen_describe_managed_prefix_lists_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeLocalGatewayRouteTablesPaginator):
            pass

        func(gen_describe_managed_prefix_lists_paginator)


def test_describe_local_gateway_route_tables_return_pass(
    gen_describe_local_gateway_route_tables_paginator,
):
    @beartype
    def func() -> DescribeLocalGatewayRouteTablesPaginator:
        return gen_describe_local_gateway_route_tables_paginator

    func()


def test_describe_local_gateway_route_tables_return_fail(
    gen_describe_managed_prefix_lists_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLocalGatewayRouteTablesPaginator:
            return gen_describe_managed_prefix_lists_paginator

        func()


# ============================
# DescribeLocalGatewayVirtualInterfaceGroupsPaginator
# ============================


def test_describe_local_gateway_virtual_interface_groups_arg_pass(
    gen_describe_local_gateway_virtual_interface_groups_paginator,
):
    @beartype
    def func(param: DescribeLocalGatewayVirtualInterfaceGroupsPaginator):
        pass

    func(gen_describe_local_gateway_virtual_interface_groups_paginator)


def test_describe_local_gateway_virtual_interface_groups_arg_fail(
    gen_describe_subnets_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeLocalGatewayVirtualInterfaceGroupsPaginator):
            pass

        func(gen_describe_subnets_paginator)


def test_describe_local_gateway_virtual_interface_groups_return_pass(
    gen_describe_local_gateway_virtual_interface_groups_paginator,
):
    @beartype
    def func() -> DescribeLocalGatewayVirtualInterfaceGroupsPaginator:
        return gen_describe_local_gateway_virtual_interface_groups_paginator

    func()


def test_describe_local_gateway_virtual_interface_groups_return_fail(
    gen_describe_subnets_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLocalGatewayVirtualInterfaceGroupsPaginator:
            return gen_describe_subnets_paginator

        func()


# ============================
# DescribeLocalGatewayVirtualInterfacesPaginator
# ============================


def test_describe_local_gateway_virtual_interfaces_arg_pass(
    gen_describe_local_gateway_virtual_interfaces_paginator,
):
    @beartype
    def func(param: DescribeLocalGatewayVirtualInterfacesPaginator):
        pass

    func(gen_describe_local_gateway_virtual_interfaces_paginator)


def test_describe_local_gateway_virtual_interfaces_arg_fail(
    gen_describe_import_snapshot_tasks_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeLocalGatewayVirtualInterfacesPaginator):
            pass

        func(gen_describe_import_snapshot_tasks_paginator)


def test_describe_local_gateway_virtual_interfaces_return_pass(
    gen_describe_local_gateway_virtual_interfaces_paginator,
):
    @beartype
    def func() -> DescribeLocalGatewayVirtualInterfacesPaginator:
        return gen_describe_local_gateway_virtual_interfaces_paginator

    func()


def test_describe_local_gateway_virtual_interfaces_return_fail(
    gen_describe_import_snapshot_tasks_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLocalGatewayVirtualInterfacesPaginator:
            return gen_describe_import_snapshot_tasks_paginator

        func()


# ============================
# DescribeLocalGatewaysPaginator
# ============================


def test_describe_local_gateways_arg_pass(gen_describe_local_gateways_paginator):
    @beartype
    def func(param: DescribeLocalGatewaysPaginator):
        pass

    func(gen_describe_local_gateways_paginator)


def test_describe_local_gateways_arg_fail(
    gen_describe_classic_link_instances_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeLocalGatewaysPaginator):
            pass

        func(gen_describe_classic_link_instances_paginator)


def test_describe_local_gateways_return_pass(gen_describe_local_gateways_paginator):
    @beartype
    def func() -> DescribeLocalGatewaysPaginator:
        return gen_describe_local_gateways_paginator

    func()


def test_describe_local_gateways_return_fail(
    gen_describe_classic_link_instances_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeLocalGatewaysPaginator:
            return gen_describe_classic_link_instances_paginator

        func()


# ============================
# DescribeTransitGatewayMulticastDomainsPaginator
# ============================


def test_describe_transit_gateway_multicast_domains_arg_pass(
    gen_describe_transit_gateway_multicast_domains_paginator,
):
    @beartype
    def func(param: DescribeTransitGatewayMulticastDomainsPaginator):
        pass

    func(gen_describe_transit_gateway_multicast_domains_paginator)


def test_describe_transit_gateway_multicast_domains_arg_fail(
    gen_describe_vpc_endpoint_services_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewayMulticastDomainsPaginator):
            pass

        func(gen_describe_vpc_endpoint_services_paginator)


def test_describe_transit_gateway_multicast_domains_return_pass(
    gen_describe_transit_gateway_multicast_domains_paginator,
):
    @beartype
    def func() -> DescribeTransitGatewayMulticastDomainsPaginator:
        return gen_describe_transit_gateway_multicast_domains_paginator

    func()


def test_describe_transit_gateway_multicast_domains_return_fail(
    gen_describe_vpc_endpoint_services_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewayMulticastDomainsPaginator:
            return gen_describe_vpc_endpoint_services_paginator

        func()


# ============================
# DescribeTransitGatewayPeeringAttachmentsPaginator
# ============================


def test_describe_transit_gateway_peering_attachments_arg_pass(
    gen_describe_transit_gateway_peering_attachments_paginator,
):
    @beartype
    def func(param: DescribeTransitGatewayPeeringAttachmentsPaginator):
        pass

    func(gen_describe_transit_gateway_peering_attachments_paginator)


def test_describe_transit_gateway_peering_attachments_arg_fail(
    gen_describe_export_image_tasks_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewayPeeringAttachmentsPaginator):
            pass

        func(gen_describe_export_image_tasks_paginator)


def test_describe_transit_gateway_peering_attachments_return_pass(
    gen_describe_transit_gateway_peering_attachments_paginator,
):
    @beartype
    def func() -> DescribeTransitGatewayPeeringAttachmentsPaginator:
        return gen_describe_transit_gateway_peering_attachments_paginator

    func()


def test_describe_transit_gateway_peering_attachments_return_fail(
    gen_describe_export_image_tasks_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewayPeeringAttachmentsPaginator:
            return gen_describe_export_image_tasks_paginator

        func()


# ============================
# GetTransitGatewayMulticastDomainAssociationsPaginator
# ============================


def test_get_transit_gateway_multicast_domain_associations_arg_pass(
    gen_get_transit_gateway_multicast_domain_associations_paginator,
):
    @beartype
    def func(param: GetTransitGatewayMulticastDomainAssociationsPaginator):
        pass

    func(gen_get_transit_gateway_multicast_domain_associations_paginator)


def test_get_transit_gateway_multicast_domain_associations_arg_fail(
    gen_describe_capacity_reservation_fleets_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetTransitGatewayMulticastDomainAssociationsPaginator):
            pass

        func(gen_describe_capacity_reservation_fleets_paginator)


def test_get_transit_gateway_multicast_domain_associations_return_pass(
    gen_get_transit_gateway_multicast_domain_associations_paginator,
):
    @beartype
    def func() -> GetTransitGatewayMulticastDomainAssociationsPaginator:
        return gen_get_transit_gateway_multicast_domain_associations_paginator

    func()


def test_get_transit_gateway_multicast_domain_associations_return_fail(
    gen_describe_capacity_reservation_fleets_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetTransitGatewayMulticastDomainAssociationsPaginator:
            return gen_describe_capacity_reservation_fleets_paginator

        func()


# ============================
# SearchLocalGatewayRoutesPaginator
# ============================


def test_search_local_gateway_routes_arg_pass(
    gen_search_local_gateway_routes_paginator,
):
    @beartype
    def func(param: SearchLocalGatewayRoutesPaginator):
        pass

    func(gen_search_local_gateway_routes_paginator)


def test_search_local_gateway_routes_arg_fail(
    gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SearchLocalGatewayRoutesPaginator):
            pass

        func(
            gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator
        )


def test_search_local_gateway_routes_return_pass(
    gen_search_local_gateway_routes_paginator,
):
    @beartype
    def func() -> SearchLocalGatewayRoutesPaginator:
        return gen_search_local_gateway_routes_paginator

    func()


def test_search_local_gateway_routes_return_fail(
    gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SearchLocalGatewayRoutesPaginator:
            return gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator

        func()


# ============================
# SearchTransitGatewayMulticastGroupsPaginator
# ============================


def test_search_transit_gateway_multicast_groups_arg_pass(
    gen_search_transit_gateway_multicast_groups_paginator,
):
    @beartype
    def func(param: SearchTransitGatewayMulticastGroupsPaginator):
        pass

    func(gen_search_transit_gateway_multicast_groups_paginator)


def test_search_transit_gateway_multicast_groups_arg_fail(
    gen_describe_subnets_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SearchTransitGatewayMulticastGroupsPaginator):
            pass

        func(gen_describe_subnets_paginator)


def test_search_transit_gateway_multicast_groups_return_pass(
    gen_search_transit_gateway_multicast_groups_paginator,
):
    @beartype
    def func() -> SearchTransitGatewayMulticastGroupsPaginator:
        return gen_search_transit_gateway_multicast_groups_paginator

    func()


def test_search_transit_gateway_multicast_groups_return_fail(
    gen_describe_subnets_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SearchTransitGatewayMulticastGroupsPaginator:
            return gen_describe_subnets_paginator

        func()


# ============================
# DescribeManagedPrefixListsPaginator
# ============================


def test_describe_managed_prefix_lists_arg_pass(
    gen_describe_managed_prefix_lists_paginator,
):
    @beartype
    def func(param: DescribeManagedPrefixListsPaginator):
        pass

    func(gen_describe_managed_prefix_lists_paginator)


def test_describe_managed_prefix_lists_arg_fail(
    gen_describe_transit_gateway_multicast_domains_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeManagedPrefixListsPaginator):
            pass

        func(gen_describe_transit_gateway_multicast_domains_paginator)


def test_describe_managed_prefix_lists_return_pass(
    gen_describe_managed_prefix_lists_paginator,
):
    @beartype
    def func() -> DescribeManagedPrefixListsPaginator:
        return gen_describe_managed_prefix_lists_paginator

    func()


def test_describe_managed_prefix_lists_return_fail(
    gen_describe_transit_gateway_multicast_domains_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeManagedPrefixListsPaginator:
            return gen_describe_transit_gateway_multicast_domains_paginator

        func()


# ============================
# GetManagedPrefixListAssociationsPaginator
# ============================


def test_get_managed_prefix_list_associations_arg_pass(
    gen_get_managed_prefix_list_associations_paginator,
):
    @beartype
    def func(param: GetManagedPrefixListAssociationsPaginator):
        pass

    func(gen_get_managed_prefix_list_associations_paginator)


def test_get_managed_prefix_list_associations_arg_fail(
    gen_get_spot_placement_scores_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetManagedPrefixListAssociationsPaginator):
            pass

        func(gen_get_spot_placement_scores_paginator)


def test_get_managed_prefix_list_associations_return_pass(
    gen_get_managed_prefix_list_associations_paginator,
):
    @beartype
    def func() -> GetManagedPrefixListAssociationsPaginator:
        return gen_get_managed_prefix_list_associations_paginator

    func()


def test_get_managed_prefix_list_associations_return_fail(
    gen_get_spot_placement_scores_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetManagedPrefixListAssociationsPaginator:
            return gen_get_spot_placement_scores_paginator

        func()


# ============================
# GetManagedPrefixListEntriesPaginator
# ============================


def test_get_managed_prefix_list_entries_arg_pass(
    gen_get_managed_prefix_list_entries_paginator,
):
    @beartype
    def func(param: GetManagedPrefixListEntriesPaginator):
        pass

    func(gen_get_managed_prefix_list_entries_paginator)


def test_get_managed_prefix_list_entries_arg_fail(
    gen_describe_host_reservation_offerings_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetManagedPrefixListEntriesPaginator):
            pass

        func(gen_describe_host_reservation_offerings_paginator)


def test_get_managed_prefix_list_entries_return_pass(
    gen_get_managed_prefix_list_entries_paginator,
):
    @beartype
    def func() -> GetManagedPrefixListEntriesPaginator:
        return gen_get_managed_prefix_list_entries_paginator

    func()


def test_get_managed_prefix_list_entries_return_fail(
    gen_describe_host_reservation_offerings_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetManagedPrefixListEntriesPaginator:
            return gen_describe_host_reservation_offerings_paginator

        func()


# ============================
# GetGroupsForCapacityReservationPaginator
# ============================


def test_get_groups_for_capacity_reservation_arg_pass(
    gen_get_groups_for_capacity_reservation_paginator,
):
    @beartype
    def func(param: GetGroupsForCapacityReservationPaginator):
        pass

    func(gen_get_groups_for_capacity_reservation_paginator)


def test_get_groups_for_capacity_reservation_arg_fail(
    gen_get_transit_gateway_multicast_domain_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetGroupsForCapacityReservationPaginator):
            pass

        func(gen_get_transit_gateway_multicast_domain_associations_paginator)


def test_get_groups_for_capacity_reservation_return_pass(
    gen_get_groups_for_capacity_reservation_paginator,
):
    @beartype
    def func() -> GetGroupsForCapacityReservationPaginator:
        return gen_get_groups_for_capacity_reservation_paginator

    func()


def test_get_groups_for_capacity_reservation_return_fail(
    gen_get_transit_gateway_multicast_domain_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetGroupsForCapacityReservationPaginator:
            return gen_get_transit_gateway_multicast_domain_associations_paginator

        func()


# ============================
# DescribeCarrierGatewaysPaginator
# ============================


def test_describe_carrier_gateways_arg_pass(gen_describe_carrier_gateways_paginator):
    @beartype
    def func(param: DescribeCarrierGatewaysPaginator):
        pass

    func(gen_describe_carrier_gateways_paginator)


def test_describe_carrier_gateways_arg_fail(
    gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeCarrierGatewaysPaginator):
            pass

        func(
            gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator
        )


def test_describe_carrier_gateways_return_pass(gen_describe_carrier_gateways_paginator):
    @beartype
    def func() -> DescribeCarrierGatewaysPaginator:
        return gen_describe_carrier_gateways_paginator

    func()


def test_describe_carrier_gateways_return_fail(
    gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeCarrierGatewaysPaginator:
            return gen_describe_local_gateway_route_table_virtual_interface_group_associations_paginator

        func()


# ============================
# GetTransitGatewayPrefixListReferencesPaginator
# ============================


def test_get_transit_gateway_prefix_list_references_arg_pass(
    gen_get_transit_gateway_prefix_list_references_paginator,
):
    @beartype
    def func(param: GetTransitGatewayPrefixListReferencesPaginator):
        pass

    func(gen_get_transit_gateway_prefix_list_references_paginator)


def test_get_transit_gateway_prefix_list_references_arg_fail(
    gen_describe_network_acls_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetTransitGatewayPrefixListReferencesPaginator):
            pass

        func(gen_describe_network_acls_paginator)


def test_get_transit_gateway_prefix_list_references_return_pass(
    gen_get_transit_gateway_prefix_list_references_paginator,
):
    @beartype
    def func() -> GetTransitGatewayPrefixListReferencesPaginator:
        return gen_get_transit_gateway_prefix_list_references_paginator

    func()


def test_get_transit_gateway_prefix_list_references_return_fail(
    gen_describe_network_acls_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetTransitGatewayPrefixListReferencesPaginator:
            return gen_describe_network_acls_paginator

        func()


# ============================
# DescribeNetworkInsightsAnalysesPaginator
# ============================


def test_describe_network_insights_analyses_arg_pass(
    gen_describe_network_insights_analyses_paginator,
):
    @beartype
    def func(param: DescribeNetworkInsightsAnalysesPaginator):
        pass

    func(gen_describe_network_insights_analyses_paginator)


def test_describe_network_insights_analyses_arg_fail(
    gen_describe_launch_templates_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeNetworkInsightsAnalysesPaginator):
            pass

        func(gen_describe_launch_templates_paginator)


def test_describe_network_insights_analyses_return_pass(
    gen_describe_network_insights_analyses_paginator,
):
    @beartype
    def func() -> DescribeNetworkInsightsAnalysesPaginator:
        return gen_describe_network_insights_analyses_paginator

    func()


def test_describe_network_insights_analyses_return_fail(
    gen_describe_launch_templates_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeNetworkInsightsAnalysesPaginator:
            return gen_describe_launch_templates_paginator

        func()


# ============================
# DescribeNetworkInsightsPathsPaginator
# ============================


def test_describe_network_insights_paths_arg_pass(
    gen_describe_network_insights_paths_paginator,
):
    @beartype
    def func(param: DescribeNetworkInsightsPathsPaginator):
        pass

    func(gen_describe_network_insights_paths_paginator)


def test_describe_network_insights_paths_arg_fail(
    gen_describe_local_gateway_route_table_vpc_associations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeNetworkInsightsPathsPaginator):
            pass

        func(gen_describe_local_gateway_route_table_vpc_associations_paginator)


def test_describe_network_insights_paths_return_pass(
    gen_describe_network_insights_paths_paginator,
):
    @beartype
    def func() -> DescribeNetworkInsightsPathsPaginator:
        return gen_describe_network_insights_paths_paginator

    func()


def test_describe_network_insights_paths_return_fail(
    gen_describe_local_gateway_route_table_vpc_associations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeNetworkInsightsPathsPaginator:
            return gen_describe_local_gateway_route_table_vpc_associations_paginator

        func()


# ============================
# DescribeTransitGatewayConnectPeersPaginator
# ============================


def test_describe_transit_gateway_connect_peers_arg_pass(
    gen_describe_transit_gateway_connect_peers_paginator,
):
    @beartype
    def func(param: DescribeTransitGatewayConnectPeersPaginator):
        pass

    func(gen_describe_transit_gateway_connect_peers_paginator)


def test_describe_transit_gateway_connect_peers_arg_fail(
    gen_describe_spot_fleet_requests_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewayConnectPeersPaginator):
            pass

        func(gen_describe_spot_fleet_requests_paginator)


def test_describe_transit_gateway_connect_peers_return_pass(
    gen_describe_transit_gateway_connect_peers_paginator,
):
    @beartype
    def func() -> DescribeTransitGatewayConnectPeersPaginator:
        return gen_describe_transit_gateway_connect_peers_paginator

    func()


def test_describe_transit_gateway_connect_peers_return_fail(
    gen_describe_spot_fleet_requests_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewayConnectPeersPaginator:
            return gen_describe_spot_fleet_requests_paginator

        func()


# ============================
# DescribeTransitGatewayConnectsPaginator
# ============================


def test_describe_transit_gateway_connects_arg_pass(
    gen_describe_transit_gateway_connects_paginator,
):
    @beartype
    def func(param: DescribeTransitGatewayConnectsPaginator):
        pass

    func(gen_describe_transit_gateway_connects_paginator)


def test_describe_transit_gateway_connects_arg_fail(
    gen_describe_capacity_reservations_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTransitGatewayConnectsPaginator):
            pass

        func(gen_describe_capacity_reservations_paginator)


def test_describe_transit_gateway_connects_return_pass(
    gen_describe_transit_gateway_connects_paginator,
):
    @beartype
    def func() -> DescribeTransitGatewayConnectsPaginator:
        return gen_describe_transit_gateway_connects_paginator

    func()


def test_describe_transit_gateway_connects_return_fail(
    gen_describe_capacity_reservations_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTransitGatewayConnectsPaginator:
            return gen_describe_capacity_reservations_paginator

        func()


# ============================
# DescribeAddressesAttributePaginator
# ============================


def test_describe_addresses_attribute_arg_pass(
    gen_describe_addresses_attribute_paginator,
):
    @beartype
    def func(param: DescribeAddressesAttributePaginator):
        pass

    func(gen_describe_addresses_attribute_paginator)


def test_describe_addresses_attribute_arg_fail(gen_describe_dhcp_options_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeAddressesAttributePaginator):
            pass

        func(gen_describe_dhcp_options_paginator)


def test_describe_addresses_attribute_return_pass(
    gen_describe_addresses_attribute_paginator,
):
    @beartype
    def func() -> DescribeAddressesAttributePaginator:
        return gen_describe_addresses_attribute_paginator

    func()


def test_describe_addresses_attribute_return_fail(gen_describe_dhcp_options_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeAddressesAttributePaginator:
            return gen_describe_dhcp_options_paginator

        func()


# ============================
# DescribeReplaceRootVolumeTasksPaginator
# ============================


def test_describe_replace_root_volume_tasks_arg_pass(
    gen_describe_replace_root_volume_tasks_paginator,
):
    @beartype
    def func(param: DescribeReplaceRootVolumeTasksPaginator):
        pass

    func(gen_describe_replace_root_volume_tasks_paginator)


def test_describe_replace_root_volume_tasks_arg_fail(
    gen_describe_client_vpn_routes_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeReplaceRootVolumeTasksPaginator):
            pass

        func(gen_describe_client_vpn_routes_paginator)


def test_describe_replace_root_volume_tasks_return_pass(
    gen_describe_replace_root_volume_tasks_paginator,
):
    @beartype
    def func() -> DescribeReplaceRootVolumeTasksPaginator:
        return gen_describe_replace_root_volume_tasks_paginator

    func()


def test_describe_replace_root_volume_tasks_return_fail(
    gen_describe_client_vpn_routes_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeReplaceRootVolumeTasksPaginator:
            return gen_describe_client_vpn_routes_paginator

        func()


# ============================
# DescribeStoreImageTasksPaginator
# ============================


def test_describe_store_image_tasks_arg_pass(gen_describe_store_image_tasks_paginator):
    @beartype
    def func(param: DescribeStoreImageTasksPaginator):
        pass

    func(gen_describe_store_image_tasks_paginator)


def test_describe_store_image_tasks_arg_fail(
    gen_describe_addresses_attribute_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeStoreImageTasksPaginator):
            pass

        func(gen_describe_addresses_attribute_paginator)


def test_describe_store_image_tasks_return_pass(
    gen_describe_store_image_tasks_paginator,
):
    @beartype
    def func() -> DescribeStoreImageTasksPaginator:
        return gen_describe_store_image_tasks_paginator

    func()


def test_describe_store_image_tasks_return_fail(
    gen_describe_addresses_attribute_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeStoreImageTasksPaginator:
            return gen_describe_addresses_attribute_paginator

        func()


# ============================
# DescribeSecurityGroupRulesPaginator
# ============================


def test_describe_security_group_rules_arg_pass(
    gen_describe_security_group_rules_paginator,
):
    @beartype
    def func(param: DescribeSecurityGroupRulesPaginator):
        pass

    func(gen_describe_security_group_rules_paginator)


def test_describe_security_group_rules_arg_fail(
    gen_describe_instance_credit_specifications_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeSecurityGroupRulesPaginator):
            pass

        func(gen_describe_instance_credit_specifications_paginator)


def test_describe_security_group_rules_return_pass(
    gen_describe_security_group_rules_paginator,
):
    @beartype
    def func() -> DescribeSecurityGroupRulesPaginator:
        return gen_describe_security_group_rules_paginator

    func()


def test_describe_security_group_rules_return_fail(
    gen_describe_instance_credit_specifications_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeSecurityGroupRulesPaginator:
            return gen_describe_instance_credit_specifications_paginator

        func()


# ============================
# DescribeInstanceEventWindowsPaginator
# ============================


def test_describe_instance_event_windows_arg_pass(
    gen_describe_instance_event_windows_paginator,
):
    @beartype
    def func(param: DescribeInstanceEventWindowsPaginator):
        pass

    func(gen_describe_instance_event_windows_paginator)


def test_describe_instance_event_windows_arg_fail(
    gen_describe_instance_status_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeInstanceEventWindowsPaginator):
            pass

        func(gen_describe_instance_status_paginator)


def test_describe_instance_event_windows_return_pass(
    gen_describe_instance_event_windows_paginator,
):
    @beartype
    def func() -> DescribeInstanceEventWindowsPaginator:
        return gen_describe_instance_event_windows_paginator

    func()


def test_describe_instance_event_windows_return_fail(
    gen_describe_instance_status_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeInstanceEventWindowsPaginator:
            return gen_describe_instance_status_paginator

        func()


# ============================
# DescribeTrunkInterfaceAssociationsPaginator
# ============================


def test_describe_trunk_interface_associations_arg_pass(
    gen_describe_trunk_interface_associations_paginator,
):
    @beartype
    def func(param: DescribeTrunkInterfaceAssociationsPaginator):
        pass

    func(gen_describe_trunk_interface_associations_paginator)


def test_describe_trunk_interface_associations_arg_fail(
    gen_search_transit_gateway_multicast_groups_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeTrunkInterfaceAssociationsPaginator):
            pass

        func(gen_search_transit_gateway_multicast_groups_paginator)


def test_describe_trunk_interface_associations_return_pass(
    gen_describe_trunk_interface_associations_paginator,
):
    @beartype
    def func() -> DescribeTrunkInterfaceAssociationsPaginator:
        return gen_describe_trunk_interface_associations_paginator

    func()


def test_describe_trunk_interface_associations_return_fail(
    gen_search_transit_gateway_multicast_groups_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeTrunkInterfaceAssociationsPaginator:
            return gen_search_transit_gateway_multicast_groups_paginator

        func()


# ============================
# GetVpnConnectionDeviceTypesPaginator
# ============================


def test_get_vpn_connection_device_types_arg_pass(
    gen_get_vpn_connection_device_types_paginator,
):
    @beartype
    def func(param: GetVpnConnectionDeviceTypesPaginator):
        pass

    func(gen_get_vpn_connection_device_types_paginator)


def test_get_vpn_connection_device_types_arg_fail(gen_describe_subnets_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetVpnConnectionDeviceTypesPaginator):
            pass

        func(gen_describe_subnets_paginator)


def test_get_vpn_connection_device_types_return_pass(
    gen_get_vpn_connection_device_types_paginator,
):
    @beartype
    def func() -> GetVpnConnectionDeviceTypesPaginator:
        return gen_get_vpn_connection_device_types_paginator

    func()


def test_get_vpn_connection_device_types_return_fail(gen_describe_subnets_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetVpnConnectionDeviceTypesPaginator:
            return gen_describe_subnets_paginator

        func()


# ============================
# DescribeCapacityReservationFleetsPaginator
# ============================


def test_describe_capacity_reservation_fleets_arg_pass(
    gen_describe_capacity_reservation_fleets_paginator,
):
    @beartype
    def func(param: DescribeCapacityReservationFleetsPaginator):
        pass

    func(gen_describe_capacity_reservation_fleets_paginator)


def test_describe_capacity_reservation_fleets_arg_fail(
    gen_describe_scheduled_instance_availability_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DescribeCapacityReservationFleetsPaginator):
            pass

        func(gen_describe_scheduled_instance_availability_paginator)


def test_describe_capacity_reservation_fleets_return_pass(
    gen_describe_capacity_reservation_fleets_paginator,
):
    @beartype
    def func() -> DescribeCapacityReservationFleetsPaginator:
        return gen_describe_capacity_reservation_fleets_paginator

    func()


def test_describe_capacity_reservation_fleets_return_fail(
    gen_describe_scheduled_instance_availability_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DescribeCapacityReservationFleetsPaginator:
            return gen_describe_scheduled_instance_availability_paginator

        func()


# ============================
# GetInstanceTypesFromInstanceRequirementsPaginator
# ============================


def test_get_instance_types_from_instance_requirements_arg_pass(
    gen_get_instance_types_from_instance_requirements_paginator,
):
    @beartype
    def func(param: GetInstanceTypesFromInstanceRequirementsPaginator):
        pass

    func(gen_get_instance_types_from_instance_requirements_paginator)


def test_get_instance_types_from_instance_requirements_arg_fail(
    gen_describe_moving_addresses_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetInstanceTypesFromInstanceRequirementsPaginator):
            pass

        func(gen_describe_moving_addresses_paginator)


def test_get_instance_types_from_instance_requirements_return_pass(
    gen_get_instance_types_from_instance_requirements_paginator,
):
    @beartype
    def func() -> GetInstanceTypesFromInstanceRequirementsPaginator:
        return gen_get_instance_types_from_instance_requirements_paginator

    func()


def test_get_instance_types_from_instance_requirements_return_fail(
    gen_describe_moving_addresses_paginator,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetInstanceTypesFromInstanceRequirementsPaginator:
            return gen_describe_moving_addresses_paginator

        func()


# ============================
# GetSpotPlacementScoresPaginator
# ============================


def test_get_spot_placement_scores_arg_pass(gen_get_spot_placement_scores_paginator):
    @beartype
    def func(param: GetSpotPlacementScoresPaginator):
        pass

    func(gen_get_spot_placement_scores_paginator)


def test_get_spot_placement_scores_arg_fail(gen_describe_prefix_lists_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GetSpotPlacementScoresPaginator):
            pass

        func(gen_describe_prefix_lists_paginator)


def test_get_spot_placement_scores_return_pass(gen_get_spot_placement_scores_paginator):
    @beartype
    def func() -> GetSpotPlacementScoresPaginator:
        return gen_get_spot_placement_scores_paginator

    func()


def test_get_spot_placement_scores_return_fail(gen_describe_prefix_lists_paginator):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetSpotPlacementScoresPaginator:
            return gen_describe_prefix_lists_paginator

        func()
