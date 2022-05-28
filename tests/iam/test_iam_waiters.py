import pytest
from bearboto3.iam import (
    InstanceProfileExistsWaiter,
    UserExistsWaiter,
    RoleExistsWaiter,
    PolicyExistsWaiter,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# InstanceProfileExistsWaiter
# ============================


def test_instance_profile_exists_arg_pass(gen_instance_profile_exists_waiter):
    @beartype
    def func(param: InstanceProfileExistsWaiter):
        pass

    func(gen_instance_profile_exists_waiter)


def test_instance_profile_exists_arg_fail(gen_user_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: InstanceProfileExistsWaiter):
            pass

        func(gen_user_exists_waiter)


def test_instance_profile_exists_return_pass(gen_instance_profile_exists_waiter):
    @beartype
    def func() -> InstanceProfileExistsWaiter:
        return gen_instance_profile_exists_waiter

    func()


def test_instance_profile_exists_return_fail(gen_user_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> InstanceProfileExistsWaiter:
            return gen_user_exists_waiter

        func()


# ============================
# UserExistsWaiter
# ============================


def test_user_exists_arg_pass(gen_user_exists_waiter):
    @beartype
    def func(param: UserExistsWaiter):
        pass

    func(gen_user_exists_waiter)


def test_user_exists_arg_fail(gen_instance_profile_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: UserExistsWaiter):
            pass

        func(gen_instance_profile_exists_waiter)


def test_user_exists_return_pass(gen_user_exists_waiter):
    @beartype
    def func() -> UserExistsWaiter:
        return gen_user_exists_waiter

    func()


def test_user_exists_return_fail(gen_instance_profile_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> UserExistsWaiter:
            return gen_instance_profile_exists_waiter

        func()


# ============================
# RoleExistsWaiter
# ============================


def test_role_exists_arg_pass(gen_role_exists_waiter):
    @beartype
    def func(param: RoleExistsWaiter):
        pass

    func(gen_role_exists_waiter)


def test_role_exists_arg_fail(gen_user_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: RoleExistsWaiter):
            pass

        func(gen_user_exists_waiter)


def test_role_exists_return_pass(gen_role_exists_waiter):
    @beartype
    def func() -> RoleExistsWaiter:
        return gen_role_exists_waiter

    func()


def test_role_exists_return_fail(gen_user_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> RoleExistsWaiter:
            return gen_user_exists_waiter

        func()


# ============================
# PolicyExistsWaiter
# ============================


def test_policy_exists_arg_pass(gen_policy_exists_waiter):
    @beartype
    def func(param: PolicyExistsWaiter):
        pass

    func(gen_policy_exists_waiter)


def test_policy_exists_arg_fail(gen_role_exists_waiter):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: PolicyExistsWaiter):
            pass

        func(gen_role_exists_waiter)


def test_policy_exists_return_pass(gen_policy_exists_waiter):
    @beartype
    def func() -> PolicyExistsWaiter:
        return gen_policy_exists_waiter

    func()


def test_policy_exists_return_fail(gen_role_exists_waiter):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> PolicyExistsWaiter:
            return gen_role_exists_waiter

        func()
