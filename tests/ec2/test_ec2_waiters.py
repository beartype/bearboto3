import pytest
from bearboto3.ec2 import (
    InstanceExistsWaiter,
    BundleTaskCompleteWaiter,
    ConversionTaskCancelledWaiter,
    ConversionTaskCompletedWaiter,
    ConversionTaskDeletedWaiter,
    CustomerGatewayAvailableWaiter,
    ExportTaskCancelledWaiter,
    ExportTaskCompletedWaiter,
    ImageExistsWaiter,
    ImageAvailableWaiter,
    InstanceRunningWaiter,
    InstanceStatusOkWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
    KeyPairExistsWaiter,
    NatGatewayAvailableWaiter,
    NetworkInterfaceAvailableWaiter,
    PasswordDataAvailableWaiter,
    SnapshotCompletedWaiter,
    SecurityGroupExistsWaiter,
    SpotInstanceRequestFulfilledWaiter,
    SubnetAvailableWaiter,
    SystemStatusOkWaiter,
    VolumeAvailableWaiter,
    VolumeDeletedWaiter,
    VolumeInUseWaiter,
    VpcAvailableWaiter,
    VpcExistsWaiter,
    VpnConnectionAvailableWaiter,
    VpnConnectionDeletedWaiter,
    VpcPeeringConnectionExistsWaiter,
    VpcPeeringConnectionDeletedWaiter,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# InstanceExistsWaiter
# ============================


def test_instance_exists_arg_pass(gen_instance_exists_waiter):
    @beartype
    def func(param: InstanceExistsWaiter):
        pass

    func(gen_instance_exists_waiter)


def test_instance_exists_arg_fail(gen_conversion_task_completed_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: InstanceExistsWaiter):
            pass

        func(gen_conversion_task_completed_waiter)


def test_instance_exists_return_pass(gen_instance_exists_waiter):
    @beartype
    def func() -> InstanceExistsWaiter:
        return gen_instance_exists_waiter

    func()


def test_instance_exists_return_fail(gen_conversion_task_completed_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceExistsWaiter:
            return gen_conversion_task_completed_waiter

        func()


# ============================
# BundleTaskCompleteWaiter
# ============================


def test_bundle_task_complete_arg_pass(gen_bundle_task_complete_waiter):
    @beartype
    def func(param: BundleTaskCompleteWaiter):
        pass

    func(gen_bundle_task_complete_waiter)


def test_bundle_task_complete_arg_fail(gen_spot_instance_request_fulfilled_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: BundleTaskCompleteWaiter):
            pass

        func(gen_spot_instance_request_fulfilled_waiter)


def test_bundle_task_complete_return_pass(gen_bundle_task_complete_waiter):
    @beartype
    def func() -> BundleTaskCompleteWaiter:
        return gen_bundle_task_complete_waiter

    func()


def test_bundle_task_complete_return_fail(gen_spot_instance_request_fulfilled_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> BundleTaskCompleteWaiter:
            return gen_spot_instance_request_fulfilled_waiter

        func()


# ============================
# ConversionTaskCancelledWaiter
# ============================


def test_conversion_task_cancelled_arg_pass(gen_conversion_task_cancelled_waiter):
    @beartype
    def func(param: ConversionTaskCancelledWaiter):
        pass

    func(gen_conversion_task_cancelled_waiter)


def test_conversion_task_cancelled_arg_fail(gen_nat_gateway_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ConversionTaskCancelledWaiter):
            pass

        func(gen_nat_gateway_available_waiter)


def test_conversion_task_cancelled_return_pass(gen_conversion_task_cancelled_waiter):
    @beartype
    def func() -> ConversionTaskCancelledWaiter:
        return gen_conversion_task_cancelled_waiter

    func()


def test_conversion_task_cancelled_return_fail(gen_nat_gateway_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ConversionTaskCancelledWaiter:
            return gen_nat_gateway_available_waiter

        func()


# ============================
# ConversionTaskCompletedWaiter
# ============================


def test_conversion_task_completed_arg_pass(gen_conversion_task_completed_waiter):
    @beartype
    def func(param: ConversionTaskCompletedWaiter):
        pass

    func(gen_conversion_task_completed_waiter)


def test_conversion_task_completed_arg_fail(gen_image_exists_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ConversionTaskCompletedWaiter):
            pass

        func(gen_image_exists_waiter)


def test_conversion_task_completed_return_pass(gen_conversion_task_completed_waiter):
    @beartype
    def func() -> ConversionTaskCompletedWaiter:
        return gen_conversion_task_completed_waiter

    func()


def test_conversion_task_completed_return_fail(gen_image_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ConversionTaskCompletedWaiter:
            return gen_image_exists_waiter

        func()


# ============================
# ConversionTaskDeletedWaiter
# ============================


def test_conversion_task_deleted_arg_pass(gen_conversion_task_deleted_waiter):
    @beartype
    def func(param: ConversionTaskDeletedWaiter):
        pass

    func(gen_conversion_task_deleted_waiter)


def test_conversion_task_deleted_arg_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ConversionTaskDeletedWaiter):
            pass

        func(gen_bundle_task_complete_waiter)


def test_conversion_task_deleted_return_pass(gen_conversion_task_deleted_waiter):
    @beartype
    def func() -> ConversionTaskDeletedWaiter:
        return gen_conversion_task_deleted_waiter

    func()


def test_conversion_task_deleted_return_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ConversionTaskDeletedWaiter:
            return gen_bundle_task_complete_waiter

        func()


# ============================
# CustomerGatewayAvailableWaiter
# ============================


def test_customer_gateway_available_arg_pass(gen_customer_gateway_available_waiter):
    @beartype
    def func(param: CustomerGatewayAvailableWaiter):
        pass

    func(gen_customer_gateway_available_waiter)


def test_customer_gateway_available_arg_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: CustomerGatewayAvailableWaiter):
            pass

        func(gen_bundle_task_complete_waiter)


def test_customer_gateway_available_return_pass(gen_customer_gateway_available_waiter):
    @beartype
    def func() -> CustomerGatewayAvailableWaiter:
        return gen_customer_gateway_available_waiter

    func()


def test_customer_gateway_available_return_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> CustomerGatewayAvailableWaiter:
            return gen_bundle_task_complete_waiter

        func()


# ============================
# ExportTaskCancelledWaiter
# ============================


def test_export_task_cancelled_arg_pass(gen_export_task_cancelled_waiter):
    @beartype
    def func(param: ExportTaskCancelledWaiter):
        pass

    func(gen_export_task_cancelled_waiter)


def test_export_task_cancelled_arg_fail(gen_subnet_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ExportTaskCancelledWaiter):
            pass

        func(gen_subnet_available_waiter)


def test_export_task_cancelled_return_pass(gen_export_task_cancelled_waiter):
    @beartype
    def func() -> ExportTaskCancelledWaiter:
        return gen_export_task_cancelled_waiter

    func()


def test_export_task_cancelled_return_fail(gen_subnet_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ExportTaskCancelledWaiter:
            return gen_subnet_available_waiter

        func()


# ============================
# ExportTaskCompletedWaiter
# ============================


def test_export_task_completed_arg_pass(gen_export_task_completed_waiter):
    @beartype
    def func(param: ExportTaskCompletedWaiter):
        pass

    func(gen_export_task_completed_waiter)


def test_export_task_completed_arg_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ExportTaskCompletedWaiter):
            pass

        func(gen_vpc_peering_connection_deleted_waiter)


def test_export_task_completed_return_pass(gen_export_task_completed_waiter):
    @beartype
    def func() -> ExportTaskCompletedWaiter:
        return gen_export_task_completed_waiter

    func()


def test_export_task_completed_return_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ExportTaskCompletedWaiter:
            return gen_vpc_peering_connection_deleted_waiter

        func()


# ============================
# ImageExistsWaiter
# ============================


def test_image_exists_arg_pass(gen_image_exists_waiter):
    @beartype
    def func(param: ImageExistsWaiter):
        pass

    func(gen_image_exists_waiter)


def test_image_exists_arg_fail(gen_password_data_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ImageExistsWaiter):
            pass

        func(gen_password_data_available_waiter)


def test_image_exists_return_pass(gen_image_exists_waiter):
    @beartype
    def func() -> ImageExistsWaiter:
        return gen_image_exists_waiter

    func()


def test_image_exists_return_fail(gen_password_data_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ImageExistsWaiter:
            return gen_password_data_available_waiter

        func()


# ============================
# ImageAvailableWaiter
# ============================


def test_image_available_arg_pass(gen_image_available_waiter):
    @beartype
    def func(param: ImageAvailableWaiter):
        pass

    func(gen_image_available_waiter)


def test_image_available_arg_fail(gen_export_task_cancelled_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ImageAvailableWaiter):
            pass

        func(gen_export_task_cancelled_waiter)


def test_image_available_return_pass(gen_image_available_waiter):
    @beartype
    def func() -> ImageAvailableWaiter:
        return gen_image_available_waiter

    func()


def test_image_available_return_fail(gen_export_task_cancelled_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ImageAvailableWaiter:
            return gen_export_task_cancelled_waiter

        func()


# ============================
# InstanceRunningWaiter
# ============================


def test_instance_running_arg_pass(gen_instance_running_waiter):
    @beartype
    def func(param: InstanceRunningWaiter):
        pass

    func(gen_instance_running_waiter)


def test_instance_running_arg_fail(gen_volume_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: InstanceRunningWaiter):
            pass

        func(gen_volume_available_waiter)


def test_instance_running_return_pass(gen_instance_running_waiter):
    @beartype
    def func() -> InstanceRunningWaiter:
        return gen_instance_running_waiter

    func()


def test_instance_running_return_fail(gen_volume_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceRunningWaiter:
            return gen_volume_available_waiter

        func()


# ============================
# InstanceStatusOkWaiter
# ============================


def test_instance_status_ok_arg_pass(gen_instance_status_ok_waiter):
    @beartype
    def func(param: InstanceStatusOkWaiter):
        pass

    func(gen_instance_status_ok_waiter)


def test_instance_status_ok_arg_fail(gen_instance_stopped_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: InstanceStatusOkWaiter):
            pass

        func(gen_instance_stopped_waiter)


def test_instance_status_ok_return_pass(gen_instance_status_ok_waiter):
    @beartype
    def func() -> InstanceStatusOkWaiter:
        return gen_instance_status_ok_waiter

    func()


def test_instance_status_ok_return_fail(gen_instance_stopped_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceStatusOkWaiter:
            return gen_instance_stopped_waiter

        func()


# ============================
# InstanceStoppedWaiter
# ============================


def test_instance_stopped_arg_pass(gen_instance_stopped_waiter):
    @beartype
    def func(param: InstanceStoppedWaiter):
        pass

    func(gen_instance_stopped_waiter)


def test_instance_stopped_arg_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: InstanceStoppedWaiter):
            pass

        func(gen_bundle_task_complete_waiter)


def test_instance_stopped_return_pass(gen_instance_stopped_waiter):
    @beartype
    def func() -> InstanceStoppedWaiter:
        return gen_instance_stopped_waiter

    func()


def test_instance_stopped_return_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceStoppedWaiter:
            return gen_bundle_task_complete_waiter

        func()


# ============================
# InstanceTerminatedWaiter
# ============================


def test_instance_terminated_arg_pass(gen_instance_terminated_waiter):
    @beartype
    def func(param: InstanceTerminatedWaiter):
        pass

    func(gen_instance_terminated_waiter)


def test_instance_terminated_arg_fail(gen_network_interface_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: InstanceTerminatedWaiter):
            pass

        func(gen_network_interface_available_waiter)


def test_instance_terminated_return_pass(gen_instance_terminated_waiter):
    @beartype
    def func() -> InstanceTerminatedWaiter:
        return gen_instance_terminated_waiter

    func()


def test_instance_terminated_return_fail(gen_network_interface_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceTerminatedWaiter:
            return gen_network_interface_available_waiter

        func()


# ============================
# KeyPairExistsWaiter
# ============================


def test_key_pair_exists_arg_pass(gen_key_pair_exists_waiter):
    @beartype
    def func(param: KeyPairExistsWaiter):
        pass

    func(gen_key_pair_exists_waiter)


def test_key_pair_exists_arg_fail(gen_snapshot_completed_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: KeyPairExistsWaiter):
            pass

        func(gen_snapshot_completed_waiter)


def test_key_pair_exists_return_pass(gen_key_pair_exists_waiter):
    @beartype
    def func() -> KeyPairExistsWaiter:
        return gen_key_pair_exists_waiter

    func()


def test_key_pair_exists_return_fail(gen_snapshot_completed_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> KeyPairExistsWaiter:
            return gen_snapshot_completed_waiter

        func()


# ============================
# NatGatewayAvailableWaiter
# ============================


def test_nat_gateway_available_arg_pass(gen_nat_gateway_available_waiter):
    @beartype
    def func(param: NatGatewayAvailableWaiter):
        pass

    func(gen_nat_gateway_available_waiter)


def test_nat_gateway_available_arg_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: NatGatewayAvailableWaiter):
            pass

        func(gen_bundle_task_complete_waiter)


def test_nat_gateway_available_return_pass(gen_nat_gateway_available_waiter):
    @beartype
    def func() -> NatGatewayAvailableWaiter:
        return gen_nat_gateway_available_waiter

    func()


def test_nat_gateway_available_return_fail(gen_bundle_task_complete_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> NatGatewayAvailableWaiter:
            return gen_bundle_task_complete_waiter

        func()


# ============================
# NetworkInterfaceAvailableWaiter
# ============================


def test_network_interface_available_arg_pass(gen_network_interface_available_waiter):
    @beartype
    def func(param: NetworkInterfaceAvailableWaiter):
        pass

    func(gen_network_interface_available_waiter)


def test_network_interface_available_arg_fail(gen_volume_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: NetworkInterfaceAvailableWaiter):
            pass

        func(gen_volume_deleted_waiter)


def test_network_interface_available_return_pass(
    gen_network_interface_available_waiter,
):
    @beartype
    def func() -> NetworkInterfaceAvailableWaiter:
        return gen_network_interface_available_waiter

    func()


def test_network_interface_available_return_fail(gen_volume_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> NetworkInterfaceAvailableWaiter:
            return gen_volume_deleted_waiter

        func()


# ============================
# PasswordDataAvailableWaiter
# ============================


def test_password_data_available_arg_pass(gen_password_data_available_waiter):
    @beartype
    def func(param: PasswordDataAvailableWaiter):
        pass

    func(gen_password_data_available_waiter)


def test_password_data_available_arg_fail(gen_key_pair_exists_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: PasswordDataAvailableWaiter):
            pass

        func(gen_key_pair_exists_waiter)


def test_password_data_available_return_pass(gen_password_data_available_waiter):
    @beartype
    def func() -> PasswordDataAvailableWaiter:
        return gen_password_data_available_waiter

    func()


def test_password_data_available_return_fail(gen_key_pair_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PasswordDataAvailableWaiter:
            return gen_key_pair_exists_waiter

        func()


# ============================
# SnapshotCompletedWaiter
# ============================


def test_snapshot_completed_arg_pass(gen_snapshot_completed_waiter):
    @beartype
    def func(param: SnapshotCompletedWaiter):
        pass

    func(gen_snapshot_completed_waiter)


def test_snapshot_completed_arg_fail(gen_instance_running_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: SnapshotCompletedWaiter):
            pass

        func(gen_instance_running_waiter)


def test_snapshot_completed_return_pass(gen_snapshot_completed_waiter):
    @beartype
    def func() -> SnapshotCompletedWaiter:
        return gen_snapshot_completed_waiter

    func()


def test_snapshot_completed_return_fail(gen_instance_running_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SnapshotCompletedWaiter:
            return gen_instance_running_waiter

        func()


# ============================
# SecurityGroupExistsWaiter
# ============================


def test_security_group_exists_arg_pass(gen_security_group_exists_waiter):
    @beartype
    def func(param: SecurityGroupExistsWaiter):
        pass

    func(gen_security_group_exists_waiter)


def test_security_group_exists_arg_fail(gen_volume_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: SecurityGroupExistsWaiter):
            pass

        func(gen_volume_available_waiter)


def test_security_group_exists_return_pass(gen_security_group_exists_waiter):
    @beartype
    def func() -> SecurityGroupExistsWaiter:
        return gen_security_group_exists_waiter

    func()


def test_security_group_exists_return_fail(gen_volume_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SecurityGroupExistsWaiter:
            return gen_volume_available_waiter

        func()


# ============================
# SpotInstanceRequestFulfilledWaiter
# ============================


def test_spot_instance_request_fulfilled_arg_pass(
    gen_spot_instance_request_fulfilled_waiter,
):
    @beartype
    def func(param: SpotInstanceRequestFulfilledWaiter):
        pass

    func(gen_spot_instance_request_fulfilled_waiter)


def test_spot_instance_request_fulfilled_arg_fail(gen_instance_stopped_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: SpotInstanceRequestFulfilledWaiter):
            pass

        func(gen_instance_stopped_waiter)


def test_spot_instance_request_fulfilled_return_pass(
    gen_spot_instance_request_fulfilled_waiter,
):
    @beartype
    def func() -> SpotInstanceRequestFulfilledWaiter:
        return gen_spot_instance_request_fulfilled_waiter

    func()


def test_spot_instance_request_fulfilled_return_fail(gen_instance_stopped_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SpotInstanceRequestFulfilledWaiter:
            return gen_instance_stopped_waiter

        func()


# ============================
# SubnetAvailableWaiter
# ============================


def test_subnet_available_arg_pass(gen_subnet_available_waiter):
    @beartype
    def func(param: SubnetAvailableWaiter):
        pass

    func(gen_subnet_available_waiter)


def test_subnet_available_arg_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: SubnetAvailableWaiter):
            pass

        func(gen_vpc_peering_connection_deleted_waiter)


def test_subnet_available_return_pass(gen_subnet_available_waiter):
    @beartype
    def func() -> SubnetAvailableWaiter:
        return gen_subnet_available_waiter

    func()


def test_subnet_available_return_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SubnetAvailableWaiter:
            return gen_vpc_peering_connection_deleted_waiter

        func()


# ============================
# SystemStatusOkWaiter
# ============================


def test_system_status_ok_arg_pass(gen_system_status_ok_waiter):
    @beartype
    def func(param: SystemStatusOkWaiter):
        pass

    func(gen_system_status_ok_waiter)


def test_system_status_ok_arg_fail(gen_export_task_cancelled_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: SystemStatusOkWaiter):
            pass

        func(gen_export_task_cancelled_waiter)


def test_system_status_ok_return_pass(gen_system_status_ok_waiter):
    @beartype
    def func() -> SystemStatusOkWaiter:
        return gen_system_status_ok_waiter

    func()


def test_system_status_ok_return_fail(gen_export_task_cancelled_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SystemStatusOkWaiter:
            return gen_export_task_cancelled_waiter

        func()


# ============================
# VolumeAvailableWaiter
# ============================


def test_volume_available_arg_pass(gen_volume_available_waiter):
    @beartype
    def func(param: VolumeAvailableWaiter):
        pass

    func(gen_volume_available_waiter)


def test_volume_available_arg_fail(gen_vpn_connection_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VolumeAvailableWaiter):
            pass

        func(gen_vpn_connection_deleted_waiter)


def test_volume_available_return_pass(gen_volume_available_waiter):
    @beartype
    def func() -> VolumeAvailableWaiter:
        return gen_volume_available_waiter

    func()


def test_volume_available_return_fail(gen_vpn_connection_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VolumeAvailableWaiter:
            return gen_vpn_connection_deleted_waiter

        func()


# ============================
# VolumeDeletedWaiter
# ============================


def test_volume_deleted_arg_pass(gen_volume_deleted_waiter):
    @beartype
    def func(param: VolumeDeletedWaiter):
        pass

    func(gen_volume_deleted_waiter)


def test_volume_deleted_arg_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VolumeDeletedWaiter):
            pass

        func(gen_vpc_peering_connection_deleted_waiter)


def test_volume_deleted_return_pass(gen_volume_deleted_waiter):
    @beartype
    def func() -> VolumeDeletedWaiter:
        return gen_volume_deleted_waiter

    func()


def test_volume_deleted_return_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VolumeDeletedWaiter:
            return gen_vpc_peering_connection_deleted_waiter

        func()


# ============================
# VolumeInUseWaiter
# ============================


def test_volume_in_use_arg_pass(gen_volume_in_use_waiter):
    @beartype
    def func(param: VolumeInUseWaiter):
        pass

    func(gen_volume_in_use_waiter)


def test_volume_in_use_arg_fail(gen_conversion_task_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VolumeInUseWaiter):
            pass

        func(gen_conversion_task_deleted_waiter)


def test_volume_in_use_return_pass(gen_volume_in_use_waiter):
    @beartype
    def func() -> VolumeInUseWaiter:
        return gen_volume_in_use_waiter

    func()


def test_volume_in_use_return_fail(gen_conversion_task_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VolumeInUseWaiter:
            return gen_conversion_task_deleted_waiter

        func()


# ============================
# VpcAvailableWaiter
# ============================


def test_vpc_available_arg_pass(gen_vpc_available_waiter):
    @beartype
    def func(param: VpcAvailableWaiter):
        pass

    func(gen_vpc_available_waiter)


def test_vpc_available_arg_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VpcAvailableWaiter):
            pass

        func(gen_vpc_peering_connection_deleted_waiter)


def test_vpc_available_return_pass(gen_vpc_available_waiter):
    @beartype
    def func() -> VpcAvailableWaiter:
        return gen_vpc_available_waiter

    func()


def test_vpc_available_return_fail(gen_vpc_peering_connection_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcAvailableWaiter:
            return gen_vpc_peering_connection_deleted_waiter

        func()


# ============================
# VpcExistsWaiter
# ============================


def test_vpc_exists_arg_pass(gen_vpc_exists_waiter):
    @beartype
    def func(param: VpcExistsWaiter):
        pass

    func(gen_vpc_exists_waiter)


def test_vpc_exists_arg_fail(gen_instance_terminated_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VpcExistsWaiter):
            pass

        func(gen_instance_terminated_waiter)


def test_vpc_exists_return_pass(gen_vpc_exists_waiter):
    @beartype
    def func() -> VpcExistsWaiter:
        return gen_vpc_exists_waiter

    func()


def test_vpc_exists_return_fail(gen_instance_terminated_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcExistsWaiter:
            return gen_instance_terminated_waiter

        func()


# ============================
# VpnConnectionAvailableWaiter
# ============================


def test_vpn_connection_available_arg_pass(gen_vpn_connection_available_waiter):
    @beartype
    def func(param: VpnConnectionAvailableWaiter):
        pass

    func(gen_vpn_connection_available_waiter)


def test_vpn_connection_available_arg_fail(gen_customer_gateway_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VpnConnectionAvailableWaiter):
            pass

        func(gen_customer_gateway_available_waiter)


def test_vpn_connection_available_return_pass(gen_vpn_connection_available_waiter):
    @beartype
    def func() -> VpnConnectionAvailableWaiter:
        return gen_vpn_connection_available_waiter

    func()


def test_vpn_connection_available_return_fail(gen_customer_gateway_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpnConnectionAvailableWaiter:
            return gen_customer_gateway_available_waiter

        func()


# ============================
# VpnConnectionDeletedWaiter
# ============================


def test_vpn_connection_deleted_arg_pass(gen_vpn_connection_deleted_waiter):
    @beartype
    def func(param: VpnConnectionDeletedWaiter):
        pass

    func(gen_vpn_connection_deleted_waiter)


def test_vpn_connection_deleted_arg_fail(gen_volume_available_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VpnConnectionDeletedWaiter):
            pass

        func(gen_volume_available_waiter)


def test_vpn_connection_deleted_return_pass(gen_vpn_connection_deleted_waiter):
    @beartype
    def func() -> VpnConnectionDeletedWaiter:
        return gen_vpn_connection_deleted_waiter

    func()


def test_vpn_connection_deleted_return_fail(gen_volume_available_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpnConnectionDeletedWaiter:
            return gen_volume_available_waiter

        func()


# ============================
# VpcPeeringConnectionExistsWaiter
# ============================


def test_vpc_peering_connection_exists_arg_pass(
    gen_vpc_peering_connection_exists_waiter,
):
    @beartype
    def func(param: VpcPeeringConnectionExistsWaiter):
        pass

    func(gen_vpc_peering_connection_exists_waiter)


def test_vpc_peering_connection_exists_arg_fail(gen_instance_exists_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VpcPeeringConnectionExistsWaiter):
            pass

        func(gen_instance_exists_waiter)


def test_vpc_peering_connection_exists_return_pass(
    gen_vpc_peering_connection_exists_waiter,
):
    @beartype
    def func() -> VpcPeeringConnectionExistsWaiter:
        return gen_vpc_peering_connection_exists_waiter

    func()


def test_vpc_peering_connection_exists_return_fail(gen_instance_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcPeeringConnectionExistsWaiter:
            return gen_instance_exists_waiter

        func()


# ============================
# VpcPeeringConnectionDeletedWaiter
# ============================


def test_vpc_peering_connection_deleted_arg_pass(
    gen_vpc_peering_connection_deleted_waiter,
):
    @beartype
    def func(param: VpcPeeringConnectionDeletedWaiter):
        pass

    func(gen_vpc_peering_connection_deleted_waiter)


def test_vpc_peering_connection_deleted_arg_fail(gen_volume_deleted_waiter):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: VpcPeeringConnectionDeletedWaiter):
            pass

        func(gen_volume_deleted_waiter)


def test_vpc_peering_connection_deleted_return_pass(
    gen_vpc_peering_connection_deleted_waiter,
):
    @beartype
    def func() -> VpcPeeringConnectionDeletedWaiter:
        return gen_vpc_peering_connection_deleted_waiter

    func()


def test_vpc_peering_connection_deleted_return_fail(gen_volume_deleted_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VpcPeeringConnectionDeletedWaiter:
            return gen_volume_deleted_waiter

        func()
