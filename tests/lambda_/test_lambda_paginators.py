import pytest
from bearboto3.lambda_ import (
    ListEventSourceMappingsPaginator,
    ListFunctionsPaginator,
    ListAliasesPaginator,
    ListLayerVersionsPaginator,
    ListLayersPaginator,
    ListVersionsByFunctionPaginator,
    ListFunctionEventInvokeConfigsPaginator,
    ListProvisionedConcurrencyConfigsPaginator,
    ListCodeSigningConfigsPaginator,
    ListFunctionsByCodeSigningConfigPaginator,
)
from beartype import beartype
from beartype.roar import (
    BeartypeCallHintPepParamException,
    BeartypeCallHintReturnViolation,
    BeartypeDecorHintPep484585Exception,
)


# ============================
# ListEventSourceMappingsPaginator
# ============================


def test_list_event_source_mappings_arg_pass(gen_list_event_source_mappings_paginator):
    @beartype
    def func(param: ListEventSourceMappingsPaginator):
        pass

    func(gen_list_event_source_mappings_paginator)


def test_list_event_source_mappings_arg_fail(
    gen_list_functions_by_code_signing_config_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListEventSourceMappingsPaginator):
            pass

        func(gen_list_functions_by_code_signing_config_paginator)


def test_list_event_source_mappings_return_pass(
    gen_list_event_source_mappings_paginator,
):
    @beartype
    def func() -> ListEventSourceMappingsPaginator:
        return gen_list_event_source_mappings_paginator

    func()


def test_list_event_source_mappings_return_fail(
    gen_list_functions_by_code_signing_config_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListEventSourceMappingsPaginator:
            return gen_list_functions_by_code_signing_config_paginator

        func()


# ============================
# ListFunctionsPaginator
# ============================


def test_list_functions_arg_pass(gen_list_functions_paginator):
    @beartype
    def func(param: ListFunctionsPaginator):
        pass

    func(gen_list_functions_paginator)


def test_list_functions_arg_fail(gen_list_code_signing_configs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListFunctionsPaginator):
            pass

        func(gen_list_code_signing_configs_paginator)


def test_list_functions_return_pass(gen_list_functions_paginator):
    @beartype
    def func() -> ListFunctionsPaginator:
        return gen_list_functions_paginator

    func()


def test_list_functions_return_fail(gen_list_code_signing_configs_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListFunctionsPaginator:
            return gen_list_code_signing_configs_paginator

        func()


# ============================
# ListAliasesPaginator
# ============================


def test_list_aliases_arg_pass(gen_list_aliases_paginator):
    @beartype
    def func(param: ListAliasesPaginator):
        pass

    func(gen_list_aliases_paginator)


def test_list_aliases_arg_fail(gen_list_provisioned_concurrency_configs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListAliasesPaginator):
            pass

        func(gen_list_provisioned_concurrency_configs_paginator)


def test_list_aliases_return_pass(gen_list_aliases_paginator):
    @beartype
    def func() -> ListAliasesPaginator:
        return gen_list_aliases_paginator

    func()


def test_list_aliases_return_fail(gen_list_provisioned_concurrency_configs_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListAliasesPaginator:
            return gen_list_provisioned_concurrency_configs_paginator

        func()


# ============================
# ListLayerVersionsPaginator
# ============================


def test_list_layer_versions_arg_pass(gen_list_layer_versions_paginator):
    @beartype
    def func(param: ListLayerVersionsPaginator):
        pass

    func(gen_list_layer_versions_paginator)


def test_list_layer_versions_arg_fail(gen_list_aliases_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListLayerVersionsPaginator):
            pass

        func(gen_list_aliases_paginator)


def test_list_layer_versions_return_pass(gen_list_layer_versions_paginator):
    @beartype
    def func() -> ListLayerVersionsPaginator:
        return gen_list_layer_versions_paginator

    func()


def test_list_layer_versions_return_fail(gen_list_aliases_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListLayerVersionsPaginator:
            return gen_list_aliases_paginator

        func()


# ============================
# ListLayersPaginator
# ============================


def test_list_layers_arg_pass(gen_list_layers_paginator):
    @beartype
    def func(param: ListLayersPaginator):
        pass

    func(gen_list_layers_paginator)


def test_list_layers_arg_fail(gen_list_code_signing_configs_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListLayersPaginator):
            pass

        func(gen_list_code_signing_configs_paginator)


def test_list_layers_return_pass(gen_list_layers_paginator):
    @beartype
    def func() -> ListLayersPaginator:
        return gen_list_layers_paginator

    func()


def test_list_layers_return_fail(gen_list_code_signing_configs_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListLayersPaginator:
            return gen_list_code_signing_configs_paginator

        func()


# ============================
# ListVersionsByFunctionPaginator
# ============================


def test_list_versions_by_function_arg_pass(gen_list_versions_by_function_paginator):
    @beartype
    def func(param: ListVersionsByFunctionPaginator):
        pass

    func(gen_list_versions_by_function_paginator)


def test_list_versions_by_function_arg_fail(
    gen_list_function_event_invoke_configs_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListVersionsByFunctionPaginator):
            pass

        func(gen_list_function_event_invoke_configs_paginator)


def test_list_versions_by_function_return_pass(gen_list_versions_by_function_paginator):
    @beartype
    def func() -> ListVersionsByFunctionPaginator:
        return gen_list_versions_by_function_paginator

    func()


def test_list_versions_by_function_return_fail(
    gen_list_function_event_invoke_configs_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListVersionsByFunctionPaginator:
            return gen_list_function_event_invoke_configs_paginator

        func()


# ============================
# ListFunctionEventInvokeConfigsPaginator
# ============================


def test_list_function_event_invoke_configs_arg_pass(
    gen_list_function_event_invoke_configs_paginator,
):
    @beartype
    def func(param: ListFunctionEventInvokeConfigsPaginator):
        pass

    func(gen_list_function_event_invoke_configs_paginator)


def test_list_function_event_invoke_configs_arg_fail(
    gen_list_code_signing_configs_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListFunctionEventInvokeConfigsPaginator):
            pass

        func(gen_list_code_signing_configs_paginator)


def test_list_function_event_invoke_configs_return_pass(
    gen_list_function_event_invoke_configs_paginator,
):
    @beartype
    def func() -> ListFunctionEventInvokeConfigsPaginator:
        return gen_list_function_event_invoke_configs_paginator

    func()


def test_list_function_event_invoke_configs_return_fail(
    gen_list_code_signing_configs_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListFunctionEventInvokeConfigsPaginator:
            return gen_list_code_signing_configs_paginator

        func()


# ============================
# ListProvisionedConcurrencyConfigsPaginator
# ============================


def test_list_provisioned_concurrency_configs_arg_pass(
    gen_list_provisioned_concurrency_configs_paginator,
):
    @beartype
    def func(param: ListProvisionedConcurrencyConfigsPaginator):
        pass

    func(gen_list_provisioned_concurrency_configs_paginator)


def test_list_provisioned_concurrency_configs_arg_fail(
    gen_list_function_event_invoke_configs_paginator,
):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListProvisionedConcurrencyConfigsPaginator):
            pass

        func(gen_list_function_event_invoke_configs_paginator)


def test_list_provisioned_concurrency_configs_return_pass(
    gen_list_provisioned_concurrency_configs_paginator,
):
    @beartype
    def func() -> ListProvisionedConcurrencyConfigsPaginator:
        return gen_list_provisioned_concurrency_configs_paginator

    func()


def test_list_provisioned_concurrency_configs_return_fail(
    gen_list_function_event_invoke_configs_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListProvisionedConcurrencyConfigsPaginator:
            return gen_list_function_event_invoke_configs_paginator

        func()


# ============================
# ListCodeSigningConfigsPaginator
# ============================


def test_list_code_signing_configs_arg_pass(gen_list_code_signing_configs_paginator):
    @beartype
    def func(param: ListCodeSigningConfigsPaginator):
        pass

    func(gen_list_code_signing_configs_paginator)


def test_list_code_signing_configs_arg_fail(gen_list_functions_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListCodeSigningConfigsPaginator):
            pass

        func(gen_list_functions_paginator)


def test_list_code_signing_configs_return_pass(gen_list_code_signing_configs_paginator):
    @beartype
    def func() -> ListCodeSigningConfigsPaginator:
        return gen_list_code_signing_configs_paginator

    func()


def test_list_code_signing_configs_return_fail(gen_list_functions_paginator):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListCodeSigningConfigsPaginator:
            return gen_list_functions_paginator

        func()


# ============================
# ListFunctionsByCodeSigningConfigPaginator
# ============================


def test_list_functions_by_code_signing_config_arg_pass(
    gen_list_functions_by_code_signing_config_paginator,
):
    @beartype
    def func(param: ListFunctionsByCodeSigningConfigPaginator):
        pass

    func(gen_list_functions_by_code_signing_config_paginator)


def test_list_functions_by_code_signing_config_arg_fail(gen_list_functions_paginator):
    with pytest.raises(BeartypeCallHintPepParamException):

        @beartype
        def func(param: ListFunctionsByCodeSigningConfigPaginator):
            pass

        func(gen_list_functions_paginator)


def test_list_functions_by_code_signing_config_return_pass(
    gen_list_functions_by_code_signing_config_paginator,
):
    @beartype
    def func() -> ListFunctionsByCodeSigningConfigPaginator:
        return gen_list_functions_by_code_signing_config_paginator

    func()


def test_list_functions_by_code_signing_config_return_fail(
    gen_list_functions_paginator,
):
    with pytest.raises(
        (BeartypeCallHintReturnViolation, BeartypeDecorHintPep484585Exception)
    ):

        @beartype
        def func() -> ListFunctionsByCodeSigningConfigPaginator:
            return gen_list_functions_paginator

        func()
