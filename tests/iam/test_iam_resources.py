import pytest
from bearboto3.iam import (
    AccessKey,
    AccessKeyPair,
    AccountPasswordPolicy,
    AccountSummary,
    AssumeRolePolicy,
    CurrentUser,
    Group,
    GroupPolicy,
    InstanceProfile,
    LoginProfile,
    MfaDevice,
    Policy,
    PolicyVersion,
    Role,
    RolePolicy,
    SamlProvider,
    ServerCertificate,
    SigningCertificate,
    User,
    UserPolicy,
    VirtualMfaDevice,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# AccessKey
# ============================


def test_access_key_arg_pass(gen_access_key):
    @beartype
    def func(param: AccessKey):
        pass

    func(gen_access_key)


def test_access_key_arg_fail(gen_role):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: AccessKey):
            pass

        func(gen_role)


def test_access_key_return_pass(gen_access_key):
    @beartype
    def func() -> AccessKey:
        return gen_access_key

    func()


def test_access_key_return_fail(gen_role):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> AccessKey:
            return gen_role

        func()


# ============================
# AccessKeyPair
# ============================


def test_access_key_pair_arg_pass(gen_access_key_pair):
    @beartype
    def func(param: AccessKeyPair):
        pass

    func(gen_access_key_pair)


def test_access_key_pair_arg_fail(gen_policy_version):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: AccessKeyPair):
            pass

        func(gen_policy_version)


def test_access_key_pair_return_pass(gen_access_key_pair):
    @beartype
    def func() -> AccessKeyPair:
        return gen_access_key_pair

    func()


def test_access_key_pair_return_fail(gen_policy_version):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> AccessKeyPair:
            return gen_policy_version

        func()


# ============================
# AccountPasswordPolicy
# ============================


def test_account_password_policy_arg_pass(gen_account_password_policy):
    @beartype
    def func(param: AccountPasswordPolicy):
        pass

    func(gen_account_password_policy)


def test_account_password_policy_arg_fail(gen_mfa_device):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: AccountPasswordPolicy):
            pass

        func(gen_mfa_device)


def test_account_password_policy_return_pass(gen_account_password_policy):
    @beartype
    def func() -> AccountPasswordPolicy:
        return gen_account_password_policy

    func()


def test_account_password_policy_return_fail(gen_mfa_device):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> AccountPasswordPolicy:
            return gen_mfa_device

        func()


# ============================
# AccountSummary
# ============================


def test_account_summary_arg_pass(gen_account_summary):
    @beartype
    def func(param: AccountSummary):
        pass

    func(gen_account_summary)


def test_account_summary_arg_fail(gen_role):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: AccountSummary):
            pass

        func(gen_role)


def test_account_summary_return_pass(gen_account_summary):
    @beartype
    def func() -> AccountSummary:
        return gen_account_summary

    func()


def test_account_summary_return_fail(gen_role):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> AccountSummary:
            return gen_role

        func()


# ============================
# AssumeRolePolicy
# ============================


def test_assume_role_policy_arg_pass(gen_assume_role_policy):
    @beartype
    def func(param: AssumeRolePolicy):
        pass

    func(gen_assume_role_policy)


def test_assume_role_policy_arg_fail(gen_signing_certificate):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: AssumeRolePolicy):
            pass

        func(gen_signing_certificate)


def test_assume_role_policy_return_pass(gen_assume_role_policy):
    @beartype
    def func() -> AssumeRolePolicy:
        return gen_assume_role_policy

    func()


def test_assume_role_policy_return_fail(gen_signing_certificate):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> AssumeRolePolicy:
            return gen_signing_certificate

        func()


# ============================
# CurrentUser
# ============================


def test_current_user_arg_pass(gen_current_user):
    @beartype
    def func(param: CurrentUser):
        pass

    func(gen_current_user)


def test_current_user_arg_fail(gen_mfa_device):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: CurrentUser):
            pass

        func(gen_mfa_device)


def test_current_user_return_pass(gen_current_user):
    @beartype
    def func() -> CurrentUser:
        return gen_current_user

    func()


def test_current_user_return_fail(gen_mfa_device):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> CurrentUser:
            return gen_mfa_device

        func()


# ============================
# Group
# ============================


def test_group_arg_pass(gen_group):
    @beartype
    def func(param: Group):
        pass

    func(gen_group)


def test_group_arg_fail(gen_account_summary):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Group):
            pass

        func(gen_account_summary)


def test_group_return_pass(gen_group):
    @beartype
    def func() -> Group:
        return gen_group

    func()


def test_group_return_fail(gen_account_summary):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Group:
            return gen_account_summary

        func()


# ============================
# GroupPolicy
# ============================


def test_group_policy_arg_pass(gen_group_policy):
    @beartype
    def func(param: GroupPolicy):
        pass

    func(gen_group_policy)


def test_group_policy_arg_fail(gen_access_key_pair):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: GroupPolicy):
            pass

        func(gen_access_key_pair)


def test_group_policy_return_pass(gen_group_policy):
    @beartype
    def func() -> GroupPolicy:
        return gen_group_policy

    func()


def test_group_policy_return_fail(gen_access_key_pair):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> GroupPolicy:
            return gen_access_key_pair

        func()


# ============================
# InstanceProfile
# ============================


def test_instance_profile_arg_pass(gen_instance_profile):
    @beartype
    def func(param: InstanceProfile):
        pass

    func(gen_instance_profile)


def test_instance_profile_arg_fail(gen_current_user):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: InstanceProfile):
            pass

        func(gen_current_user)


def test_instance_profile_return_pass(gen_instance_profile):
    @beartype
    def func() -> InstanceProfile:
        return gen_instance_profile

    func()


def test_instance_profile_return_fail(gen_current_user):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceProfile:
            return gen_current_user

        func()


# ============================
# LoginProfile
# ============================


def test_login_profile_arg_pass(gen_login_profile):
    @beartype
    def func(param: LoginProfile):
        pass

    func(gen_login_profile)


def test_login_profile_arg_fail(gen_role_policy):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: LoginProfile):
            pass

        func(gen_role_policy)


def test_login_profile_return_pass(gen_login_profile):
    @beartype
    def func() -> LoginProfile:
        return gen_login_profile

    func()


def test_login_profile_return_fail(gen_role_policy):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> LoginProfile:
            return gen_role_policy

        func()


# ============================
# MfaDevice
# ============================


def test_mfa_device_arg_pass(gen_mfa_device):
    @beartype
    def func(param: MfaDevice):
        pass

    func(gen_mfa_device)


def test_mfa_device_arg_fail(gen_server_certificate):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: MfaDevice):
            pass

        func(gen_server_certificate)


def test_mfa_device_return_pass(gen_mfa_device):
    @beartype
    def func() -> MfaDevice:
        return gen_mfa_device

    func()


def test_mfa_device_return_fail(gen_server_certificate):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> MfaDevice:
            return gen_server_certificate

        func()


# ============================
# Policy
# ============================


def test_policy_arg_pass(gen_policy):
    @beartype
    def func(param: Policy):
        pass

    func(gen_policy)


def test_policy_arg_fail(gen_role):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Policy):
            pass

        func(gen_role)


def test_policy_return_pass(gen_policy):
    @beartype
    def func() -> Policy:
        return gen_policy

    func()


def test_policy_return_fail(gen_role):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Policy:
            return gen_role

        func()


# ============================
# PolicyVersion
# ============================


def test_policy_version_arg_pass(gen_policy_version):
    @beartype
    def func(param: PolicyVersion):
        pass

    func(gen_policy_version)


def test_policy_version_arg_fail(gen_group):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PolicyVersion):
            pass

        func(gen_group)


def test_policy_version_return_pass(gen_policy_version):
    @beartype
    def func() -> PolicyVersion:
        return gen_policy_version

    func()


def test_policy_version_return_fail(gen_group):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PolicyVersion:
            return gen_group

        func()


# ============================
# Role
# ============================


def test_role_arg_pass(gen_role):
    @beartype
    def func(param: Role):
        pass

    func(gen_role)


def test_role_arg_fail(gen_account_summary):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Role):
            pass

        func(gen_account_summary)


def test_role_return_pass(gen_role):
    @beartype
    def func() -> Role:
        return gen_role

    func()


def test_role_return_fail(gen_account_summary):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Role:
            return gen_account_summary

        func()


# ============================
# RolePolicy
# ============================


def test_role_policy_arg_pass(gen_role_policy):
    @beartype
    def func(param: RolePolicy):
        pass

    func(gen_role_policy)


def test_role_policy_arg_fail(gen_group):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: RolePolicy):
            pass

        func(gen_group)


def test_role_policy_return_pass(gen_role_policy):
    @beartype
    def func() -> RolePolicy:
        return gen_role_policy

    func()


def test_role_policy_return_fail(gen_group):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> RolePolicy:
            return gen_group

        func()


# ============================
# SamlProvider
# ============================


def test_saml_provider_arg_pass(gen_saml_provider):
    @beartype
    def func(param: SamlProvider):
        pass

    func(gen_saml_provider)


def test_saml_provider_arg_fail(gen_mfa_device):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SamlProvider):
            pass

        func(gen_mfa_device)


def test_saml_provider_return_pass(gen_saml_provider):
    @beartype
    def func() -> SamlProvider:
        return gen_saml_provider

    func()


def test_saml_provider_return_fail(gen_mfa_device):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SamlProvider:
            return gen_mfa_device

        func()


# ============================
# ServerCertificate
# ============================


def test_server_certificate_arg_pass(gen_server_certificate):
    @beartype
    def func(param: ServerCertificate):
        pass

    func(gen_server_certificate)


def test_server_certificate_arg_fail(gen_saml_provider):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ServerCertificate):
            pass

        func(gen_saml_provider)


def test_server_certificate_return_pass(gen_server_certificate):
    @beartype
    def func() -> ServerCertificate:
        return gen_server_certificate

    func()


def test_server_certificate_return_fail(gen_saml_provider):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServerCertificate:
            return gen_saml_provider

        func()


# ============================
# SigningCertificate
# ============================


def test_signing_certificate_arg_pass(gen_signing_certificate):
    @beartype
    def func(param: SigningCertificate):
        pass

    func(gen_signing_certificate)


def test_signing_certificate_arg_fail(gen_saml_provider):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: SigningCertificate):
            pass

        func(gen_saml_provider)


def test_signing_certificate_return_pass(gen_signing_certificate):
    @beartype
    def func() -> SigningCertificate:
        return gen_signing_certificate

    func()


def test_signing_certificate_return_fail(gen_saml_provider):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> SigningCertificate:
            return gen_saml_provider

        func()


# ============================
# User
# ============================


def test_user_arg_pass(gen_user):
    @beartype
    def func(param: User):
        pass

    func(gen_user)


def test_user_arg_fail(gen_role_policy):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: User):
            pass

        func(gen_role_policy)


def test_user_return_pass(gen_user):
    @beartype
    def func() -> User:
        return gen_user

    func()


def test_user_return_fail(gen_role_policy):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> User:
            return gen_role_policy

        func()


# ============================
# UserPolicy
# ============================


def test_user_policy_arg_pass(gen_user_policy):
    @beartype
    def func(param: UserPolicy):
        pass

    func(gen_user_policy)


def test_user_policy_arg_fail(gen_account_summary):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserPolicy):
            pass

        func(gen_account_summary)


def test_user_policy_return_pass(gen_user_policy):
    @beartype
    def func() -> UserPolicy:
        return gen_user_policy

    func()


def test_user_policy_return_fail(gen_account_summary):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserPolicy:
            return gen_account_summary

        func()


# ============================
# VirtualMfaDevice
# ============================


def test_virtual_mfa_device_arg_pass(gen_virtual_mfa_device):
    @beartype
    def func(param: VirtualMfaDevice):
        pass

    func(gen_virtual_mfa_device)


def test_virtual_mfa_device_arg_fail(gen_role):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: VirtualMfaDevice):
            pass

        func(gen_role)


def test_virtual_mfa_device_return_pass(gen_virtual_mfa_device):
    @beartype
    def func() -> VirtualMfaDevice:
        return gen_virtual_mfa_device

    func()


def test_virtual_mfa_device_return_fail(gen_role):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> VirtualMfaDevice:
            return gen_role

        func()
