import boto3
import pytest
from moto import mock_iam
from tests.utils import random_str


@pytest.fixture
def gen_iam_client(aws_setup):
    with mock_iam():
        yield boto3.client("iam")


@pytest.fixture
def gen_iam_resource(aws_setup):
    with mock_iam():
        yield boto3.resource("iam")


# ============================
# WAITER
# ============================


@pytest.fixture
def gen_instance_profile_exists_waiter(gen_iam_client):
    return gen_iam_client.get_waiter("instance_profile_exists")


@pytest.fixture
def gen_user_exists_waiter(gen_iam_client):
    return gen_iam_client.get_waiter("user_exists")


@pytest.fixture
def gen_role_exists_waiter(gen_iam_client):
    return gen_iam_client.get_waiter("role_exists")


@pytest.fixture
def gen_policy_exists_waiter(gen_iam_client):
    return gen_iam_client.get_waiter("policy_exists")


# ============================
# PAGINATOR
# ============================


@pytest.fixture
def gen_get_account_authorization_details_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("get_account_authorization_details")


@pytest.fixture
def gen_get_group_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("get_group")


@pytest.fixture
def gen_list_access_keys_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_access_keys")


@pytest.fixture
def gen_list_account_aliases_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_account_aliases")


@pytest.fixture
def gen_list_attached_group_policies_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_attached_group_policies")


@pytest.fixture
def gen_list_attached_role_policies_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_attached_role_policies")


@pytest.fixture
def gen_list_attached_user_policies_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_attached_user_policies")


@pytest.fixture
def gen_list_entities_for_policy_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_entities_for_policy")


@pytest.fixture
def gen_list_group_policies_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_group_policies")


@pytest.fixture
def gen_list_groups_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_groups")


@pytest.fixture
def gen_list_groups_for_user_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_groups_for_user")


@pytest.fixture
def gen_list_instance_profiles_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_instance_profiles")


@pytest.fixture
def gen_list_instance_profiles_for_role_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_instance_profiles_for_role")


@pytest.fixture
def gen_list_mfa_devices_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_mfa_devices")


@pytest.fixture
def gen_list_policies_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_policies")


@pytest.fixture
def gen_list_policy_versions_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_policy_versions")


@pytest.fixture
def gen_list_role_policies_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_role_policies")


@pytest.fixture
def gen_list_roles_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_roles")


@pytest.fixture
def gen_list_server_certificates_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_server_certificates")


@pytest.fixture
def gen_list_signing_certificates_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_signing_certificates")


@pytest.fixture
def gen_list_ssh_public_keys_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_ssh_public_keys")


@pytest.fixture
def gen_list_user_policies_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_user_policies")


@pytest.fixture
def gen_list_users_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_users")


@pytest.fixture
def gen_list_virtual_mfa_devices_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_virtual_mfa_devices")


@pytest.fixture
def gen_simulate_custom_policy_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("simulate_custom_policy")


@pytest.fixture
def gen_simulate_principal_policy_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("simulate_principal_policy")


@pytest.fixture
def gen_list_user_tags_paginator(gen_iam_client):
    return gen_iam_client.get_paginator("list_user_tags")


# ============================
# RESOURCES
# ============================


@pytest.fixture
def gen_access_key(gen_iam_resource):
    return gen_iam_resource.AccessKey(random_str(), random_str())


@pytest.fixture
def gen_access_key_pair(gen_iam_resource):
    return gen_iam_resource.AccessKeyPair(random_str(), random_str(), random_str())


@pytest.fixture
def gen_account_password_policy(gen_iam_resource):
    return gen_iam_resource.AccountPasswordPolicy()


@pytest.fixture
def gen_account_summary(gen_iam_resource):
    return gen_iam_resource.AccountSummary()


@pytest.fixture
def gen_assume_role_policy(gen_iam_resource):
    return gen_iam_resource.AssumeRolePolicy(random_str())


@pytest.fixture
def gen_current_user(gen_iam_resource):
    return gen_iam_resource.CurrentUser()


@pytest.fixture
def gen_group(gen_iam_resource):
    return gen_iam_resource.Group(random_str())


@pytest.fixture
def gen_group_policy(gen_iam_resource):
    return gen_iam_resource.GroupPolicy(random_str(), random_str())


@pytest.fixture
def gen_instance_profile(gen_iam_resource):
    return gen_iam_resource.InstanceProfile(random_str())


@pytest.fixture
def gen_login_profile(gen_iam_resource):
    return gen_iam_resource.LoginProfile(random_str())


@pytest.fixture
def gen_mfa_device(gen_iam_resource):
    return gen_iam_resource.MfaDevice(random_str(), random_str())


@pytest.fixture
def gen_policy(gen_iam_resource):
    return gen_iam_resource.Policy(random_str())


@pytest.fixture
def gen_policy_version(gen_iam_resource):
    return gen_iam_resource.PolicyVersion(random_str(), random_str())


@pytest.fixture
def gen_role(gen_iam_resource):
    return gen_iam_resource.Role(random_str())


@pytest.fixture
def gen_role_policy(gen_iam_resource):
    return gen_iam_resource.RolePolicy(random_str(), random_str())


@pytest.fixture
def gen_saml_provider(gen_iam_resource):
    return gen_iam_resource.SamlProvider(random_str())


@pytest.fixture
def gen_server_certificate(gen_iam_resource):
    return gen_iam_resource.ServerCertificate(random_str())


@pytest.fixture
def gen_signing_certificate(gen_iam_resource):
    return gen_iam_resource.SigningCertificate(random_str(), random_str())


@pytest.fixture
def gen_user(gen_iam_resource):
    return gen_iam_resource.User(random_str())


@pytest.fixture
def gen_user_policy(gen_iam_resource):
    return gen_iam_resource.UserPolicy(random_str(), random_str())


@pytest.fixture
def gen_virtual_mfa_device(gen_iam_resource):
    return gen_iam_resource.VirtualMfaDevice(random_str())


# ============================
# COLLECTIONS
# ============================


@pytest.fixture
def gen_service_resource_groups_collection(gen_iam_resource):
    return gen_iam_resource.groups.all()


@pytest.fixture
def gen_service_resource_instance_profiles_collection(gen_iam_resource):
    return gen_iam_resource.instance_profiles.all()


@pytest.fixture
def gen_service_resource_policies_collection(gen_iam_resource):
    return gen_iam_resource.policies.all()


@pytest.fixture
def gen_service_resource_roles_collection(gen_iam_resource):
    return gen_iam_resource.roles.all()


@pytest.fixture
def gen_service_resource_saml_providers_collection(gen_iam_resource):
    return gen_iam_resource.saml_providers.all()


@pytest.fixture
def gen_service_resource_server_certificates_collection(gen_iam_resource):
    return gen_iam_resource.server_certificates.all()


@pytest.fixture
def gen_service_resource_users_collection(gen_iam_resource):
    return gen_iam_resource.users.all()


@pytest.fixture
def gen_service_resource_virtual_mfa_devices_collection(gen_iam_resource):
    return gen_iam_resource.virtual_mfa_devices.all()


@pytest.fixture
def gen_current_user_access_keys_collection(gen_current_user):
    return gen_current_user.access_keys.all()


@pytest.fixture
def gen_current_user_mfa_devices_collection(gen_current_user):
    return gen_current_user.mfa_devices.all()


@pytest.fixture
def gen_current_user_signing_certificates_collection(gen_current_user):
    return gen_current_user.signing_certificates.all()


@pytest.fixture
def gen_group_attached_policies_collection(gen_group):
    return gen_group.attached_policies.all()


@pytest.fixture
def gen_group_policies_collection(gen_group):
    return gen_group.policies.all()


@pytest.fixture
def gen_group_users_collection(gen_group):
    return gen_group.users.all()


@pytest.fixture
def gen_policy_attached_groups_collection(gen_policy):
    return gen_policy.attached_groups.all()


@pytest.fixture
def gen_policy_attached_roles_collection(gen_policy):
    return gen_policy.attached_roles.all()


@pytest.fixture
def gen_policy_attached_users_collection(gen_policy):
    return gen_policy.attached_users.all()


@pytest.fixture
def gen_policy_versions_collection(gen_policy):
    return gen_policy.versions.all()


@pytest.fixture
def gen_role_attached_policies_collection(gen_role):
    return gen_role.attached_policies.all()


@pytest.fixture
def gen_role_instance_profiles_collection(gen_role):
    return gen_role.instance_profiles.all()


@pytest.fixture
def gen_role_policies_collection(gen_role):
    return gen_role.policies.all()


@pytest.fixture
def gen_user_access_keys_collection(gen_user):
    return gen_user.access_keys.all()


@pytest.fixture
def gen_user_attached_policies_collection(gen_user):
    return gen_user.attached_policies.all()


@pytest.fixture
def gen_user_groups_collection(gen_user):
    return gen_user.groups.all()


@pytest.fixture
def gen_user_mfa_devices_collection(gen_user):
    return gen_user.mfa_devices.all()


@pytest.fixture
def gen_user_policies_collection(gen_user):
    return gen_user.policies.all()


@pytest.fixture
def gen_user_signing_certificates_collection(gen_user):
    return gen_user.signing_certificates.all()
