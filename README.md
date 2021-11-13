# bearboto3 

This project provides support for using the [boto3](https://github.com/boto/boto3/) library (AWS Python SDK) and associated stub libraries such as [boto3-stubs](https://pypi.org/project/boto3-stubs/) together with [beartype](https://github.com/beartype/beartype/) for runtime type-checking.

Since boto3 uses a data-drive factory model to create class types at runtime, you cannot annotate them without support of stub libraries such as `boto3-stubs`. However, if you are using a runtime type-checker such as `beartype`, type validation will since the types technically do not match (even though they represent the same object schema). It is possible to define custom types and annotate with them, but you lose access to the various IDE integrations (such as autocomplete) that you get with the static type stub libraries.

*Behold...* 

Using the approach pioneered in [this issue](https://github.com/beartype/beartype/issues/68) and [now documented in beartype](https://github.com/beartype/beartype/#boto3-types), this project makes use of the [`typing.TYPE_CHECKING`](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING) constant found in the python `typing` module to conditionally load either static types from a stub library (in this case `boto3-stubs`), or custom annotated types that can be checked and are compatible with runtime type-checkers (in this case `beartype`).

## Installation/Use

**Note:** Only python >=3.5.2 is supported, as the `typing.TYPE_CHECKING` constant was not introduced prior.

Install with `pip`:

`pip3 install bearboto3`

or with whatever dependency management tool you use (like [`poetry`](https://python-poetry.org/)):

`poetry add bearboto3`

Then in your code, import the specific types you need:

```python
from beartype import beartype
from bearboto3.s3 import S3, Bucket
import boto3

@beartype
def example(s3: S3) -> Bucket:
    return s3.create_bucket(Bucket='mybucket')

s3_client = boto3.client('s3')
bucket = example(s3_client)
```

You will get the benefit of both the IDE integrations provided by the stub libraries, as well as being able to type-check your code with runtime checkers.

## Developing
- Install [poetry](https://python-poetry.org/)
- Navigate to the project folder and run `poetry install` to setup the virtualenv
- Configure your IDE to use the virtualenv (you can run `poetry env info` to get the path if it's not auto-detected)
- Access the virtualenv via `poetry shell`
- ???
- Profit$$$
  
Each AWS service should get its own module (file) that the types are defined in.

### Figuring out the types
To figure out the corresponding `boto3` type, you must execute python code to create an object of the type you are looking for. Then, examine the value of the `boto3_obj.__class__.__name__` attribute to get the type. This value is what is used by the custom annotated types to perform type comparisons/checking.

## Contributing
If you are interested in contributing, thank you! The more the merrier! 

AWS and the SDK have a lot of services, which means a lot of types to add support for. Creating a PR for a given service is the best way to help this project grow and allow everyone to reap the benefits of type-hinting and runtime type-checking!
