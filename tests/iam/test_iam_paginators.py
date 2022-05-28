import pytest
from bearboto3.iam import (
    GetAccountAuthorizationDetailsPaginator,
    GetGroupPaginator,
    ListAccessKeysPaginator,
    ListAccountAliasesPaginator,
    ListAttachedGroupPoliciesPaginator,
    ListAttachedRolePoliciesPaginator,
    ListAttachedUserPoliciesPaginator,
    ListEntitiesForPolicyPaginator,
    ListGroupPoliciesPaginator,
    ListGroupsPaginator,
    ListGroupsForUserPaginator,
    ListInstanceProfilesPaginator,
    ListInstanceProfilesForRolePaginator,
    ListMFADevicesPaginator,
    ListPoliciesPaginator,
    ListPolicyVersionsPaginator,
    ListRolePoliciesPaginator,
    ListRolesPaginator,
    ListServerCertificatesPaginator,
    ListSigningCertificatesPaginator,
    ListSSHPublicKeysPaginator,
    ListUserPoliciesPaginator,
    ListUsersPaginator,
    ListVirtualMFADevicesPaginator,
    SimulateCustomPolicyPaginator,
    SimulatePrincipalPolicyPaginator,
    ListUserTagsPaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# GetAccountAuthorizationDetailsPaginator
# ============================


def test_get_account_authorization_details_arg_pass(
    gen_get_account_authorization_details_paginator,
):
    @beartype
    def func(param: GetAccountAuthorizationDetailsPaginator):
        pass

    func(gen_get_account_authorization_details_paginator)


def test_get_account_authorization_details_arg_fail(gen_list_group_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: GetAccountAuthorizationDetailsPaginator):
            pass

        func(gen_list_group_policies_paginator)


def test_get_account_authorization_details_return_pass(
    gen_get_account_authorization_details_paginator,
):
    @beartype
    def func() -> GetAccountAuthorizationDetailsPaginator:
        return gen_get_account_authorization_details_paginator

    func()


def test_get_account_authorization_details_return_fail(
    gen_list_group_policies_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetAccountAuthorizationDetailsPaginator:
            return gen_list_group_policies_paginator

        func()


# ============================
# GetGroupPaginator
# ============================


def test_get_group_arg_pass(gen_get_group_paginator):
    @beartype
    def func(param: GetGroupPaginator):
        pass

    func(gen_get_group_paginator)


def test_get_group_arg_fail(gen_list_roles_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: GetGroupPaginator):
            pass

        func(gen_list_roles_paginator)


def test_get_group_return_pass(gen_get_group_paginator):
    @beartype
    def func() -> GetGroupPaginator:
        return gen_get_group_paginator

    func()


def test_get_group_return_fail(gen_list_roles_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GetGroupPaginator:
            return gen_list_roles_paginator

        func()


# ============================
# ListAccessKeysPaginator
# ============================


def test_list_access_keys_arg_pass(gen_list_access_keys_paginator):
    @beartype
    def func(param: ListAccessKeysPaginator):
        pass

    func(gen_list_access_keys_paginator)


def test_list_access_keys_arg_fail(gen_list_user_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListAccessKeysPaginator):
            pass

        func(gen_list_user_policies_paginator)


def test_list_access_keys_return_pass(gen_list_access_keys_paginator):
    @beartype
    def func() -> ListAccessKeysPaginator:
        return gen_list_access_keys_paginator

    func()


def test_list_access_keys_return_fail(gen_list_user_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListAccessKeysPaginator:
            return gen_list_user_policies_paginator

        func()


# ============================
# ListAccountAliasesPaginator
# ============================


def test_list_account_aliases_arg_pass(gen_list_account_aliases_paginator):
    @beartype
    def func(param: ListAccountAliasesPaginator):
        pass

    func(gen_list_account_aliases_paginator)


def test_list_account_aliases_arg_fail(gen_list_ssh_public_keys_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListAccountAliasesPaginator):
            pass

        func(gen_list_ssh_public_keys_paginator)


def test_list_account_aliases_return_pass(gen_list_account_aliases_paginator):
    @beartype
    def func() -> ListAccountAliasesPaginator:
        return gen_list_account_aliases_paginator

    func()


def test_list_account_aliases_return_fail(gen_list_ssh_public_keys_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListAccountAliasesPaginator:
            return gen_list_ssh_public_keys_paginator

        func()


# ============================
# ListAttachedGroupPoliciesPaginator
# ============================


def test_list_attached_group_policies_arg_pass(
    gen_list_attached_group_policies_paginator,
):
    @beartype
    def func(param: ListAttachedGroupPoliciesPaginator):
        pass

    func(gen_list_attached_group_policies_paginator)


def test_list_attached_group_policies_arg_fail(gen_list_user_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListAttachedGroupPoliciesPaginator):
            pass

        func(gen_list_user_policies_paginator)


def test_list_attached_group_policies_return_pass(
    gen_list_attached_group_policies_paginator,
):
    @beartype
    def func() -> ListAttachedGroupPoliciesPaginator:
        return gen_list_attached_group_policies_paginator

    func()


def test_list_attached_group_policies_return_fail(gen_list_user_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListAttachedGroupPoliciesPaginator:
            return gen_list_user_policies_paginator

        func()


# ============================
# ListAttachedRolePoliciesPaginator
# ============================


def test_list_attached_role_policies_arg_pass(
    gen_list_attached_role_policies_paginator,
):
    @beartype
    def func(param: ListAttachedRolePoliciesPaginator):
        pass

    func(gen_list_attached_role_policies_paginator)


def test_list_attached_role_policies_arg_fail(gen_list_server_certificates_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListAttachedRolePoliciesPaginator):
            pass

        func(gen_list_server_certificates_paginator)


def test_list_attached_role_policies_return_pass(
    gen_list_attached_role_policies_paginator,
):
    @beartype
    def func() -> ListAttachedRolePoliciesPaginator:
        return gen_list_attached_role_policies_paginator

    func()


def test_list_attached_role_policies_return_fail(
    gen_list_server_certificates_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListAttachedRolePoliciesPaginator:
            return gen_list_server_certificates_paginator

        func()


# ============================
# ListAttachedUserPoliciesPaginator
# ============================


def test_list_attached_user_policies_arg_pass(
    gen_list_attached_user_policies_paginator,
):
    @beartype
    def func(param: ListAttachedUserPoliciesPaginator):
        pass

    func(gen_list_attached_user_policies_paginator)


def test_list_attached_user_policies_arg_fail(gen_list_roles_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListAttachedUserPoliciesPaginator):
            pass

        func(gen_list_roles_paginator)


def test_list_attached_user_policies_return_pass(
    gen_list_attached_user_policies_paginator,
):
    @beartype
    def func() -> ListAttachedUserPoliciesPaginator:
        return gen_list_attached_user_policies_paginator

    func()


def test_list_attached_user_policies_return_fail(gen_list_roles_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListAttachedUserPoliciesPaginator:
            return gen_list_roles_paginator

        func()


# ============================
# ListEntitiesForPolicyPaginator
# ============================


def test_list_entities_for_policy_arg_pass(gen_list_entities_for_policy_paginator):
    @beartype
    def func(param: ListEntitiesForPolicyPaginator):
        pass

    func(gen_list_entities_for_policy_paginator)


def test_list_entities_for_policy_arg_fail(gen_get_group_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListEntitiesForPolicyPaginator):
            pass

        func(gen_get_group_paginator)


def test_list_entities_for_policy_return_pass(gen_list_entities_for_policy_paginator):
    @beartype
    def func() -> ListEntitiesForPolicyPaginator:
        return gen_list_entities_for_policy_paginator

    func()


def test_list_entities_for_policy_return_fail(gen_get_group_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListEntitiesForPolicyPaginator:
            return gen_get_group_paginator

        func()


# ============================
# ListGroupPoliciesPaginator
# ============================


def test_list_group_policies_arg_pass(gen_list_group_policies_paginator):
    @beartype
    def func(param: ListGroupPoliciesPaginator):
        pass

    func(gen_list_group_policies_paginator)


def test_list_group_policies_arg_fail(gen_get_group_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListGroupPoliciesPaginator):
            pass

        func(gen_get_group_paginator)


def test_list_group_policies_return_pass(gen_list_group_policies_paginator):
    @beartype
    def func() -> ListGroupPoliciesPaginator:
        return gen_list_group_policies_paginator

    func()


def test_list_group_policies_return_fail(gen_get_group_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListGroupPoliciesPaginator:
            return gen_get_group_paginator

        func()


# ============================
# ListGroupsPaginator
# ============================


def test_list_groups_arg_pass(gen_list_groups_paginator):
    @beartype
    def func(param: ListGroupsPaginator):
        pass

    func(gen_list_groups_paginator)


def test_list_groups_arg_fail(gen_list_account_aliases_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListGroupsPaginator):
            pass

        func(gen_list_account_aliases_paginator)


def test_list_groups_return_pass(gen_list_groups_paginator):
    @beartype
    def func() -> ListGroupsPaginator:
        return gen_list_groups_paginator

    func()


def test_list_groups_return_fail(gen_list_account_aliases_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListGroupsPaginator:
            return gen_list_account_aliases_paginator

        func()


# ============================
# ListGroupsForUserPaginator
# ============================


def test_list_groups_for_user_arg_pass(gen_list_groups_for_user_paginator):
    @beartype
    def func(param: ListGroupsForUserPaginator):
        pass

    func(gen_list_groups_for_user_paginator)


def test_list_groups_for_user_arg_fail(gen_list_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListGroupsForUserPaginator):
            pass

        func(gen_list_policies_paginator)


def test_list_groups_for_user_return_pass(gen_list_groups_for_user_paginator):
    @beartype
    def func() -> ListGroupsForUserPaginator:
        return gen_list_groups_for_user_paginator

    func()


def test_list_groups_for_user_return_fail(gen_list_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListGroupsForUserPaginator:
            return gen_list_policies_paginator

        func()


# ============================
# ListInstanceProfilesPaginator
# ============================


def test_list_instance_profiles_arg_pass(gen_list_instance_profiles_paginator):
    @beartype
    def func(param: ListInstanceProfilesPaginator):
        pass

    func(gen_list_instance_profiles_paginator)


def test_list_instance_profiles_arg_fail(gen_list_groups_for_user_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListInstanceProfilesPaginator):
            pass

        func(gen_list_groups_for_user_paginator)


def test_list_instance_profiles_return_pass(gen_list_instance_profiles_paginator):
    @beartype
    def func() -> ListInstanceProfilesPaginator:
        return gen_list_instance_profiles_paginator

    func()


def test_list_instance_profiles_return_fail(gen_list_groups_for_user_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListInstanceProfilesPaginator:
            return gen_list_groups_for_user_paginator

        func()


# ============================
# ListInstanceProfilesForRolePaginator
# ============================


def test_list_instance_profiles_for_role_arg_pass(
    gen_list_instance_profiles_for_role_paginator,
):
    @beartype
    def func(param: ListInstanceProfilesForRolePaginator):
        pass

    func(gen_list_instance_profiles_for_role_paginator)


def test_list_instance_profiles_for_role_arg_fail(gen_list_group_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListInstanceProfilesForRolePaginator):
            pass

        func(gen_list_group_policies_paginator)


def test_list_instance_profiles_for_role_return_pass(
    gen_list_instance_profiles_for_role_paginator,
):
    @beartype
    def func() -> ListInstanceProfilesForRolePaginator:
        return gen_list_instance_profiles_for_role_paginator

    func()


def test_list_instance_profiles_for_role_return_fail(gen_list_group_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListInstanceProfilesForRolePaginator:
            return gen_list_group_policies_paginator

        func()


# ============================
# ListMFADevicesPaginator
# ============================


def test_list_mfa_devices_arg_pass(gen_list_mfa_devices_paginator):
    @beartype
    def func(param: ListMFADevicesPaginator):
        pass

    func(gen_list_mfa_devices_paginator)


def test_list_mfa_devices_arg_fail(gen_list_instance_profiles_for_role_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListMFADevicesPaginator):
            pass

        func(gen_list_instance_profiles_for_role_paginator)


def test_list_mfa_devices_return_pass(gen_list_mfa_devices_paginator):
    @beartype
    def func() -> ListMFADevicesPaginator:
        return gen_list_mfa_devices_paginator

    func()


def test_list_mfa_devices_return_fail(gen_list_instance_profiles_for_role_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListMFADevicesPaginator:
            return gen_list_instance_profiles_for_role_paginator

        func()


# ============================
# ListPoliciesPaginator
# ============================


def test_list_policies_arg_pass(gen_list_policies_paginator):
    @beartype
    def func(param: ListPoliciesPaginator):
        pass

    func(gen_list_policies_paginator)


def test_list_policies_arg_fail(gen_list_role_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListPoliciesPaginator):
            pass

        func(gen_list_role_policies_paginator)


def test_list_policies_return_pass(gen_list_policies_paginator):
    @beartype
    def func() -> ListPoliciesPaginator:
        return gen_list_policies_paginator

    func()


def test_list_policies_return_fail(gen_list_role_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListPoliciesPaginator:
            return gen_list_role_policies_paginator

        func()


# ============================
# ListPolicyVersionsPaginator
# ============================


def test_list_policy_versions_arg_pass(gen_list_policy_versions_paginator):
    @beartype
    def func(param: ListPolicyVersionsPaginator):
        pass

    func(gen_list_policy_versions_paginator)


def test_list_policy_versions_arg_fail(gen_list_account_aliases_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListPolicyVersionsPaginator):
            pass

        func(gen_list_account_aliases_paginator)


def test_list_policy_versions_return_pass(gen_list_policy_versions_paginator):
    @beartype
    def func() -> ListPolicyVersionsPaginator:
        return gen_list_policy_versions_paginator

    func()


def test_list_policy_versions_return_fail(gen_list_account_aliases_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListPolicyVersionsPaginator:
            return gen_list_account_aliases_paginator

        func()


# ============================
# ListRolePoliciesPaginator
# ============================


def test_list_role_policies_arg_pass(gen_list_role_policies_paginator):
    @beartype
    def func(param: ListRolePoliciesPaginator):
        pass

    func(gen_list_role_policies_paginator)


def test_list_role_policies_arg_fail(gen_list_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListRolePoliciesPaginator):
            pass

        func(gen_list_policies_paginator)


def test_list_role_policies_return_pass(gen_list_role_policies_paginator):
    @beartype
    def func() -> ListRolePoliciesPaginator:
        return gen_list_role_policies_paginator

    func()


def test_list_role_policies_return_fail(gen_list_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListRolePoliciesPaginator:
            return gen_list_policies_paginator

        func()


# ============================
# ListRolesPaginator
# ============================


def test_list_roles_arg_pass(gen_list_roles_paginator):
    @beartype
    def func(param: ListRolesPaginator):
        pass

    func(gen_list_roles_paginator)


def test_list_roles_arg_fail(gen_list_group_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListRolesPaginator):
            pass

        func(gen_list_group_policies_paginator)


def test_list_roles_return_pass(gen_list_roles_paginator):
    @beartype
    def func() -> ListRolesPaginator:
        return gen_list_roles_paginator

    func()


def test_list_roles_return_fail(gen_list_group_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListRolesPaginator:
            return gen_list_group_policies_paginator

        func()


# ============================
# ListServerCertificatesPaginator
# ============================


def test_list_server_certificates_arg_pass(gen_list_server_certificates_paginator):
    @beartype
    def func(param: ListServerCertificatesPaginator):
        pass

    func(gen_list_server_certificates_paginator)


def test_list_server_certificates_arg_fail(gen_list_user_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListServerCertificatesPaginator):
            pass

        func(gen_list_user_policies_paginator)


def test_list_server_certificates_return_pass(gen_list_server_certificates_paginator):
    @beartype
    def func() -> ListServerCertificatesPaginator:
        return gen_list_server_certificates_paginator

    func()


def test_list_server_certificates_return_fail(gen_list_user_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListServerCertificatesPaginator:
            return gen_list_user_policies_paginator

        func()


# ============================
# ListSigningCertificatesPaginator
# ============================


def test_list_signing_certificates_arg_pass(gen_list_signing_certificates_paginator):
    @beartype
    def func(param: ListSigningCertificatesPaginator):
        pass

    func(gen_list_signing_certificates_paginator)


def test_list_signing_certificates_arg_fail(gen_list_group_policies_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListSigningCertificatesPaginator):
            pass

        func(gen_list_group_policies_paginator)


def test_list_signing_certificates_return_pass(gen_list_signing_certificates_paginator):
    @beartype
    def func() -> ListSigningCertificatesPaginator:
        return gen_list_signing_certificates_paginator

    func()


def test_list_signing_certificates_return_fail(gen_list_group_policies_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListSigningCertificatesPaginator:
            return gen_list_group_policies_paginator

        func()


# ============================
# ListSSHPublicKeysPaginator
# ============================


def test_list_ssh_public_keys_arg_pass(gen_list_ssh_public_keys_paginator):
    @beartype
    def func(param: ListSSHPublicKeysPaginator):
        pass

    func(gen_list_ssh_public_keys_paginator)


def test_list_ssh_public_keys_arg_fail(gen_list_users_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListSSHPublicKeysPaginator):
            pass

        func(gen_list_users_paginator)


def test_list_ssh_public_keys_return_pass(gen_list_ssh_public_keys_paginator):
    @beartype
    def func() -> ListSSHPublicKeysPaginator:
        return gen_list_ssh_public_keys_paginator

    func()


def test_list_ssh_public_keys_return_fail(gen_list_users_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListSSHPublicKeysPaginator:
            return gen_list_users_paginator

        func()


# ============================
# ListUserPoliciesPaginator
# ============================


def test_list_user_policies_arg_pass(gen_list_user_policies_paginator):
    @beartype
    def func(param: ListUserPoliciesPaginator):
        pass

    func(gen_list_user_policies_paginator)


def test_list_user_policies_arg_fail(gen_list_groups_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListUserPoliciesPaginator):
            pass

        func(gen_list_groups_paginator)


def test_list_user_policies_return_pass(gen_list_user_policies_paginator):
    @beartype
    def func() -> ListUserPoliciesPaginator:
        return gen_list_user_policies_paginator

    func()


def test_list_user_policies_return_fail(gen_list_groups_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListUserPoliciesPaginator:
            return gen_list_groups_paginator

        func()


# ============================
# ListUsersPaginator
# ============================


def test_list_users_arg_pass(gen_list_users_paginator):
    @beartype
    def func(param: ListUsersPaginator):
        pass

    func(gen_list_users_paginator)


def test_list_users_arg_fail(gen_get_group_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListUsersPaginator):
            pass

        func(gen_get_group_paginator)


def test_list_users_return_pass(gen_list_users_paginator):
    @beartype
    def func() -> ListUsersPaginator:
        return gen_list_users_paginator

    func()


def test_list_users_return_fail(gen_get_group_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListUsersPaginator:
            return gen_get_group_paginator

        func()


# ============================
# ListVirtualMFADevicesPaginator
# ============================


def test_list_virtual_mfa_devices_arg_pass(gen_list_virtual_mfa_devices_paginator):
    @beartype
    def func(param: ListVirtualMFADevicesPaginator):
        pass

    func(gen_list_virtual_mfa_devices_paginator)


def test_list_virtual_mfa_devices_arg_fail(gen_list_policy_versions_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListVirtualMFADevicesPaginator):
            pass

        func(gen_list_policy_versions_paginator)


def test_list_virtual_mfa_devices_return_pass(gen_list_virtual_mfa_devices_paginator):
    @beartype
    def func() -> ListVirtualMFADevicesPaginator:
        return gen_list_virtual_mfa_devices_paginator

    func()


def test_list_virtual_mfa_devices_return_fail(gen_list_policy_versions_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListVirtualMFADevicesPaginator:
            return gen_list_policy_versions_paginator

        func()


# ============================
# SimulateCustomPolicyPaginator
# ============================


def test_simulate_custom_policy_arg_pass(gen_simulate_custom_policy_paginator):
    @beartype
    def func(param: SimulateCustomPolicyPaginator):
        pass

    func(gen_simulate_custom_policy_paginator)


def test_simulate_custom_policy_arg_fail(gen_list_instance_profiles_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: SimulateCustomPolicyPaginator):
            pass

        func(gen_list_instance_profiles_paginator)


def test_simulate_custom_policy_return_pass(gen_simulate_custom_policy_paginator):
    @beartype
    def func() -> SimulateCustomPolicyPaginator:
        return gen_simulate_custom_policy_paginator

    func()


def test_simulate_custom_policy_return_fail(gen_list_instance_profiles_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SimulateCustomPolicyPaginator:
            return gen_list_instance_profiles_paginator

        func()


# ============================
# SimulatePrincipalPolicyPaginator
# ============================


def test_simulate_principal_policy_arg_pass(gen_simulate_principal_policy_paginator):
    @beartype
    def func(param: SimulatePrincipalPolicyPaginator):
        pass

    func(gen_simulate_principal_policy_paginator)


def test_simulate_principal_policy_arg_fail(gen_list_policy_versions_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: SimulatePrincipalPolicyPaginator):
            pass

        func(gen_list_policy_versions_paginator)


def test_simulate_principal_policy_return_pass(gen_simulate_principal_policy_paginator):
    @beartype
    def func() -> SimulatePrincipalPolicyPaginator:
        return gen_simulate_principal_policy_paginator

    func()


def test_simulate_principal_policy_return_fail(gen_list_policy_versions_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SimulatePrincipalPolicyPaginator:
            return gen_list_policy_versions_paginator

        func()


# ============================
# ListUserTagsPaginator
# ============================


def test_list_user_tags_arg_pass(gen_list_user_tags_paginator):
    @beartype
    def func(param: ListUserTagsPaginator):
        pass

    func(gen_list_user_tags_paginator)


def test_list_user_tags_arg_fail(gen_get_account_authorization_details_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListUserTagsPaginator):
            pass

        func(gen_get_account_authorization_details_paginator)


def test_list_user_tags_return_pass(gen_list_user_tags_paginator):
    @beartype
    def func() -> ListUserTagsPaginator:
        return gen_list_user_tags_paginator

    func()


def test_list_user_tags_return_fail(gen_get_account_authorization_details_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListUserTagsPaginator:
            return gen_get_account_authorization_details_paginator

        func()
