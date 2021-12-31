from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_iam import (
        GetAccountAuthorizationDetailsPaginator,
        GetGroupPaginator,
        IAMClient,
        InstanceProfileExistsWaiter,
        ListAccessKeysPaginator,
        ListAccountAliasesPaginator,
        ListAttachedGroupPoliciesPaginator,
        ListAttachedRolePoliciesPaginator,
        ListAttachedUserPoliciesPaginator,
        ListEntitiesForPolicyPaginator,
        ListGroupPoliciesPaginator,
        ListGroupsForUserPaginator,
        ListGroupsPaginator,
        ListInstanceProfilesForRolePaginator,
        ListInstanceProfilesPaginator,
        ListMFADevicesPaginator,
        ListPoliciesPaginator,
        ListPolicyVersionsPaginator,
        ListRolePoliciesPaginator,
        ListRolesPaginator,
        ListSSHPublicKeysPaginator,
        ListServerCertificatesPaginator,
        ListSigningCertificatesPaginator,
        ListUserPoliciesPaginator,
        ListUserTagsPaginator,
        ListUsersPaginator,
        ListVirtualMFADevicesPaginator,
        PolicyExistsWaiter,
        RoleExistsWaiter,
        SimulateCustomPolicyPaginator,
        SimulatePrincipalPolicyPaginator,
        UserExistsWaiter,
    )
    from mypy_boto3_iam.service_resource import (
        AccessKey,
        AccessKeyPair,
        AccountPasswordPolicy,
        AccountSummary,
        AssumeRolePolicy,
        CurrentUser,
        CurrentUserAccessKeysCollection,
        CurrentUserMfaDevicesCollection,
        CurrentUserSigningCertificatesCollection,
        Group,
        GroupAttachedPoliciesCollection,
        GroupPoliciesCollection,
        GroupPolicy,
        GroupUsersCollection,
        IAMServiceResource,
        InstanceProfile,
        LoginProfile,
        MfaDevice,
        Policy,
        PolicyAttachedGroupsCollection,
        PolicyAttachedRolesCollection,
        PolicyAttachedUsersCollection,
        PolicyVersion,
        PolicyVersionsCollection,
        Role,
        RoleAttachedPoliciesCollection,
        RoleInstanceProfilesCollection,
        RolePoliciesCollection,
        RolePolicy,
        SamlProvider,
        ServerCertificate,
        ServiceResourceGroupsCollection,
        ServiceResourceInstanceProfilesCollection,
        ServiceResourcePoliciesCollection,
        ServiceResourceRolesCollection,
        ServiceResourceSamlProvidersCollection,
        ServiceResourceServerCertificatesCollection,
        ServiceResourceUsersCollection,
        ServiceResourceVirtualMfaDevicesCollection,
        SigningCertificate,
        User,
        UserAccessKeysCollection,
        UserAttachedPoliciesCollection,
        UserGroupsCollection,
        UserMfaDevicesCollection,
        UserPoliciesCollection,
        UserPolicy,
        UserSigningCertificatesCollection,
        VirtualMfaDevice,
    )
else:
    from beartype.vale import IsAttr, IsEqual
    from boto3.resources.base import ServiceResource
    from boto3.resources.collection import ResourceCollection
    from botocore.client import BaseClient
    from botocore.paginate import Paginator
    from botocore.waiter import Waiter

    from bearboto3 import Annotated

    AccessKey = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.AccessKey"]]],
    ]

    AccessKeyPair = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.AccessKeyPair"]]],
    ]

    AccountPasswordPolicy = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.AccountPasswordPolicy"]]],
    ]

    AccountSummary = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.AccountSummary"]]],
    ]

    AssumeRolePolicy = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.AssumeRolePolicy"]]],
    ]

    CurrentUser = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.CurrentUser"]]],
    ]

    CurrentUserAccessKeysCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.CurrentUser.access_keysCollection"]],
        ],
    ]

    CurrentUserMfaDevicesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.CurrentUser.mfa_devicesCollection"]],
        ],
    ]

    CurrentUserSigningCertificatesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr[
                "__name__", IsEqual["iam.CurrentUser.signing_certificatesCollection"]
            ],
        ],
    ]

    GetAccountAuthorizationDetailsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.GetAccountAuthorizationDetails"]],
        ],
    ]

    GetGroupPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Paginator.GetGroup"]]],
    ]

    Group = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["iam.Group"]]]
    ]

    GroupAttachedPoliciesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.Group.attached_policiesCollection"]],
        ],
    ]

    GroupPoliciesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["iam.Group.policiesCollection"]]
        ],
    ]

    GroupPolicy = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.GroupPolicy"]]],
    ]

    GroupUsersCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.Group.usersCollection"]]],
    ]

    IAMClient = Annotated[
        BaseClient, IsAttr["__class__", IsAttr["__name__", IsEqual["IAM"]]]
    ]

    IAMServiceResource = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.ServiceResource"]]],
    ]

    InstanceProfile = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.InstanceProfile"]]],
    ]

    InstanceProfileExistsWaiter = Annotated[
        Waiter,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Waiter.InstanceProfileExists"]]
        ],
    ]

    ListAccessKeysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListAccessKeys"]]
        ],
    ]

    ListAccountAliasesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListAccountAliases"]]
        ],
    ]

    ListAttachedGroupPoliciesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListAttachedGroupPolicies"]],
        ],
    ]

    ListAttachedRolePoliciesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListAttachedRolePolicies"]],
        ],
    ]

    ListAttachedUserPoliciesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListAttachedUserPolicies"]],
        ],
    ]

    ListEntitiesForPolicyPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListEntitiesForPolicy"]],
        ],
    ]

    ListGroupPoliciesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListGroupPolicies"]]
        ],
    ]

    ListGroupsForUserPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListGroupsForUser"]]
        ],
    ]

    ListGroupsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListGroups"]]],
    ]

    ListInstanceProfilesForRolePaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListInstanceProfilesForRole"]],
        ],
    ]

    ListInstanceProfilesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListInstanceProfiles"]],
        ],
    ]

    ListMFADevicesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListMFADevices"]]
        ],
    ]

    ListPoliciesPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListPolicies"]]],
    ]

    ListPolicyVersionsPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListPolicyVersions"]]
        ],
    ]

    ListRolePoliciesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListRolePolicies"]]
        ],
    ]

    ListRolesPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListRoles"]]],
    ]

    ListSSHPublicKeysPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListSSHPublicKeys"]]
        ],
    ]

    ListServerCertificatesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListServerCertificates"]],
        ],
    ]

    ListSigningCertificatesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListSigningCertificates"]],
        ],
    ]

    ListUserPoliciesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListUserPolicies"]]
        ],
    ]

    ListUserTagsPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListUserTags"]]],
    ]

    ListUsersPaginator = Annotated[
        Paginator,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Paginator.ListUsers"]]],
    ]

    ListVirtualMFADevicesPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.ListVirtualMFADevices"]],
        ],
    ]

    LoginProfile = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.LoginProfile"]]],
    ]

    MfaDevice = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.MfaDevice"]]],
    ]

    Policy = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["iam.Policy"]]]
    ]

    PolicyAttachedGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.Policy.attached_groupsCollection"]],
        ],
    ]

    PolicyAttachedRolesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.Policy.attached_rolesCollection"]],
        ],
    ]

    PolicyAttachedUsersCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.Policy.attached_usersCollection"]],
        ],
    ]

    PolicyExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Waiter.PolicyExists"]]],
    ]

    PolicyVersion = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.PolicyVersion"]]],
    ]

    PolicyVersionsCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["iam.Policy.versionsCollection"]]
        ],
    ]

    Role = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["iam.Role"]]]
    ]

    RoleAttachedPoliciesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.Role.attached_policiesCollection"]],
        ],
    ]

    RoleExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Waiter.RoleExists"]]],
    ]

    RoleInstanceProfilesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.Role.instance_profilesCollection"]],
        ],
    ]

    RolePoliciesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.Role.policiesCollection"]]],
    ]

    RolePolicy = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.RolePolicy"]]],
    ]

    SamlProvider = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.SamlProvider"]]],
    ]

    ServerCertificate = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.ServerCertificate"]]],
    ]

    ServiceResourceGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.groupsCollection"]]],
    ]

    ServiceResourceInstanceProfilesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["iam.instance_profilesCollection"]]
        ],
    ]

    ServiceResourcePoliciesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.policiesCollection"]]],
    ]

    ServiceResourceRolesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.rolesCollection"]]],
    ]

    ServiceResourceSamlProvidersCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["iam.saml_providersCollection"]]
        ],
    ]

    ServiceResourceServerCertificatesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.server_certificatesCollection"]],
        ],
    ]

    ServiceResourceUsersCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.usersCollection"]]],
    ]

    ServiceResourceVirtualMfaDevicesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.virtual_mfa_devicesCollection"]],
        ],
    ]

    SigningCertificate = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.SigningCertificate"]]],
    ]

    SimulateCustomPolicyPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.SimulateCustomPolicy"]],
        ],
    ]

    SimulatePrincipalPolicyPaginator = Annotated[
        Paginator,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["IAM.Paginator.SimulatePrincipalPolicy"]],
        ],
    ]

    User = Annotated[
        ServiceResource, IsAttr["__class__", IsAttr["__name__", IsEqual["iam.User"]]]
    ]

    UserAccessKeysCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["iam.User.access_keysCollection"]]
        ],
    ]

    UserAttachedPoliciesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.User.attached_policiesCollection"]],
        ],
    ]

    UserExistsWaiter = Annotated[
        Waiter,
        IsAttr["__class__", IsAttr["__name__", IsEqual["IAM.Waiter.UserExists"]]],
    ]

    UserGroupsCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.User.groupsCollection"]]],
    ]

    UserMfaDevicesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__", IsAttr["__name__", IsEqual["iam.User.mfa_devicesCollection"]]
        ],
    ]

    UserPoliciesCollection = Annotated[
        ResourceCollection,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.User.policiesCollection"]]],
    ]

    UserPolicy = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.UserPolicy"]]],
    ]

    UserSigningCertificatesCollection = Annotated[
        ResourceCollection,
        IsAttr[
            "__class__",
            IsAttr["__name__", IsEqual["iam.User.signing_certificatesCollection"]],
        ],
    ]

    VirtualMfaDevice = Annotated[
        ServiceResource,
        IsAttr["__class__", IsAttr["__name__", IsEqual["iam.VirtualMfaDevice"]]],
    ]
