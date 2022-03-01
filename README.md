# bearboto3

[![Test](https://github.com/beartype/bearboto3/actions/workflows/test.yml/badge.svg)](https://github.com/beartype/bearboto3/actions/workflows/test.yml) ![PyPI - Downloads](https://img.shields.io/pypi/dm/bearboto3)

This project provides support for using the [boto3](https://github.com/boto/boto3/) library (AWS Python SDK) and associated stub libraries such as [boto3-stubs](https://pypi.org/project/boto3-stubs/) together with [beartype](https://github.com/beartype/beartype/) for runtime type-checking.

Since boto3 uses a data-driven factory model to create class types at runtime, you cannot annotate them without support of stub libraries such as `boto3-stubs`. However, if you are using a runtime type-checker such as `beartype`, type validation will fail since the types technically do not match (even though they represent the same object schema).

_Behold..._

this project makes use of the [`typing.TYPE_CHECKING`](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING) constant found in the python `typing` module to conditionally load either static types from a stub library (in this case `boto3-stubs`), or custom annotated types that can be checked with `beartype`.

## Installation/Use

See the [list of services](services.md) to see what is currently implemented.

### Supported python versions:
- `>= 3.7`

Install with `pip`:

`pip3 install bearboto3`

or with whatever dependency management tool you use (like [`poetry`](https://python-poetry.org/)):

`poetry add bearboto3`

Then in your code, import the specific types you need:

```python
from beartype import beartype
from bearboto3.s3 import S3Client, Bucket
import boto3

@beartype
def example(s3: S3Client) -> Bucket:
    return s3.create_bucket(Bucket='mybucket')

s3_client = boto3.client('s3')
bucket = example(s3_client)
```

You will be able to have your salmon and eat it too!

## Installing the type stubs
At present, there does not appear to be a way in `pyproject.toml` to specify extra/optional packages that should be installed as _dev_ dependencies. The type stubs for each service (which allow for IDE integration courtsey of [boto3-stubs](https://pypi.org/project/boto3-stubs/)) can be installed as extras such as:

`poetry install bearboto3[s3]`

but **NOTE** this will install the type stubs as _runtime_ dependencies given the limitations above. The type stub libraries are _not_ needed to run any code you use this package with, so the recommended approach is to install whatever type stubs you need yourself in your project's `dev-dependencies` section.

Future work includes being able to isolate installing `bearboto3` runtime type definitions per service, like you are able to specify with `moto` and `boto3-stubs`.

## Contributing

See [contributing](contributing.md)

## Acknowledgements

* @leycec For being an avid supporter and welcoming me to the `beartype` family
