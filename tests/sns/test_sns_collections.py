import pytest
from bearboto3.sns import (
    ServiceResourcePlatformApplicationsCollection,
    ServiceResourceSubscriptionsCollection,
    ServiceResourceTopicsCollection,
    PlatformApplicationEndpointsCollection,
    TopicSubscriptionsCollection,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ServiceResourcePlatformApplicationsCollection
# ============================


def test_platform_applications_arg_pass(
    gen_service_resource_platform_applications_collection,
):
    @beartype
    def func(param: ServiceResourcePlatformApplicationsCollection):
        pass

    func(gen_service_resource_platform_applications_collection)


def test_platform_applications_arg_fail(gen_platform_application_endpoints_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ServiceResourcePlatformApplicationsCollection):
            pass

        func(gen_platform_application_endpoints_collection)


def test_platform_applications_return_pass(
    gen_service_resource_platform_applications_collection,
):
    @beartype
    def func() -> ServiceResourcePlatformApplicationsCollection:
        return gen_service_resource_platform_applications_collection

    func()


def test_platform_applications_return_fail(
    gen_platform_application_endpoints_collection,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourcePlatformApplicationsCollection:
            return gen_platform_application_endpoints_collection

        func()


# ============================
# ServiceResourceSubscriptionsCollection
# ============================


def test_subscriptions_arg_pass(gen_service_resource_subscriptions_collection):
    @beartype
    def func(param: ServiceResourceSubscriptionsCollection):
        pass

    func(gen_service_resource_subscriptions_collection)


def test_subscriptions_arg_fail(gen_service_resource_platform_applications_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ServiceResourceSubscriptionsCollection):
            pass

        func(gen_service_resource_platform_applications_collection)


def test_subscriptions_return_pass(gen_service_resource_subscriptions_collection):
    @beartype
    def func() -> ServiceResourceSubscriptionsCollection:
        return gen_service_resource_subscriptions_collection

    func()


def test_subscriptions_return_fail(
    gen_service_resource_platform_applications_collection,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceSubscriptionsCollection:
            return gen_service_resource_platform_applications_collection

        func()


# ============================
# ServiceResourceTopicsCollection
# ============================


def test_topics_arg_pass(gen_service_resource_topics_collection):
    @beartype
    def func(param: ServiceResourceTopicsCollection):
        pass

    func(gen_service_resource_topics_collection)


def test_topics_arg_fail(gen_platform_application_endpoints_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ServiceResourceTopicsCollection):
            pass

        func(gen_platform_application_endpoints_collection)


def test_topics_return_pass(gen_service_resource_topics_collection):
    @beartype
    def func() -> ServiceResourceTopicsCollection:
        return gen_service_resource_topics_collection

    func()


def test_topics_return_fail(gen_platform_application_endpoints_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ServiceResourceTopicsCollection:
            return gen_platform_application_endpoints_collection

        func()


# ============================
# PlatformApplicationEndpointsCollection
# ============================


def test_endpoints_arg_pass(gen_platform_application_endpoints_collection):
    @beartype
    def func(param: PlatformApplicationEndpointsCollection):
        pass

    func(gen_platform_application_endpoints_collection)


def test_endpoints_arg_fail(gen_service_resource_subscriptions_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: PlatformApplicationEndpointsCollection):
            pass

        func(gen_service_resource_subscriptions_collection)


def test_endpoints_return_pass(gen_platform_application_endpoints_collection):
    @beartype
    def func() -> PlatformApplicationEndpointsCollection:
        return gen_platform_application_endpoints_collection

    func()


def test_endpoints_return_fail(gen_service_resource_subscriptions_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PlatformApplicationEndpointsCollection:
            return gen_service_resource_subscriptions_collection

        func()


# ============================
# TopicSubscriptionsCollection
# ============================


def test_subscriptions_arg_pass(gen_topic_subscriptions_collection):
    @beartype
    def func(param: TopicSubscriptionsCollection):
        pass

    func(gen_topic_subscriptions_collection)


def test_subscriptions_arg_fail(gen_service_resource_topics_collection):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: TopicSubscriptionsCollection):
            pass

        func(gen_service_resource_topics_collection)


def test_subscriptions_return_pass(gen_topic_subscriptions_collection):
    @beartype
    def func() -> TopicSubscriptionsCollection:
        return gen_topic_subscriptions_collection

    func()


def test_subscriptions_return_fail(gen_service_resource_topics_collection):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> TopicSubscriptionsCollection:
            return gen_service_resource_topics_collection

        func()
