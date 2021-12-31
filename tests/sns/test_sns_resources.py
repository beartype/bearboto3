import pytest
from bearboto3.sns import (
    PlatformApplication,
    PlatformEndpoint,
    Subscription,
    Topic,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintPepReturnException,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# PlatformApplication
# ============================


def test_platform_application_arg_pass(gen_platform_application):
    @beartype
    def func(param: PlatformApplication):
        pass

    func(gen_platform_application)


def test_platform_application_arg_fail(gen_subscription):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PlatformApplication):
            pass

        func(gen_subscription)


def test_platform_application_return_pass(gen_platform_application):
    @beartype
    def func() -> PlatformApplication:
        return gen_platform_application

    func()


def test_platform_application_return_fail(gen_subscription):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PlatformApplication:
            return gen_subscription

        func()


# ============================
# PlatformEndpoint
# ============================


def test_platform_endpoint_arg_pass(gen_platform_endpoint):
    @beartype
    def func(param: PlatformEndpoint):
        pass

    func(gen_platform_endpoint)


def test_platform_endpoint_arg_fail(gen_subscription):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PlatformEndpoint):
            pass

        func(gen_subscription)


def test_platform_endpoint_return_pass(gen_platform_endpoint):
    @beartype
    def func() -> PlatformEndpoint:
        return gen_platform_endpoint

    func()


def test_platform_endpoint_return_fail(gen_subscription):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PlatformEndpoint:
            return gen_subscription

        func()


# ============================
# Subscription
# ============================


def test_subscription_arg_pass(gen_subscription):
    @beartype
    def func(param: Subscription):
        pass

    func(gen_subscription)


def test_subscription_arg_fail(gen_topic):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Subscription):
            pass

        func(gen_topic)


def test_subscription_return_pass(gen_subscription):
    @beartype
    def func() -> Subscription:
        return gen_subscription

    func()


def test_subscription_return_fail(gen_topic):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Subscription:
            return gen_topic

        func()


# ============================
# Topic
# ============================


def test_topic_arg_pass(gen_topic):
    @beartype
    def func(param: Topic):
        pass

    func(gen_topic)


def test_topic_arg_fail(gen_platform_endpoint):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: Topic):
            pass

        func(gen_platform_endpoint)


def test_topic_return_pass(gen_topic):
    @beartype
    def func() -> Topic:
        return gen_topic

    func()


def test_topic_return_fail(gen_platform_endpoint):
    with pytest.raises(
        (BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> Topic:
            return gen_platform_endpoint

        func()
