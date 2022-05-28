import pytest
from bearboto3.ec2 import (
    ClassicAddress,
    DhcpOptions,
    Image,
    Instance,
    InternetGateway,
    KeyPair,
    KeyPairInfo,
    NetworkAcl,
    NetworkInterface,
    NetworkInterfaceAssociation,
    PlacementGroup,
    Route,
    RouteTable,
    RouteTableAssociation,
    SecurityGroup,
    Snapshot,
    Subnet,
    Tag,
    Volume,
    Vpc,
    VpcAddress,
    VpcPeeringConnection,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)

# ============================
# ClassicAddress
# ============================


def test_classic_address_arg_pass(gen_classic_address):
    @beartype
    def func(param: ClassicAddress):
        pass

    func(gen_classic_address)


def test_classic_address_arg_fail(gen_key_pair):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ClassicAddress):
            pass

        func(gen_key_pair)


def test_classic_address_return_pass(gen_classic_address):
    @beartype
    def func() -> ClassicAddress:
        return gen_classic_address

    func()


def test_classic_address_return_fail(gen_key_pair):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ClassicAddress:
            return gen_key_pair

        func()


# ============================
# DhcpOptions
# ============================


def test_dhcp_options_arg_pass(gen_dhcp_options):
    @beartype
    def func(param: DhcpOptions):
        pass

    func(gen_dhcp_options)


def test_dhcp_options_arg_fail(gen_route_table):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: DhcpOptions):
            pass

        func(gen_route_table)


def test_dhcp_options_return_pass(gen_dhcp_options):
    @beartype
    def func() -> DhcpOptions:
        return gen_dhcp_options

    func()


def test_dhcp_options_return_fail(gen_route_table):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> DhcpOptions:
            return gen_route_table

        func()


# ============================
# Image
# ============================


def test_image_arg_pass(gen_image):
    @beartype
    def func(param: Image):
        pass

    func(gen_image)


def test_image_arg_fail(gen_classic_address):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Image):
            pass

        func(gen_classic_address)


def test_image_return_pass(gen_image):
    @beartype
    def func() -> Image:
        return gen_image

    func()


def test_image_return_fail(gen_classic_address):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Image:
            return gen_classic_address

        func()


# ============================
# Instance
# ============================


def test_instance_arg_pass(gen_instance):
    @beartype
    def func(param: Instance):
        pass

    func(gen_instance)


def test_instance_arg_fail(gen_network_acl):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Instance):
            pass

        func(gen_network_acl)


def test_instance_return_pass(gen_instance):
    @beartype
    def func() -> Instance:
        return gen_instance

    func()


def test_instance_return_fail(gen_network_acl):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Instance:
            return gen_network_acl

        func()


# ============================
# InternetGateway
# ============================


def test_internet_gateway_arg_pass(gen_internet_gateway):
    @beartype
    def func(param: InternetGateway):
        pass

    func(gen_internet_gateway)


def test_internet_gateway_arg_fail(gen_tag):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: InternetGateway):
            pass

        func(gen_tag)


def test_internet_gateway_return_pass(gen_internet_gateway):
    @beartype
    def func() -> InternetGateway:
        return gen_internet_gateway

    func()


def test_internet_gateway_return_fail(gen_tag):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InternetGateway:
            return gen_tag

        func()


# ============================
# KeyPair
# ============================


def test_key_pair_arg_pass(gen_key_pair):
    @beartype
    def func(param: KeyPair):
        pass

    func(gen_key_pair)


def test_key_pair_arg_fail(gen_volume):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: KeyPair):
            pass

        func(gen_volume)


def test_key_pair_return_pass(gen_key_pair):
    @beartype
    def func() -> KeyPair:
        return gen_key_pair

    func()


def test_key_pair_return_fail(gen_volume):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> KeyPair:
            return gen_volume

        func()


# ============================
# KeyPairInfo
# ============================


def test_key_pair_info_arg_pass(gen_key_pair):
    @beartype
    def func(param: KeyPairInfo):
        pass

    func(gen_key_pair)


def test_key_pair_info_arg_fail(gen_route_table_association):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: KeyPairInfo):
            pass

        func(gen_route_table_association)


def test_key_pair_info_return_pass(gen_key_pair):
    @beartype
    def func() -> KeyPairInfo:
        return gen_key_pair

    func()


def test_key_pair_info_return_fail(gen_route_table_association):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> KeyPairInfo:
            return gen_route_table_association

        func()


# ============================
# NetworkAcl
# ============================


def test_network_acl_arg_pass(gen_network_acl):
    @beartype
    def func(param: NetworkAcl):
        pass

    func(gen_network_acl)


def test_network_acl_arg_fail(gen_route_table):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: NetworkAcl):
            pass

        func(gen_route_table)


def test_network_acl_return_pass(gen_network_acl):
    @beartype
    def func() -> NetworkAcl:
        return gen_network_acl

    func()


def test_network_acl_return_fail(gen_route_table):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> NetworkAcl:
            return gen_route_table

        func()


# ============================
# NetworkInterface
# ============================


def test_network_interface_arg_pass(gen_network_interface):
    @beartype
    def func(param: NetworkInterface):
        pass

    func(gen_network_interface)


def test_network_interface_arg_fail(gen_key_pair):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: NetworkInterface):
            pass

        func(gen_key_pair)


def test_network_interface_return_pass(gen_network_interface):
    @beartype
    def func() -> NetworkInterface:
        return gen_network_interface

    func()


def test_network_interface_return_fail(gen_key_pair):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> NetworkInterface:
            return gen_key_pair

        func()


# ============================
# NetworkInterfaceAssociation
# ============================


def test_network_interface_association_arg_pass(gen_network_interface_association):
    @beartype
    def func(param: NetworkInterfaceAssociation):
        pass

    func(gen_network_interface_association)


def test_network_interface_association_arg_fail(gen_network_interface):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: NetworkInterfaceAssociation):
            pass

        func(gen_network_interface)


def test_network_interface_association_return_pass(gen_network_interface_association):
    @beartype
    def func() -> NetworkInterfaceAssociation:
        return gen_network_interface_association

    func()


def test_network_interface_association_return_fail(gen_network_interface):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> NetworkInterfaceAssociation:
            return gen_network_interface

        func()


# ============================
# PlacementGroup
# ============================


def test_placement_group_arg_pass(gen_placement_group):
    @beartype
    def func(param: PlacementGroup):
        pass

    func(gen_placement_group)


def test_placement_group_arg_fail(gen_vpc_address):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PlacementGroup):
            pass

        func(gen_vpc_address)


def test_placement_group_return_pass(gen_placement_group):
    @beartype
    def func() -> PlacementGroup:
        return gen_placement_group

    func()


def test_placement_group_return_fail(gen_vpc_address):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PlacementGroup:
            return gen_vpc_address

        func()


# ============================
# Route
# ============================


def test_route_arg_pass(gen_route):
    @beartype
    def func(param: Route):
        pass

    func(gen_route)


def test_route_arg_fail(gen_placement_group):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Route):
            pass

        func(gen_placement_group)


def test_route_return_pass(gen_route):
    @beartype
    def func() -> Route:
        return gen_route

    func()


def test_route_return_fail(gen_placement_group):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Route:
            return gen_placement_group

        func()


# ============================
# RouteTable
# ============================


def test_route_table_arg_pass(gen_route_table):
    @beartype
    def func(param: RouteTable):
        pass

    func(gen_route_table)


def test_route_table_arg_fail(gen_key_pair):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: RouteTable):
            pass

        func(gen_key_pair)


def test_route_table_return_pass(gen_route_table):
    @beartype
    def func() -> RouteTable:
        return gen_route_table

    func()


def test_route_table_return_fail(gen_key_pair):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> RouteTable:
            return gen_key_pair

        func()


# ============================
# RouteTableAssociation
# ============================


def test_route_table_association_arg_pass(gen_route_table_association):
    @beartype
    def func(param: RouteTableAssociation):
        pass

    func(gen_route_table_association)


def test_route_table_association_arg_fail(gen_image):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: RouteTableAssociation):
            pass

        func(gen_image)


def test_route_table_association_return_pass(gen_route_table_association):
    @beartype
    def func() -> RouteTableAssociation:
        return gen_route_table_association

    func()


def test_route_table_association_return_fail(gen_image):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> RouteTableAssociation:
            return gen_image

        func()


# ============================
# SecurityGroup
# ============================


def test_security_group_arg_pass(gen_security_group):
    @beartype
    def func(param: SecurityGroup):
        pass

    func(gen_security_group)


def test_security_group_arg_fail(gen_route):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SecurityGroup):
            pass

        func(gen_route)


def test_security_group_return_pass(gen_security_group):
    @beartype
    def func() -> SecurityGroup:
        return gen_security_group

    func()


def test_security_group_return_fail(gen_route):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SecurityGroup:
            return gen_route

        func()


# ============================
# Snapshot
# ============================


def test_snapshot_arg_pass(gen_snapshot):
    @beartype
    def func(param: Snapshot):
        pass

    func(gen_snapshot)


def test_snapshot_arg_fail(gen_classic_address):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Snapshot):
            pass

        func(gen_classic_address)


def test_snapshot_return_pass(gen_snapshot):
    @beartype
    def func() -> Snapshot:
        return gen_snapshot

    func()


def test_snapshot_return_fail(gen_classic_address):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Snapshot:
            return gen_classic_address

        func()


# ============================
# Subnet
# ============================


def test_subnet_arg_pass(gen_subnet):
    @beartype
    def func(param: Subnet):
        pass

    func(gen_subnet)


def test_subnet_arg_fail(gen_vpc):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Subnet):
            pass

        func(gen_vpc)


def test_subnet_return_pass(gen_subnet):
    @beartype
    def func() -> Subnet:
        return gen_subnet

    func()


def test_subnet_return_fail(gen_vpc):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Subnet:
            return gen_vpc

        func()


# ============================
# Tag
# ============================


def test_tag_arg_pass(gen_tag):
    @beartype
    def func(param: Tag):
        pass

    func(gen_tag)


def test_tag_arg_fail(gen_classic_address):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Tag):
            pass

        func(gen_classic_address)


def test_tag_return_pass(gen_tag):
    @beartype
    def func() -> Tag:
        return gen_tag

    func()


def test_tag_return_fail(gen_classic_address):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Tag:
            return gen_classic_address

        func()


# ============================
# Volume
# ============================


def test_volume_arg_pass(gen_volume):
    @beartype
    def func(param: Volume):
        pass

    func(gen_volume)


def test_volume_arg_fail(gen_classic_address):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Volume):
            pass

        func(gen_classic_address)


def test_volume_return_pass(gen_volume):
    @beartype
    def func() -> Volume:
        return gen_volume

    func()


def test_volume_return_fail(gen_classic_address):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Volume:
            return gen_classic_address

        func()


# ============================
# Vpc
# ============================


def test_vpc_arg_pass(gen_vpc):
    @beartype
    def func(param: Vpc):
        pass

    func(gen_vpc)


def test_vpc_arg_fail(gen_tag):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Vpc):
            pass

        func(gen_tag)


def test_vpc_return_pass(gen_vpc):
    @beartype
    def func() -> Vpc:
        return gen_vpc

    func()


def test_vpc_return_fail(gen_tag):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Vpc:
            return gen_tag

        func()


# ============================
# VpcPeeringConnection
# ============================


def test_vpc_peering_connection_arg_pass(gen_vpc_peering_connection):
    @beartype
    def func(param: VpcPeeringConnection):
        pass

    func(gen_vpc_peering_connection)


def test_vpc_peering_connection_arg_fail(gen_network_interface_association):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcPeeringConnection):
            pass

        func(gen_network_interface_association)


def test_vpc_peering_connection_return_pass(gen_vpc_peering_connection):
    @beartype
    def func() -> VpcPeeringConnection:
        return gen_vpc_peering_connection

    func()


def test_vpc_peering_connection_return_fail(gen_network_interface_association):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcPeeringConnection:
            return gen_network_interface_association

        func()


# ============================
# VpcAddress
# ============================


def test_vpc_address_arg_pass(gen_vpc_address):
    @beartype
    def func(param: VpcAddress):
        pass

    func(gen_vpc_address)


def test_vpc_address_arg_fail(gen_network_interface_association):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VpcAddress):
            pass

        func(gen_network_interface_association)


def test_vpc_address_return_pass(gen_vpc_address):
    @beartype
    def func() -> VpcAddress:
        return gen_vpc_address

    func()


def test_vpc_address_return_fail(gen_network_interface_association):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcAddress:
            return gen_network_interface_association

        func()
