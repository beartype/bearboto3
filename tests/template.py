"""A template for creating unit tests for a service.
Simply copy/paste, and change the following values based
on the test:

- foo_type: The name of the type being tested in snake case
- FooType: The name of the type itself
- pass_fixture: The name of a pytest fixture that returns an object of
    the correct type being tested
- fail_fixture: The name of a pytest fixture that returns an object of
    the incorrect type based on the same base class of the type being tested
- SECTION: The category or type name the following tests are for.
    Used to improve readability and maintainence of the test files.
"""

# ============================
# SECTION
# ============================

# def test_foo_type_arg_pass(pass_fixture):
#     @beartype
#     def func(param: FooType):
#         pass
#     func(pass_fixture)

# def test_foo_type_arg_fail(fail_fixture):
#     with pytest.raises(BeartypeCallHintPepParamException):
#         @beartype
#         def func(param: FooType):
#             pass
#         func(fail_fixture)

# def test_foo_type_return_pass(pass_fixture):
#     @beartype
#     def func() -> FooType:
#         return pass_fixture
#     param = func()

# def test_foo_type_return_fail(fail_fixture):
#     with pytest.raises((BeartypeCallHintPepReturnException, BeartypeDecorHintPep484585Exception)):
#         @beartype
#         def func() -> FooType:
#             return fail_fixture
#         param = func()
