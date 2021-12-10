import pytest
from bearboto3.ec2 import (
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
    InstanceVolumesCollection,
    InstanceVpcAddressesCollection,
    PlacementGroupInstancesCollection,
    SubnetInstancesCollection,
    SubnetNetworkInterfacesCollection,
    VolumeSnapshotsCollection,
    VpcAcceptedVpcPeeringConnectionsCollection,
    VpcInstancesCollection,
    VpcInternetGatewaysCollection,
    VpcNetworkAclsCollection,
    VpcNetworkInterfacesCollection,
    VpcRequestedVpcPeeringConnectionsCollection,
    VpcRouteTablesCollection,
    VpcSecurityGroupsCollection,
    VpcSubnetsCollection,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ServiceResourceClassicAddressesCollection
# ============================


def test_classic_addresses_arg_pass(gen_service_resource_classic_addresses_collection):
    @beartype
    def func(param: ServiceResourceClassicAddressesCollection):
        pass

    func(gen_service_resource_classic_addresses_collection)


def test_classic_addresses_arg_fail(gen_service_resource_network_acls_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceClassicAddressesCollection):
            pass

        func(gen_service_resource_network_acls_collection)


def test_classic_addresses_return_pass(
    gen_service_resource_classic_addresses_collection,
):
    @beartype
    def func() -> ServiceResourceClassicAddressesCollection:
        return gen_service_resource_classic_addresses_collection

    func()


def test_classic_addresses_return_fail(gen_service_resource_network_acls_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceClassicAddressesCollection:
            return gen_service_resource_network_acls_collection

        func()


# ============================
# ServiceResourceDhcpOptionsSetsCollection
# ============================


def test_dhcp_options_sets_arg_pass(gen_service_resource_dhcp_options_sets_collection):
    @beartype
    def func(param: ServiceResourceDhcpOptionsSetsCollection):
        pass

    func(gen_service_resource_dhcp_options_sets_collection)


def test_dhcp_options_sets_arg_fail(
    gen_vpc_accepted_vpc_peering_connections_collection,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceDhcpOptionsSetsCollection):
            pass

        func(gen_vpc_accepted_vpc_peering_connections_collection)


def test_dhcp_options_sets_return_pass(
    gen_service_resource_dhcp_options_sets_collection,
):
    @beartype
    def func() -> ServiceResourceDhcpOptionsSetsCollection:
        return gen_service_resource_dhcp_options_sets_collection

    func()


def test_dhcp_options_sets_return_fail(
    gen_vpc_accepted_vpc_peering_connections_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceDhcpOptionsSetsCollection:
            return gen_vpc_accepted_vpc_peering_connections_collection

        func()


# ============================
# ServiceResourceImagesCollection
# ============================


def test_images_arg_pass(gen_service_resource_images_collection):
    @beartype
    def func(param: ServiceResourceImagesCollection):
        pass

    func(gen_service_resource_images_collection)


def test_images_arg_fail(gen_service_resource_network_acls_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceImagesCollection):
            pass

        func(gen_service_resource_network_acls_collection)


def test_images_return_pass(gen_service_resource_images_collection):
    @beartype
    def func() -> ServiceResourceImagesCollection:
        return gen_service_resource_images_collection

    func()


def test_images_return_fail(gen_service_resource_network_acls_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceImagesCollection:
            return gen_service_resource_network_acls_collection

        func()


# ============================
# ServiceResourceInstancesCollection
# ============================


def test_instances_arg_pass(gen_service_resource_instances_collection):
    @beartype
    def func(param: ServiceResourceInstancesCollection):
        pass

    func(gen_service_resource_instances_collection)


def test_instances_arg_fail(gen_subnet_instances_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceInstancesCollection):
            pass

        func(gen_subnet_instances_collection)


def test_instances_return_pass(gen_service_resource_instances_collection):
    @beartype
    def func() -> ServiceResourceInstancesCollection:
        return gen_service_resource_instances_collection

    func()


def test_instances_return_fail(gen_subnet_instances_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceInstancesCollection:
            return gen_subnet_instances_collection

        func()


# ============================
# ServiceResourceInternetGatewaysCollection
# ============================


def test_internet_gateways_arg_pass(gen_service_resource_internet_gateways_collection):
    @beartype
    def func(param: ServiceResourceInternetGatewaysCollection):
        pass

    func(gen_service_resource_internet_gateways_collection)


def test_internet_gateways_arg_fail(gen_service_resource_dhcp_options_sets_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceInternetGatewaysCollection):
            pass

        func(gen_service_resource_dhcp_options_sets_collection)


def test_internet_gateways_return_pass(
    gen_service_resource_internet_gateways_collection,
):
    @beartype
    def func() -> ServiceResourceInternetGatewaysCollection:
        return gen_service_resource_internet_gateways_collection

    func()


def test_internet_gateways_return_fail(
    gen_service_resource_dhcp_options_sets_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceInternetGatewaysCollection:
            return gen_service_resource_dhcp_options_sets_collection

        func()


# ============================
# ServiceResourceKeyPairsCollection
# ============================


def test_key_pairs_arg_pass(gen_service_resource_key_pairs_collection):
    @beartype
    def func(param: ServiceResourceKeyPairsCollection):
        pass

    func(gen_service_resource_key_pairs_collection)


def test_key_pairs_arg_fail(gen_placement_group_instances_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceKeyPairsCollection):
            pass

        func(gen_placement_group_instances_collection)


def test_key_pairs_return_pass(gen_service_resource_key_pairs_collection):
    @beartype
    def func() -> ServiceResourceKeyPairsCollection:
        return gen_service_resource_key_pairs_collection

    func()


def test_key_pairs_return_fail(gen_placement_group_instances_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceKeyPairsCollection:
            return gen_placement_group_instances_collection

        func()


# ============================
# ServiceResourceNetworkAclsCollection
# ============================


def test_network_acls_arg_pass(gen_service_resource_network_acls_collection):
    @beartype
    def func(param: ServiceResourceNetworkAclsCollection):
        pass

    func(gen_service_resource_network_acls_collection)


def test_network_acls_arg_fail(gen_vpc_internet_gateways_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceNetworkAclsCollection):
            pass

        func(gen_vpc_internet_gateways_collection)


def test_network_acls_return_pass(gen_service_resource_network_acls_collection):
    @beartype
    def func() -> ServiceResourceNetworkAclsCollection:
        return gen_service_resource_network_acls_collection

    func()


def test_network_acls_return_fail(gen_vpc_internet_gateways_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceNetworkAclsCollection:
            return gen_vpc_internet_gateways_collection

        func()


# ============================
# ServiceResourceNetworkInterfacesCollection
# ============================


def test_network_interfaces_arg_pass(
    gen_service_resource_network_interfaces_collection,
):
    @beartype
    def func(param: ServiceResourceNetworkInterfacesCollection):
        pass

    func(gen_service_resource_network_interfaces_collection)


def test_network_interfaces_arg_fail(gen_service_resource_volumes_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceNetworkInterfacesCollection):
            pass

        func(gen_service_resource_volumes_collection)


def test_network_interfaces_return_pass(
    gen_service_resource_network_interfaces_collection,
):
    @beartype
    def func() -> ServiceResourceNetworkInterfacesCollection:
        return gen_service_resource_network_interfaces_collection

    func()


def test_network_interfaces_return_fail(gen_service_resource_volumes_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceNetworkInterfacesCollection:
            return gen_service_resource_volumes_collection

        func()


# ============================
# ServiceResourcePlacementGroupsCollection
# ============================


def test_placement_groups_arg_pass(gen_service_resource_placement_groups_collection):
    @beartype
    def func(param: ServiceResourcePlacementGroupsCollection):
        pass

    func(gen_service_resource_placement_groups_collection)


def test_placement_groups_arg_fail(gen_service_resource_route_tables_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourcePlacementGroupsCollection):
            pass

        func(gen_service_resource_route_tables_collection)


def test_placement_groups_return_pass(gen_service_resource_placement_groups_collection):
    @beartype
    def func() -> ServiceResourcePlacementGroupsCollection:
        return gen_service_resource_placement_groups_collection

    func()


def test_placement_groups_return_fail(gen_service_resource_route_tables_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourcePlacementGroupsCollection:
            return gen_service_resource_route_tables_collection

        func()


# ============================
# ServiceResourceRouteTablesCollection
# ============================


def test_route_tables_arg_pass(gen_service_resource_route_tables_collection):
    @beartype
    def func(param: ServiceResourceRouteTablesCollection):
        pass

    func(gen_service_resource_route_tables_collection)


def test_route_tables_arg_fail(gen_service_resource_vpc_peering_connections_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceRouteTablesCollection):
            pass

        func(gen_service_resource_vpc_peering_connections_collection)


def test_route_tables_return_pass(gen_service_resource_route_tables_collection):
    @beartype
    def func() -> ServiceResourceRouteTablesCollection:
        return gen_service_resource_route_tables_collection

    func()


def test_route_tables_return_fail(
    gen_service_resource_vpc_peering_connections_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceRouteTablesCollection:
            return gen_service_resource_vpc_peering_connections_collection

        func()


# ============================
# ServiceResourceSecurityGroupsCollection
# ============================


def test_security_groups_arg_pass(gen_service_resource_security_groups_collection):
    @beartype
    def func(param: ServiceResourceSecurityGroupsCollection):
        pass

    func(gen_service_resource_security_groups_collection)


def test_security_groups_arg_fail(gen_service_resource_images_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceSecurityGroupsCollection):
            pass

        func(gen_service_resource_images_collection)


def test_security_groups_return_pass(gen_service_resource_security_groups_collection):
    @beartype
    def func() -> ServiceResourceSecurityGroupsCollection:
        return gen_service_resource_security_groups_collection

    func()


def test_security_groups_return_fail(gen_service_resource_images_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceSecurityGroupsCollection:
            return gen_service_resource_images_collection

        func()


# ============================
# ServiceResourceSnapshotsCollection
# ============================


def test_snapshots_arg_pass(gen_service_resource_snapshots_collection):
    @beartype
    def func(param: ServiceResourceSnapshotsCollection):
        pass

    func(gen_service_resource_snapshots_collection)


def test_snapshots_arg_fail(gen_service_resource_route_tables_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceSnapshotsCollection):
            pass

        func(gen_service_resource_route_tables_collection)


def test_snapshots_return_pass(gen_service_resource_snapshots_collection):
    @beartype
    def func() -> ServiceResourceSnapshotsCollection:
        return gen_service_resource_snapshots_collection

    func()


def test_snapshots_return_fail(gen_service_resource_route_tables_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceSnapshotsCollection:
            return gen_service_resource_route_tables_collection

        func()


# ============================
# ServiceResourceSubnetsCollection
# ============================


def test_subnets_arg_pass(gen_service_resource_subnets_collection):
    @beartype
    def func(param: ServiceResourceSubnetsCollection):
        pass

    func(gen_service_resource_subnets_collection)


def test_subnets_arg_fail(gen_service_resource_snapshots_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceSubnetsCollection):
            pass

        func(gen_service_resource_snapshots_collection)


def test_subnets_return_pass(gen_service_resource_subnets_collection):
    @beartype
    def func() -> ServiceResourceSubnetsCollection:
        return gen_service_resource_subnets_collection

    func()


def test_subnets_return_fail(gen_service_resource_snapshots_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceSubnetsCollection:
            return gen_service_resource_snapshots_collection

        func()


# ============================
# ServiceResourceVolumesCollection
# ============================


def test_volumes_arg_pass(gen_service_resource_volumes_collection):
    @beartype
    def func(param: ServiceResourceVolumesCollection):
        pass

    func(gen_service_resource_volumes_collection)


def test_volumes_arg_fail(gen_vpc_accepted_vpc_peering_connections_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceVolumesCollection):
            pass

        func(gen_vpc_accepted_vpc_peering_connections_collection)


def test_volumes_return_pass(gen_service_resource_volumes_collection):
    @beartype
    def func() -> ServiceResourceVolumesCollection:
        return gen_service_resource_volumes_collection

    func()


def test_volumes_return_fail(gen_vpc_accepted_vpc_peering_connections_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceVolumesCollection:
            return gen_vpc_accepted_vpc_peering_connections_collection

        func()


# ============================
# ServiceResourceVpcAddressesCollection
# ============================


def test_vpc_addresses_arg_pass(gen_service_resource_vpc_addresses_collection):
    @beartype
    def func(param: ServiceResourceVpcAddressesCollection):
        pass

    func(gen_service_resource_vpc_addresses_collection)


def test_vpc_addresses_arg_fail(gen_volume_snapshots_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceVpcAddressesCollection):
            pass

        func(gen_volume_snapshots_collection)


def test_vpc_addresses_return_pass(gen_service_resource_vpc_addresses_collection):
    @beartype
    def func() -> ServiceResourceVpcAddressesCollection:
        return gen_service_resource_vpc_addresses_collection

    func()


def test_vpc_addresses_return_fail(gen_volume_snapshots_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceVpcAddressesCollection:
            return gen_volume_snapshots_collection

        func()


# ============================
# ServiceResourceVpcPeeringConnectionsCollection
# ============================


def test_vpc_peering_connections_arg_pass(
    gen_service_resource_vpc_peering_connections_collection,
):
    @beartype
    def func(param: ServiceResourceVpcPeeringConnectionsCollection):
        pass

    func(gen_service_resource_vpc_peering_connections_collection)


def test_vpc_peering_connections_arg_fail(gen_service_resource_snapshots_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceVpcPeeringConnectionsCollection):
            pass

        func(gen_service_resource_snapshots_collection)


def test_vpc_peering_connections_return_pass(
    gen_service_resource_vpc_peering_connections_collection,
):
    @beartype
    def func() -> ServiceResourceVpcPeeringConnectionsCollection:
        return gen_service_resource_vpc_peering_connections_collection

    func()


def test_vpc_peering_connections_return_fail(gen_service_resource_snapshots_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceVpcPeeringConnectionsCollection:
            return gen_service_resource_snapshots_collection

        func()


# ============================
# ServiceResourceVpcsCollection
# ============================


def test_vpcs_arg_pass(gen_service_resource_vpcs_collection):
    @beartype
    def func(param: ServiceResourceVpcsCollection):
        pass

    func(gen_service_resource_vpcs_collection)


def test_vpcs_arg_fail(gen_service_resource_images_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceVpcsCollection):
            pass

        func(gen_service_resource_images_collection)


def test_vpcs_return_pass(gen_service_resource_vpcs_collection):
    @beartype
    def func() -> ServiceResourceVpcsCollection:
        return gen_service_resource_vpcs_collection

    func()


def test_vpcs_return_fail(gen_service_resource_images_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceVpcsCollection:
            return gen_service_resource_images_collection

        func()


# ============================
# InstanceVolumesCollection
# ============================


def test_volumes_arg_pass(gen_instance_volumes_collection):
    @beartype
    def func(param: InstanceVolumesCollection):
        pass

    func(gen_instance_volumes_collection)


def test_volumes_arg_fail(gen_service_resource_network_acls_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: InstanceVolumesCollection):
            pass

        func(gen_service_resource_network_acls_collection)


def test_volumes_return_pass(gen_instance_volumes_collection):
    @beartype
    def func() -> InstanceVolumesCollection:
        return gen_instance_volumes_collection

    func()


def test_volumes_return_fail(gen_service_resource_network_acls_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceVolumesCollection:
            return gen_service_resource_network_acls_collection

        func()


# ============================
# InstanceVpcAddressesCollection
# ============================


def test_vpc_addresses_arg_pass(gen_instance_vpc_addresses_collection):
    @beartype
    def func(param: InstanceVpcAddressesCollection):
        pass

    func(gen_instance_vpc_addresses_collection)


def test_vpc_addresses_arg_fail(gen_vpc_network_acls_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: InstanceVpcAddressesCollection):
            pass

        func(gen_vpc_network_acls_collection)


def test_vpc_addresses_return_pass(gen_instance_vpc_addresses_collection):
    @beartype
    def func() -> InstanceVpcAddressesCollection:
        return gen_instance_vpc_addresses_collection

    func()


def test_vpc_addresses_return_fail(gen_vpc_network_acls_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceVpcAddressesCollection:
            return gen_vpc_network_acls_collection

        func()


# ============================
# PlacementGroupInstancesCollection
# ============================


def test_instances_arg_pass(gen_placement_group_instances_collection):
    @beartype
    def func(param: PlacementGroupInstancesCollection):
        pass

    func(gen_placement_group_instances_collection)


def test_instances_arg_fail(gen_vpc_requested_vpc_peering_connections_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PlacementGroupInstancesCollection):
            pass

        func(gen_vpc_requested_vpc_peering_connections_collection)


def test_instances_return_pass(gen_placement_group_instances_collection):
    @beartype
    def func() -> PlacementGroupInstancesCollection:
        return gen_placement_group_instances_collection

    func()


def test_instances_return_fail(gen_vpc_requested_vpc_peering_connections_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PlacementGroupInstancesCollection:
            return gen_vpc_requested_vpc_peering_connections_collection

        func()


# ============================
# SubnetInstancesCollection
# ============================


def test_instances_arg_pass(gen_subnet_instances_collection):
    @beartype
    def func(param: SubnetInstancesCollection):
        pass

    func(gen_subnet_instances_collection)


def test_instances_arg_fail(gen_vpc_network_acls_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SubnetInstancesCollection):
            pass

        func(gen_vpc_network_acls_collection)


def test_instances_return_pass(gen_subnet_instances_collection):
    @beartype
    def func() -> SubnetInstancesCollection:
        return gen_subnet_instances_collection

    func()


def test_instances_return_fail(gen_vpc_network_acls_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SubnetInstancesCollection:
            return gen_vpc_network_acls_collection

        func()


# ============================
# SubnetNetworkInterfacesCollection
# ============================


def test_network_interfaces_arg_pass(gen_subnet_network_interfaces_collection):
    @beartype
    def func(param: SubnetNetworkInterfacesCollection):
        pass

    func(gen_subnet_network_interfaces_collection)


def test_network_interfaces_arg_fail(gen_vpc_subnets_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SubnetNetworkInterfacesCollection):
            pass

        func(gen_vpc_subnets_collection)


def test_network_interfaces_return_pass(gen_subnet_network_interfaces_collection):
    @beartype
    def func() -> SubnetNetworkInterfacesCollection:
        return gen_subnet_network_interfaces_collection

    func()


def test_network_interfaces_return_fail(gen_vpc_subnets_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SubnetNetworkInterfacesCollection:
            return gen_vpc_subnets_collection

        func()


# ============================
# VolumeSnapshotsCollection
# ============================


def test_snapshots_arg_pass(gen_volume_snapshots_collection):
    @beartype
    def func(param: VolumeSnapshotsCollection):
        pass

    func(gen_volume_snapshots_collection)


def test_snapshots_arg_fail(gen_vpc_subnets_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VolumeSnapshotsCollection):
            pass

        func(gen_vpc_subnets_collection)


def test_snapshots_return_pass(gen_volume_snapshots_collection):
    @beartype
    def func() -> VolumeSnapshotsCollection:
        return gen_volume_snapshots_collection

    func()


def test_snapshots_return_fail(gen_vpc_subnets_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VolumeSnapshotsCollection:
            return gen_vpc_subnets_collection

        func()


# ============================
# VpcAcceptedVpcPeeringConnectionsCollection
# ============================


def test_accepted_vpc_peering_connections_arg_pass(
    gen_vpc_accepted_vpc_peering_connections_collection,
):
    @beartype
    def func(param: VpcAcceptedVpcPeeringConnectionsCollection):
        pass

    func(gen_vpc_accepted_vpc_peering_connections_collection)


def test_accepted_vpc_peering_connections_arg_fail(
    gen_service_resource_dhcp_options_sets_collection,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcAcceptedVpcPeeringConnectionsCollection):
            pass

        func(gen_service_resource_dhcp_options_sets_collection)


def test_accepted_vpc_peering_connections_return_pass(
    gen_vpc_accepted_vpc_peering_connections_collection,
):
    @beartype
    def func() -> VpcAcceptedVpcPeeringConnectionsCollection:
        return gen_vpc_accepted_vpc_peering_connections_collection

    func()


def test_accepted_vpc_peering_connections_return_fail(
    gen_service_resource_dhcp_options_sets_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcAcceptedVpcPeeringConnectionsCollection:
            return gen_service_resource_dhcp_options_sets_collection

        func()


# ============================
# VpcInstancesCollection
# ============================


def test_instances_arg_pass(gen_vpc_instances_collection):
    @beartype
    def func(param: VpcInstancesCollection):
        pass

    func(gen_vpc_instances_collection)


def test_instances_arg_fail(gen_service_resource_route_tables_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcInstancesCollection):
            pass

        func(gen_service_resource_route_tables_collection)


def test_instances_return_pass(gen_vpc_instances_collection):
    @beartype
    def func() -> VpcInstancesCollection:
        return gen_vpc_instances_collection

    func()


def test_instances_return_fail(gen_service_resource_route_tables_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcInstancesCollection:
            return gen_service_resource_route_tables_collection

        func()


# ============================
# VpcInternetGatewaysCollection
# ============================


def test_internet_gateways_arg_pass(gen_vpc_internet_gateways_collection):
    @beartype
    def func(param: VpcInternetGatewaysCollection):
        pass

    func(gen_vpc_internet_gateways_collection)


def test_internet_gateways_arg_fail(gen_service_resource_internet_gateways_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcInternetGatewaysCollection):
            pass

        func(gen_service_resource_internet_gateways_collection)


def test_internet_gateways_return_pass(gen_vpc_internet_gateways_collection):
    @beartype
    def func() -> VpcInternetGatewaysCollection:
        return gen_vpc_internet_gateways_collection

    func()


def test_internet_gateways_return_fail(
    gen_service_resource_internet_gateways_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcInternetGatewaysCollection:
            return gen_service_resource_internet_gateways_collection

        func()


# ============================
# VpcNetworkAclsCollection
# ============================


def test_network_acls_arg_pass(gen_vpc_network_acls_collection):
    @beartype
    def func(param: VpcNetworkAclsCollection):
        pass

    func(gen_vpc_network_acls_collection)


def test_network_acls_arg_fail(gen_service_resource_images_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcNetworkAclsCollection):
            pass

        func(gen_service_resource_images_collection)


def test_network_acls_return_pass(gen_vpc_network_acls_collection):
    @beartype
    def func() -> VpcNetworkAclsCollection:
        return gen_vpc_network_acls_collection

    func()


def test_network_acls_return_fail(gen_service_resource_images_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcNetworkAclsCollection:
            return gen_service_resource_images_collection

        func()


# ============================
# VpcNetworkInterfacesCollection
# ============================


def test_network_interfaces_arg_pass(gen_vpc_network_interfaces_collection):
    @beartype
    def func(param: VpcNetworkInterfacesCollection):
        pass

    func(gen_vpc_network_interfaces_collection)


def test_network_interfaces_arg_fail(gen_service_resource_internet_gateways_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcNetworkInterfacesCollection):
            pass

        func(gen_service_resource_internet_gateways_collection)


def test_network_interfaces_return_pass(gen_vpc_network_interfaces_collection):
    @beartype
    def func() -> VpcNetworkInterfacesCollection:
        return gen_vpc_network_interfaces_collection

    func()


def test_network_interfaces_return_fail(
    gen_service_resource_internet_gateways_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcNetworkInterfacesCollection:
            return gen_service_resource_internet_gateways_collection

        func()


# ============================
# VpcRequestedVpcPeeringConnectionsCollection
# ============================


def test_requested_vpc_peering_connections_arg_pass(
    gen_vpc_requested_vpc_peering_connections_collection,
):
    @beartype
    def func(param: VpcRequestedVpcPeeringConnectionsCollection):
        pass

    func(gen_vpc_requested_vpc_peering_connections_collection)


def test_requested_vpc_peering_connections_arg_fail(
    gen_subnet_network_interfaces_collection,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcRequestedVpcPeeringConnectionsCollection):
            pass

        func(gen_subnet_network_interfaces_collection)


def test_requested_vpc_peering_connections_return_pass(
    gen_vpc_requested_vpc_peering_connections_collection,
):
    @beartype
    def func() -> VpcRequestedVpcPeeringConnectionsCollection:
        return gen_vpc_requested_vpc_peering_connections_collection

    func()


def test_requested_vpc_peering_connections_return_fail(
    gen_subnet_network_interfaces_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcRequestedVpcPeeringConnectionsCollection:
            return gen_subnet_network_interfaces_collection

        func()


# ============================
# VpcRouteTablesCollection
# ============================


def test_route_tables_arg_pass(gen_vpc_route_tables_collection):
    @beartype
    def func(param: VpcRouteTablesCollection):
        pass

    func(gen_vpc_route_tables_collection)


def test_route_tables_arg_fail(gen_service_resource_dhcp_options_sets_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcRouteTablesCollection):
            pass

        func(gen_service_resource_dhcp_options_sets_collection)


def test_route_tables_return_pass(gen_vpc_route_tables_collection):
    @beartype
    def func() -> VpcRouteTablesCollection:
        return gen_vpc_route_tables_collection

    func()


def test_route_tables_return_fail(gen_service_resource_dhcp_options_sets_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcRouteTablesCollection:
            return gen_service_resource_dhcp_options_sets_collection

        func()


# ============================
# VpcSecurityGroupsCollection
# ============================


def test_security_groups_arg_pass(gen_vpc_security_groups_collection):
    @beartype
    def func(param: VpcSecurityGroupsCollection):
        pass

    func(gen_vpc_security_groups_collection)


def test_security_groups_arg_fail(gen_service_resource_key_pairs_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcSecurityGroupsCollection):
            pass

        func(gen_service_resource_key_pairs_collection)


def test_security_groups_return_pass(gen_vpc_security_groups_collection):
    @beartype
    def func() -> VpcSecurityGroupsCollection:
        return gen_vpc_security_groups_collection

    func()


def test_security_groups_return_fail(gen_service_resource_key_pairs_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcSecurityGroupsCollection:
            return gen_service_resource_key_pairs_collection

        func()


# ============================
# VpcSubnetsCollection
# ============================


def test_subnets_arg_pass(gen_vpc_subnets_collection):
    @beartype
    def func(param: VpcSubnetsCollection):
        pass

    func(gen_vpc_subnets_collection)


def test_subnets_arg_fail(gen_vpc_route_tables_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcSubnetsCollection):
            pass

        func(gen_vpc_route_tables_collection)


def test_subnets_return_pass(gen_vpc_subnets_collection):
    @beartype
    def func() -> VpcSubnetsCollection:
        return gen_vpc_subnets_collection

    func()


def test_subnets_return_fail(gen_vpc_route_tables_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcSubnetsCollection:
            return gen_vpc_route_tables_collection

        func()
