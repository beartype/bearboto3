# Beartype Boto3 example

This is an example environment for trying to use [beartype](https://github.com/beartype) with the AWS Python SDK (boto3). 

Since boto3 [uses a factory to dynamically create the various class _types_ at runtime](https://github.com/boto/boto3/blob/develop/boto3/resources/factory.py#L139), you normally cannot annotate them. The [boto3-stubs](https://pypi.org/project/boto3-stubs/) package exists as a way to provide both types to annotate with, as well as allowing various IDE auto-complete features to work.

However, if one is decorating functions that accept or return boto3 types with beartype, validation will fail since the types do not match (even though they effectively represent the same object schema).

This small project provides a reproducible example to serve as a starting point for further investigation and finding potential solutions.

### Using this sample project

- Install [poetry](https://python-poetry.org/)
- Navigate to the project folder and run `poetry install` to setup the virtualenv
- Access the virtualenv via `poetry shell`
- Run the example with `python3 example.py`