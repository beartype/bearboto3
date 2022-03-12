# Contributing

If you are interested in contributing, thank you! The more the merrier!

AWS and the SDK have a lot of services, which means a lot of types to add support for. Creating a PR for a given service is the best way to help this project grow and allow everyone to reap the benefits of type-annotating and runtime type-checking!

Below should be all the steps you need to get started. Don't hestitate to create an issue or PR to improve the docs if you think something's missing.

## Dev Setup

- Install [poetry](https://python-poetry.org/)
- Navigate to the project folder and run `poetry install` to setup the virtualenv
- Configure your IDE to use the virtualenv (you can run `poetry env info` to get the path if it's not auto-detected)
- Access the virtualenv via `poetry shell`
- ???
- Profit$$$

Each AWS service should get its own module (file) that the types are defined in.

## Figuring out the types

To figure out the corresponding `boto3` type and annotate it, you need 2 things:

- The base class type that the object inherits from (yes, despite the nefarious factory nonsense going on, there are still statically-existing (though empty) base classes that everything else in boto inherits from). Typically, this will be one of the following:
  - `boto3.resources.base.ServiceResource`
  - `boto3.resources.collection.ResourceCollection`
  - `botocore.client.BaseClient`
  - `botocore.paginate.Paginator`
  - `botocore.waiter.Waiter`
- The class name, which is shown by calling `type` on the object, or by accessing its `__class__.__name__` attribute.

### The automated way
Use the scripts provided in the `tools` folder to automate the process. The scripts will parse the JSON schema from boto and extract the necessary data for annotating the classes to work with beartype, as well as creating the test suites through the use of jinja2 templates.

A typical workflow will look like this:

1. `tools/map_classes.py --service ec2`
2. `tools/annotate_classes.py --service ec2`
3. `tools/create_fixtures.py --service ec2`
4. `tools/create_tests.py --service ec2`

Note that the scripts may not be perfect, but should vastly cut down the amount of manual work needed. Very little (if anything) should need to be tweaked in order for the tests to pass after running the scripts if adding a new service.

### The manual way
You can _generally_ use the type indicated in the boto3 docs for the class name as a starting point. Some types, like the waiters and paginators, you can copy the class name given in the docs (ex. the class name of `ObjectExistsWaiter` is `S3.Waiter.ObjectExists` exactly as listed in the docs). Others, like many of the service resource based classes (like `Bucket`) are _almost_ identical (e.g. `Bucket` is actually `s3.Bucket` - note the lowercase vs the docs). And still others (like the collections) will use underscores, camelcase, or other conventions:

- `BucketObjectsCollection` (`Bucket.objects.all()`) is `s3.Bucket.objectsCollection`, _**not**_ `list(ObjectSummary)` like the docs say.
- `BucketObjectVersionsCollection` (`Bucket.object_versions.all()`) is `s3.Bucket.object_versionsCollection`

You get the idea. I recommend starting with the types exactly as they are from the docs, and then use your unit tests to highlight any inconsistencies. You can also check the types manually by running some snippet of code to create the object in question, then examine the type.

```python
# Suggested helper function if you are having to grab multiple types
def get_type(obj):
    return obj.__class__.__name__

resource = boto3.resource('s3')
get_type(resource.Bucket('foo'))
# 's3.Bucket'
```

# Testing

This project uses pytest as the unit testing framework. By default, pytest is configured to run and produce a coverage report, all you need to do is run `pytest` (if using VS Code, I recommend setting `--no-cov` in `python.testing.pytestArgs` in your `settings.json` otherwise the code coverage settings will likely cause the test discovery and IDE integration to fail.

## Creating tests

Each type should have the following scenarios covered:

- Passing the type as an argument correctly
- Passing in a similar type (that is of the same base class) that is incorrect that should throw an error
- Returning the type from a function correctly
- Returning a similar type (that is of the same base class) that is incorrect from a function that should throw an error

[`Moto`](https://github.com/spulec/moto) is used to mock the boto3 library. There is an existing pytest fixture called `aws_setup` that mocks the needed boto3 aws variables and is globally available in all files in the `tests/` folder (you don't need to import it). It is also recommended to create pytest fixtures for the client and resource of the AWS service you are working with:

```python
@pytest.fixture
def gen_s3_resource(aws_setup):
    with mock_s3():
        yield boto3.resource('s3')
```

You can then request the fixture in your tests and ensure you have the necessary mocked services for testing.