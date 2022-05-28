import pytest
from bearboto3.sns import (
    ListEndpointsByPlatformApplicationPaginator,
    ListPlatformApplicationsPaginator,
    ListSubscriptionsPaginator,
    ListSubscriptionsByTopicPaginator,
    ListTopicsPaginator,
    ListPhoneNumbersOptedOutPaginator,
    ListOriginationNumbersPaginator,
    ListSMSSandboxPhoneNumbersPaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintParamViolation,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ListEndpointsByPlatformApplicationPaginator
# ============================


def test_list_endpoints_by_platform_application_arg_pass(
    gen_list_endpoints_by_platform_application_paginator,
):
    @beartype
    def func(param: ListEndpointsByPlatformApplicationPaginator):
        pass

    func(gen_list_endpoints_by_platform_application_paginator)


def test_list_endpoints_by_platform_application_arg_fail(gen_list_topics_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListEndpointsByPlatformApplicationPaginator):
            pass

        func(gen_list_topics_paginator)


def test_list_endpoints_by_platform_application_return_pass(
    gen_list_endpoints_by_platform_application_paginator,
):
    @beartype
    def func() -> ListEndpointsByPlatformApplicationPaginator:
        return gen_list_endpoints_by_platform_application_paginator

    func()


def test_list_endpoints_by_platform_application_return_fail(gen_list_topics_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListEndpointsByPlatformApplicationPaginator:
            return gen_list_topics_paginator

        func()


# ============================
# ListPlatformApplicationsPaginator
# ============================


def test_list_platform_applications_arg_pass(gen_list_platform_applications_paginator):
    @beartype
    def func(param: ListPlatformApplicationsPaginator):
        pass

    func(gen_list_platform_applications_paginator)


def test_list_platform_applications_arg_fail(gen_list_subscriptions_by_topic_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListPlatformApplicationsPaginator):
            pass

        func(gen_list_subscriptions_by_topic_paginator)


def test_list_platform_applications_return_pass(
    gen_list_platform_applications_paginator,
):
    @beartype
    def func() -> ListPlatformApplicationsPaginator:
        return gen_list_platform_applications_paginator

    func()


def test_list_platform_applications_return_fail(
    gen_list_subscriptions_by_topic_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListPlatformApplicationsPaginator:
            return gen_list_subscriptions_by_topic_paginator

        func()


# ============================
# ListSubscriptionsPaginator
# ============================


def test_list_subscriptions_arg_pass(gen_list_subscriptions_paginator):
    @beartype
    def func(param: ListSubscriptionsPaginator):
        pass

    func(gen_list_subscriptions_paginator)


def test_list_subscriptions_arg_fail(gen_list_platform_applications_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListSubscriptionsPaginator):
            pass

        func(gen_list_platform_applications_paginator)


def test_list_subscriptions_return_pass(gen_list_subscriptions_paginator):
    @beartype
    def func() -> ListSubscriptionsPaginator:
        return gen_list_subscriptions_paginator

    func()


def test_list_subscriptions_return_fail(gen_list_platform_applications_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListSubscriptionsPaginator:
            return gen_list_platform_applications_paginator

        func()


# ============================
# ListSubscriptionsByTopicPaginator
# ============================


def test_list_subscriptions_by_topic_arg_pass(
    gen_list_subscriptions_by_topic_paginator,
):
    @beartype
    def func(param: ListSubscriptionsByTopicPaginator):
        pass

    func(gen_list_subscriptions_by_topic_paginator)


def test_list_subscriptions_by_topic_arg_fail(gen_list_platform_applications_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListSubscriptionsByTopicPaginator):
            pass

        func(gen_list_platform_applications_paginator)


def test_list_subscriptions_by_topic_return_pass(
    gen_list_subscriptions_by_topic_paginator,
):
    @beartype
    def func() -> ListSubscriptionsByTopicPaginator:
        return gen_list_subscriptions_by_topic_paginator

    func()


def test_list_subscriptions_by_topic_return_fail(
    gen_list_platform_applications_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListSubscriptionsByTopicPaginator:
            return gen_list_platform_applications_paginator

        func()


# ============================
# ListTopicsPaginator
# ============================


def test_list_topics_arg_pass(gen_list_topics_paginator):
    @beartype
    def func(param: ListTopicsPaginator):
        pass

    func(gen_list_topics_paginator)


def test_list_topics_arg_fail(gen_list_endpoints_by_platform_application_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListTopicsPaginator):
            pass

        func(gen_list_endpoints_by_platform_application_paginator)


def test_list_topics_return_pass(gen_list_topics_paginator):
    @beartype
    def func() -> ListTopicsPaginator:
        return gen_list_topics_paginator

    func()


def test_list_topics_return_fail(gen_list_endpoints_by_platform_application_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListTopicsPaginator:
            return gen_list_endpoints_by_platform_application_paginator

        func()


# ============================
# ListPhoneNumbersOptedOutPaginator
# ============================


def test_list_phone_numbers_opted_out_arg_pass(
    gen_list_phone_numbers_opted_out_paginator,
):
    @beartype
    def func(param: ListPhoneNumbersOptedOutPaginator):
        pass

    func(gen_list_phone_numbers_opted_out_paginator)


def test_list_phone_numbers_opted_out_arg_fail(
    gen_list_platform_applications_paginator,
):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListPhoneNumbersOptedOutPaginator):
            pass

        func(gen_list_platform_applications_paginator)


def test_list_phone_numbers_opted_out_return_pass(
    gen_list_phone_numbers_opted_out_paginator,
):
    @beartype
    def func() -> ListPhoneNumbersOptedOutPaginator:
        return gen_list_phone_numbers_opted_out_paginator

    func()


def test_list_phone_numbers_opted_out_return_fail(
    gen_list_platform_applications_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListPhoneNumbersOptedOutPaginator:
            return gen_list_platform_applications_paginator

        func()


# ============================
# ListOriginationNumbersPaginator
# ============================


def test_list_origination_numbers_arg_pass(gen_list_origination_numbers_paginator):
    @beartype
    def func(param: ListOriginationNumbersPaginator):
        pass

    func(gen_list_origination_numbers_paginator)


def test_list_origination_numbers_arg_fail(gen_list_phone_numbers_opted_out_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListOriginationNumbersPaginator):
            pass

        func(gen_list_phone_numbers_opted_out_paginator)


def test_list_origination_numbers_return_pass(gen_list_origination_numbers_paginator):
    @beartype
    def func() -> ListOriginationNumbersPaginator:
        return gen_list_origination_numbers_paginator

    func()


def test_list_origination_numbers_return_fail(
    gen_list_phone_numbers_opted_out_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListOriginationNumbersPaginator:
            return gen_list_phone_numbers_opted_out_paginator

        func()


# ============================
# ListSMSSandboxPhoneNumbersPaginator
# ============================


def test_list_sms_sandbox_phone_numbers_arg_pass(
    gen_list_sms_sandbox_phone_numbers_paginator,
):
    @beartype
    def func(param: ListSMSSandboxPhoneNumbersPaginator):
        pass

    func(gen_list_sms_sandbox_phone_numbers_paginator)


def test_list_sms_sandbox_phone_numbers_arg_fail(gen_list_topics_paginator):
    with pytest.raises(BeartypeCallHintParamViolation):

        @beartype
        def func(param: ListSMSSandboxPhoneNumbersPaginator):
            pass

        func(gen_list_topics_paginator)


def test_list_sms_sandbox_phone_numbers_return_pass(
    gen_list_sms_sandbox_phone_numbers_paginator,
):
    @beartype
    def func() -> ListSMSSandboxPhoneNumbersPaginator:
        return gen_list_sms_sandbox_phone_numbers_paginator

    func()


def test_list_sms_sandbox_phone_numbers_return_fail(gen_list_topics_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListSMSSandboxPhoneNumbersPaginator:
            return gen_list_topics_paginator

        func()
