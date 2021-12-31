import pytest
from bearboto3.iam import (
    ServiceResourceGroupsCollection,
    ServiceResourceInstanceProfilesCollection,
    ServiceResourcePoliciesCollection,
    ServiceResourceRolesCollection,
    ServiceResourceSamlProvidersCollection,
    ServiceResourceServerCertificatesCollection,
    ServiceResourceUsersCollection,
    ServiceResourceVirtualMfaDevicesCollection,
    CurrentUserAccessKeysCollection,
    CurrentUserMfaDevicesCollection,
    CurrentUserSigningCertificatesCollection,
    GroupAttachedPoliciesCollection,
    GroupPoliciesCollection,
    GroupUsersCollection,
    PolicyAttachedGroupsCollection,
    PolicyAttachedRolesCollection,
    PolicyAttachedUsersCollection,
    PolicyVersionsCollection,
    RoleAttachedPoliciesCollection,
    RoleInstanceProfilesCollection,
    RolePoliciesCollection,
    UserAccessKeysCollection,
    UserAttachedPoliciesCollection,
    UserGroupsCollection,
    UserMfaDevicesCollection,
    UserPoliciesCollection,
    UserSigningCertificatesCollection,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ServiceResourceGroupsCollection
# ============================


def test_groups_arg_pass(gen_service_resource_groups_collection):
    @beartype
    def func(param: ServiceResourceGroupsCollection):
        pass

    func(gen_service_resource_groups_collection)


def test_groups_arg_fail(gen_current_user_access_keys_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceGroupsCollection):
            pass

        func(gen_current_user_access_keys_collection)


def test_groups_return_pass(gen_service_resource_groups_collection):
    @beartype
    def func() -> ServiceResourceGroupsCollection:
        return gen_service_resource_groups_collection

    func()


def test_groups_return_fail(gen_current_user_access_keys_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceGroupsCollection:
            return gen_current_user_access_keys_collection

        func()


# ============================
# ServiceResourceInstanceProfilesCollection
# ============================


def test_instance_profiles_arg_pass(gen_service_resource_instance_profiles_collection):
    @beartype
    def func(param: ServiceResourceInstanceProfilesCollection):
        pass

    func(gen_service_resource_instance_profiles_collection)


def test_instance_profiles_arg_fail(gen_user_groups_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceInstanceProfilesCollection):
            pass

        func(gen_user_groups_collection)


def test_instance_profiles_return_pass(
    gen_service_resource_instance_profiles_collection,
):
    @beartype
    def func() -> ServiceResourceInstanceProfilesCollection:
        return gen_service_resource_instance_profiles_collection

    func()


def test_instance_profiles_return_fail(gen_user_groups_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceInstanceProfilesCollection:
            return gen_user_groups_collection

        func()


# ============================
# ServiceResourcePoliciesCollection
# ============================


def test_policies_arg_pass(gen_service_resource_policies_collection):
    @beartype
    def func(param: ServiceResourcePoliciesCollection):
        pass

    func(gen_service_resource_policies_collection)


def test_policies_arg_fail(gen_service_resource_roles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourcePoliciesCollection):
            pass

        func(gen_service_resource_roles_collection)


def test_policies_return_pass(gen_service_resource_policies_collection):
    @beartype
    def func() -> ServiceResourcePoliciesCollection:
        return gen_service_resource_policies_collection

    func()


def test_policies_return_fail(gen_service_resource_roles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourcePoliciesCollection:
            return gen_service_resource_roles_collection

        func()


# ============================
# ServiceResourceRolesCollection
# ============================


def test_roles_arg_pass(gen_service_resource_roles_collection):
    @beartype
    def func(param: ServiceResourceRolesCollection):
        pass

    func(gen_service_resource_roles_collection)


def test_roles_arg_fail(gen_group_attached_policies_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceRolesCollection):
            pass

        func(gen_group_attached_policies_collection)


def test_roles_return_pass(gen_service_resource_roles_collection):
    @beartype
    def func() -> ServiceResourceRolesCollection:
        return gen_service_resource_roles_collection

    func()


def test_roles_return_fail(gen_group_attached_policies_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceRolesCollection:
            return gen_group_attached_policies_collection

        func()


# ============================
# ServiceResourceSamlProvidersCollection
# ============================


def test_saml_providers_arg_pass(gen_service_resource_saml_providers_collection):
    @beartype
    def func(param: ServiceResourceSamlProvidersCollection):
        pass

    func(gen_service_resource_saml_providers_collection)


def test_saml_providers_arg_fail(gen_user_groups_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceSamlProvidersCollection):
            pass

        func(gen_user_groups_collection)


def test_saml_providers_return_pass(gen_service_resource_saml_providers_collection):
    @beartype
    def func() -> ServiceResourceSamlProvidersCollection:
        return gen_service_resource_saml_providers_collection

    func()


def test_saml_providers_return_fail(gen_user_groups_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceSamlProvidersCollection:
            return gen_user_groups_collection

        func()


# ============================
# ServiceResourceServerCertificatesCollection
# ============================


def test_server_certificates_arg_pass(
    gen_service_resource_server_certificates_collection,
):
    @beartype
    def func(param: ServiceResourceServerCertificatesCollection):
        pass

    func(gen_service_resource_server_certificates_collection)


def test_server_certificates_arg_fail(gen_service_resource_saml_providers_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceServerCertificatesCollection):
            pass

        func(gen_service_resource_saml_providers_collection)


def test_server_certificates_return_pass(
    gen_service_resource_server_certificates_collection,
):
    @beartype
    def func() -> ServiceResourceServerCertificatesCollection:
        return gen_service_resource_server_certificates_collection

    func()


def test_server_certificates_return_fail(
    gen_service_resource_saml_providers_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceServerCertificatesCollection:
            return gen_service_resource_saml_providers_collection

        func()


# ============================
# ServiceResourceUsersCollection
# ============================


def test_users_arg_pass(gen_service_resource_users_collection):
    @beartype
    def func(param: ServiceResourceUsersCollection):
        pass

    func(gen_service_resource_users_collection)


def test_users_arg_fail(gen_policy_attached_roles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceUsersCollection):
            pass

        func(gen_policy_attached_roles_collection)


def test_users_return_pass(gen_service_resource_users_collection):
    @beartype
    def func() -> ServiceResourceUsersCollection:
        return gen_service_resource_users_collection

    func()


def test_users_return_fail(gen_policy_attached_roles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceUsersCollection:
            return gen_policy_attached_roles_collection

        func()


# ============================
# ServiceResourceVirtualMfaDevicesCollection
# ============================


def test_virtual_mfa_devices_arg_pass(
    gen_service_resource_virtual_mfa_devices_collection,
):
    @beartype
    def func(param: ServiceResourceVirtualMfaDevicesCollection):
        pass

    func(gen_service_resource_virtual_mfa_devices_collection)


def test_virtual_mfa_devices_arg_fail(gen_service_resource_users_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServiceResourceVirtualMfaDevicesCollection):
            pass

        func(gen_service_resource_users_collection)


def test_virtual_mfa_devices_return_pass(
    gen_service_resource_virtual_mfa_devices_collection,
):
    @beartype
    def func() -> ServiceResourceVirtualMfaDevicesCollection:
        return gen_service_resource_virtual_mfa_devices_collection

    func()


def test_virtual_mfa_devices_return_fail(gen_service_resource_users_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceVirtualMfaDevicesCollection:
            return gen_service_resource_users_collection

        func()


# ============================
# CurrentUserAccessKeysCollection
# ============================


def test_access_keys_arg_pass(gen_current_user_access_keys_collection):
    @beartype
    def func(param: CurrentUserAccessKeysCollection):
        pass

    func(gen_current_user_access_keys_collection)


def test_access_keys_arg_fail(gen_user_groups_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: CurrentUserAccessKeysCollection):
            pass

        func(gen_user_groups_collection)


def test_access_keys_return_pass(gen_current_user_access_keys_collection):
    @beartype
    def func() -> CurrentUserAccessKeysCollection:
        return gen_current_user_access_keys_collection

    func()


def test_access_keys_return_fail(gen_user_groups_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> CurrentUserAccessKeysCollection:
            return gen_user_groups_collection

        func()


# ============================
# CurrentUserMfaDevicesCollection
# ============================


def test_mfa_devices_arg_pass(gen_current_user_mfa_devices_collection):
    @beartype
    def func(param: CurrentUserMfaDevicesCollection):
        pass

    func(gen_current_user_mfa_devices_collection)


def test_mfa_devices_arg_fail(gen_service_resource_groups_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: CurrentUserMfaDevicesCollection):
            pass

        func(gen_service_resource_groups_collection)


def test_mfa_devices_return_pass(gen_current_user_mfa_devices_collection):
    @beartype
    def func() -> CurrentUserMfaDevicesCollection:
        return gen_current_user_mfa_devices_collection

    func()


def test_mfa_devices_return_fail(gen_service_resource_groups_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> CurrentUserMfaDevicesCollection:
            return gen_service_resource_groups_collection

        func()


# ============================
# CurrentUserSigningCertificatesCollection
# ============================


def test_signing_certificates_arg_pass(
    gen_current_user_signing_certificates_collection,
):
    @beartype
    def func(param: CurrentUserSigningCertificatesCollection):
        pass

    func(gen_current_user_signing_certificates_collection)


def test_signing_certificates_arg_fail(
    gen_service_resource_server_certificates_collection,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: CurrentUserSigningCertificatesCollection):
            pass

        func(gen_service_resource_server_certificates_collection)


def test_signing_certificates_return_pass(
    gen_current_user_signing_certificates_collection,
):
    @beartype
    def func() -> CurrentUserSigningCertificatesCollection:
        return gen_current_user_signing_certificates_collection

    func()


def test_signing_certificates_return_fail(
    gen_service_resource_server_certificates_collection,
):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> CurrentUserSigningCertificatesCollection:
            return gen_service_resource_server_certificates_collection

        func()


# ============================
# GroupAttachedPoliciesCollection
# ============================


def test_attached_policies_arg_pass(gen_group_attached_policies_collection):
    @beartype
    def func(param: GroupAttachedPoliciesCollection):
        pass

    func(gen_group_attached_policies_collection)


def test_attached_policies_arg_fail(gen_policy_attached_roles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GroupAttachedPoliciesCollection):
            pass

        func(gen_policy_attached_roles_collection)


def test_attached_policies_return_pass(gen_group_attached_policies_collection):
    @beartype
    def func() -> GroupAttachedPoliciesCollection:
        return gen_group_attached_policies_collection

    func()


def test_attached_policies_return_fail(gen_policy_attached_roles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GroupAttachedPoliciesCollection:
            return gen_policy_attached_roles_collection

        func()


# ============================
# GroupPoliciesCollection
# ============================


def test_policies_arg_pass(gen_group_policies_collection):
    @beartype
    def func(param: GroupPoliciesCollection):
        pass

    func(gen_group_policies_collection)


def test_policies_arg_fail(gen_service_resource_roles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GroupPoliciesCollection):
            pass

        func(gen_service_resource_roles_collection)


def test_policies_return_pass(gen_group_policies_collection):
    @beartype
    def func() -> GroupPoliciesCollection:
        return gen_group_policies_collection

    func()


def test_policies_return_fail(gen_service_resource_roles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GroupPoliciesCollection:
            return gen_service_resource_roles_collection

        func()


# ============================
# GroupUsersCollection
# ============================


def test_users_arg_pass(gen_group_users_collection):
    @beartype
    def func(param: GroupUsersCollection):
        pass

    func(gen_group_users_collection)


def test_users_arg_fail(gen_role_instance_profiles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GroupUsersCollection):
            pass

        func(gen_role_instance_profiles_collection)


def test_users_return_pass(gen_group_users_collection):
    @beartype
    def func() -> GroupUsersCollection:
        return gen_group_users_collection

    func()


def test_users_return_fail(gen_role_instance_profiles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GroupUsersCollection:
            return gen_role_instance_profiles_collection

        func()


# ============================
# PolicyAttachedGroupsCollection
# ============================


def test_attached_groups_arg_pass(gen_policy_attached_groups_collection):
    @beartype
    def func(param: PolicyAttachedGroupsCollection):
        pass

    func(gen_policy_attached_groups_collection)


def test_attached_groups_arg_fail(gen_service_resource_users_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PolicyAttachedGroupsCollection):
            pass

        func(gen_service_resource_users_collection)


def test_attached_groups_return_pass(gen_policy_attached_groups_collection):
    @beartype
    def func() -> PolicyAttachedGroupsCollection:
        return gen_policy_attached_groups_collection

    func()


def test_attached_groups_return_fail(gen_service_resource_users_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PolicyAttachedGroupsCollection:
            return gen_service_resource_users_collection

        func()


# ============================
# PolicyAttachedRolesCollection
# ============================


def test_attached_roles_arg_pass(gen_policy_attached_roles_collection):
    @beartype
    def func(param: PolicyAttachedRolesCollection):
        pass

    func(gen_policy_attached_roles_collection)


def test_attached_roles_arg_fail(gen_user_access_keys_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PolicyAttachedRolesCollection):
            pass

        func(gen_user_access_keys_collection)


def test_attached_roles_return_pass(gen_policy_attached_roles_collection):
    @beartype
    def func() -> PolicyAttachedRolesCollection:
        return gen_policy_attached_roles_collection

    func()


def test_attached_roles_return_fail(gen_user_access_keys_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PolicyAttachedRolesCollection:
            return gen_user_access_keys_collection

        func()


# ============================
# PolicyAttachedUsersCollection
# ============================


def test_attached_users_arg_pass(gen_policy_attached_users_collection):
    @beartype
    def func(param: PolicyAttachedUsersCollection):
        pass

    func(gen_policy_attached_users_collection)


def test_attached_users_arg_fail(gen_service_resource_roles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PolicyAttachedUsersCollection):
            pass

        func(gen_service_resource_roles_collection)


def test_attached_users_return_pass(gen_policy_attached_users_collection):
    @beartype
    def func() -> PolicyAttachedUsersCollection:
        return gen_policy_attached_users_collection

    func()


def test_attached_users_return_fail(gen_service_resource_roles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PolicyAttachedUsersCollection:
            return gen_service_resource_roles_collection

        func()


# ============================
# PolicyVersionsCollection
# ============================


def test_versions_arg_pass(gen_policy_versions_collection):
    @beartype
    def func(param: PolicyVersionsCollection):
        pass

    func(gen_policy_versions_collection)


def test_versions_arg_fail(gen_service_resource_users_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PolicyVersionsCollection):
            pass

        func(gen_service_resource_users_collection)


def test_versions_return_pass(gen_policy_versions_collection):
    @beartype
    def func() -> PolicyVersionsCollection:
        return gen_policy_versions_collection

    func()


def test_versions_return_fail(gen_service_resource_users_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PolicyVersionsCollection:
            return gen_service_resource_users_collection

        func()


# ============================
# RoleAttachedPoliciesCollection
# ============================


def test_attached_policies_arg_pass(gen_role_attached_policies_collection):
    @beartype
    def func(param: RoleAttachedPoliciesCollection):
        pass

    func(gen_role_attached_policies_collection)


def test_attached_policies_arg_fail(gen_service_resource_roles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: RoleAttachedPoliciesCollection):
            pass

        func(gen_service_resource_roles_collection)


def test_attached_policies_return_pass(gen_role_attached_policies_collection):
    @beartype
    def func() -> RoleAttachedPoliciesCollection:
        return gen_role_attached_policies_collection

    func()


def test_attached_policies_return_fail(gen_service_resource_roles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> RoleAttachedPoliciesCollection:
            return gen_service_resource_roles_collection

        func()


# ============================
# RoleInstanceProfilesCollection
# ============================


def test_instance_profiles_arg_pass(gen_role_instance_profiles_collection):
    @beartype
    def func(param: RoleInstanceProfilesCollection):
        pass

    func(gen_role_instance_profiles_collection)


def test_instance_profiles_arg_fail(gen_user_access_keys_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: RoleInstanceProfilesCollection):
            pass

        func(gen_user_access_keys_collection)


def test_instance_profiles_return_pass(gen_role_instance_profiles_collection):
    @beartype
    def func() -> RoleInstanceProfilesCollection:
        return gen_role_instance_profiles_collection

    func()


def test_instance_profiles_return_fail(gen_user_access_keys_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> RoleInstanceProfilesCollection:
            return gen_user_access_keys_collection

        func()


# ============================
# RolePoliciesCollection
# ============================


def test_policies_arg_pass(gen_role_policies_collection):
    @beartype
    def func(param: RolePoliciesCollection):
        pass

    func(gen_role_policies_collection)


def test_policies_arg_fail(gen_user_groups_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: RolePoliciesCollection):
            pass

        func(gen_user_groups_collection)


def test_policies_return_pass(gen_role_policies_collection):
    @beartype
    def func() -> RolePoliciesCollection:
        return gen_role_policies_collection

    func()


def test_policies_return_fail(gen_user_groups_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> RolePoliciesCollection:
            return gen_user_groups_collection

        func()


# ============================
# UserAccessKeysCollection
# ============================


def test_access_keys_arg_pass(gen_user_access_keys_collection):
    @beartype
    def func(param: UserAccessKeysCollection):
        pass

    func(gen_user_access_keys_collection)


def test_access_keys_arg_fail(gen_user_signing_certificates_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserAccessKeysCollection):
            pass

        func(gen_user_signing_certificates_collection)


def test_access_keys_return_pass(gen_user_access_keys_collection):
    @beartype
    def func() -> UserAccessKeysCollection:
        return gen_user_access_keys_collection

    func()


def test_access_keys_return_fail(gen_user_signing_certificates_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserAccessKeysCollection:
            return gen_user_signing_certificates_collection

        func()


# ============================
# UserAttachedPoliciesCollection
# ============================


def test_attached_policies_arg_pass(gen_user_attached_policies_collection):
    @beartype
    def func(param: UserAttachedPoliciesCollection):
        pass

    func(gen_user_attached_policies_collection)


def test_attached_policies_arg_fail(gen_policy_attached_roles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserAttachedPoliciesCollection):
            pass

        func(gen_policy_attached_roles_collection)


def test_attached_policies_return_pass(gen_user_attached_policies_collection):
    @beartype
    def func() -> UserAttachedPoliciesCollection:
        return gen_user_attached_policies_collection

    func()


def test_attached_policies_return_fail(gen_policy_attached_roles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserAttachedPoliciesCollection:
            return gen_policy_attached_roles_collection

        func()


# ============================
# UserGroupsCollection
# ============================


def test_groups_arg_pass(gen_user_groups_collection):
    @beartype
    def func(param: UserGroupsCollection):
        pass

    func(gen_user_groups_collection)


def test_groups_arg_fail(gen_role_instance_profiles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserGroupsCollection):
            pass

        func(gen_role_instance_profiles_collection)


def test_groups_return_pass(gen_user_groups_collection):
    @beartype
    def func() -> UserGroupsCollection:
        return gen_user_groups_collection

    func()


def test_groups_return_fail(gen_role_instance_profiles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserGroupsCollection:
            return gen_role_instance_profiles_collection

        func()


# ============================
# UserMfaDevicesCollection
# ============================


def test_mfa_devices_arg_pass(gen_user_mfa_devices_collection):
    @beartype
    def func(param: UserMfaDevicesCollection):
        pass

    func(gen_user_mfa_devices_collection)


def test_mfa_devices_arg_fail(gen_service_resource_instance_profiles_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserMfaDevicesCollection):
            pass

        func(gen_service_resource_instance_profiles_collection)


def test_mfa_devices_return_pass(gen_user_mfa_devices_collection):
    @beartype
    def func() -> UserMfaDevicesCollection:
        return gen_user_mfa_devices_collection

    func()


def test_mfa_devices_return_fail(gen_service_resource_instance_profiles_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserMfaDevicesCollection:
            return gen_service_resource_instance_profiles_collection

        func()


# ============================
# UserPoliciesCollection
# ============================


def test_policies_arg_pass(gen_user_policies_collection):
    @beartype
    def func(param: UserPoliciesCollection):
        pass

    func(gen_user_policies_collection)


def test_policies_arg_fail(gen_policy_attached_groups_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserPoliciesCollection):
            pass

        func(gen_policy_attached_groups_collection)


def test_policies_return_pass(gen_user_policies_collection):
    @beartype
    def func() -> UserPoliciesCollection:
        return gen_user_policies_collection

    func()


def test_policies_return_fail(gen_policy_attached_groups_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserPoliciesCollection:
            return gen_policy_attached_groups_collection

        func()


# ============================
# UserSigningCertificatesCollection
# ============================


def test_signing_certificates_arg_pass(gen_user_signing_certificates_collection):
    @beartype
    def func(param: UserSigningCertificatesCollection):
        pass

    func(gen_user_signing_certificates_collection)


def test_signing_certificates_arg_fail(gen_user_access_keys_collection):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserSigningCertificatesCollection):
            pass

        func(gen_user_access_keys_collection)


def test_signing_certificates_return_pass(gen_user_signing_certificates_collection):
    @beartype
    def func() -> UserSigningCertificatesCollection:
        return gen_user_signing_certificates_collection

    func()


def test_signing_certificates_return_fail(gen_user_access_keys_collection):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserSigningCertificatesCollection:
            return gen_user_access_keys_collection

        func()
