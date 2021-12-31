# bearboto3

This project provides support for using the [boto3](https://github.com/boto/boto3/) library (AWS Python SDK) and associated stub libraries such as [boto3-stubs](https://pypi.org/project/boto3-stubs/) together with [beartype](https://github.com/beartype/beartype/) for runtime type-checking.

Since boto3 uses a data-driven factory model to create class types at runtime, you cannot annotate them without support of stub libraries such as `boto3-stubs`. However, if you are using a runtime type-checker such as `beartype`, type validation will fail since the types technically do not match (even though they represent the same object schema). It is possible to define custom types and annotate with them, but you lose access to the various IDE integrations (such as autocomplete) that you get with the static type stub libraries.

_Behold..._

Using the approach pioneered in [this issue](https://github.com/beartype/beartype/issues/68) and [now documented in beartype](https://github.com/beartype/beartype/#boto3-types), this project makes use of the [`typing.TYPE_CHECKING`](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING) constant found in the python `typing` module to conditionally load either static types from a stub library (in this case `boto3-stubs`), or custom annotated types that can be checked and are compatible with runtime type-checkers (in this case `beartype`).

## Installation/Use

See the [list of services](https://github.com/paulhutchings/bearboto3/#supported-aws-services) to see what is currently supported.

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

## Contributing

If you are interested in contributing, thank you! The more the merrier!

AWS and the SDK have a lot of services, which means a lot of types to add support for. Creating a PR for a given service is the best way to help this project grow and allow everyone to reap the benefits of type-hinting and runtime type-checking!

### Dev Setup

- Install [poetry](https://python-poetry.org/)
- Navigate to the project folder and run `poetry install` to setup the virtualenv
- Configure your IDE to use the virtualenv (you can run `poetry env info` to get the path if it's not auto-detected)
- Access the virtualenv via `poetry shell`
- ???
- Profit$$$

Each AWS service should get its own module (file) that the types are defined in.

### Figuring out the types

To figure out the corresponding `boto3` type and annotate it, you need 2 things:

- The base class type that the object inherits from (yes, despite the nefarious factory nonsense going on, there are still statically-existing (though empty) base classes that everything else in boto inherits from). Typically, this will be one of the following:
  - `boto3.resources.base.ServiceResource`
  - `boto3.resources.collection.ResourceCollection`
  - `botocore.client.BaseClient`
  - `botocore.paginate.Paginator`
  - `botocore.waiter.Waiter`
- The class name, which is shown by calling `type` on the object, or by accessing its `__class__.__name__` attribute.

#### The automated way
Use the scripts provided in the `tools` folder to automate the process. The scripts will parse the JSON schema from boto and extract the necessary data for annotating the classes to work with beartype, as well as creating the test suites through the use of jinja2 templates.

A typical workflow will look like this:

1. `tools/map_classes.py --service ec2`
2. `tools/annotate_classes.py --service ec2`
3. `tools/create_fixtures.py --service ec2`
4. `tools/create_tests.py --service ec2`

Note that the scripts may not be perfect, but should vastly cut down the amount of manual work needed. Very little (if anything) should need to be tweaked in order for the tests to pass after running the scripts if adding a new service.

#### The manual way
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

## Testing

This project uses pytest as the unit testing framework. By default, pytest is configured to run and produce a coverage report, all you need to do is run `pytest` (if using VS Code, I recommend setting `--no-cov` in `python.testing.pytestArgs` in your `settings.json` otherwise the code coverage settings will likely cause the test discovery and IDE integration to fail.

### Creating tests

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

## Supported AWS Services

- [ ] AccessAnalyzer
- [ ] Account
- [ ] ACM
- [ ] ACMPCA
- [ ] AlexaForBusiness
- [ ] Amplify
- [ ] AmplifyBackend
- [ ] APIGateway
- [ ] ApiGatewayManagementApi
- [ ] ApiGatewayV2
- [ ] AppConfig
- [ ] Appflow
- [ ] AppIntegrationsService
- [ ] ApplicationAutoScaling
- [ ] ApplicationCostProfiler
- [ ] ApplicationDiscoveryService
- [ ] ApplicationInsights
- [ ] AppMesh
- [ ] AppRegistry
- [ ] AppRunner
- [ ] AppStream
- [ ] AppSync
- [ ] Athena
- [ ] AuditManager
- [ ] AugmentedAIRuntime
- [ ] AutoScaling
- [ ] AutoScalingPlans
- [ ] Backup
- [ ] Batch
- [ ] Braket
- [ ] Budgets
- [ ] Chime
- [ ] ChimeSDKIdentity
- [ ] ChimeSDKMeetings
- [ ] ChimeSDKMessaging
- [ ] Cloud9
- [ ] CloudControlApi
- [ ] CloudDirectory
- [ ] CloudFormation
- [ ] CloudFront
- [ ] CloudHSM
- [ ] CloudHSMV2
- [ ] CloudSearch
- [ ] CloudSearchDomain
- [ ] CloudTrail
- [ ] CloudWatch
- [ ] CloudWatchLogs
- [ ] CodeArtifact
- [ ] CodeBuild
- [ ] CodeCommit
- [ ] CodeDeploy
- [ ] CodeGuruProfiler
- [ ] CodeGuruReviewer
- [ ] CodePipeline
- [ ] CodeStar
- [ ] CodeStarconnections
- [ ] CodeStarNotifications
- [ ] CognitoIdentity
- [ ] CognitoIdentityProvider
- [ ] CognitoSync
- [ ] Comprehend
- [ ] ComprehendMedical
- [ ] ComputeOptimizer
- [ ] ConfigService
- [ ] Connect
- [ ] ConnectContactLens
- [ ] ConnectParticipant
- [ ] ConnectWisdomService
- [ ] CostandUsageReportService
- [ ] CostExplorer
- [ ] CustomerProfiles
- [ ] DatabaseMigrationService
- [ ] DataExchange
- [ ] DataPipeline
- [ ] DataSync
- [ ] DAX
- [ ] Detective
- [ ] DeviceFarm
- [ ] DevOpsGuru
- [ ] DirectConnect
- [ ] DirectoryService
- [ ] DLM
- [ ] DocDB
- [x] DynamoDB
- [ ] DynamoDBStreams
- [ ] EBS
- [x] EC2
- [ ] EC2InstanceConnect
- [ ] ECR
- [ ] ECRPublic
- [ ] ECS
- [ ] EFS
- [ ] EKS
- [ ] ElastiCache
- [ ] ElasticBeanstalk
- [ ] ElasticInference
- [ ] ElasticLoadBalancing
- [ ] ElasticLoadBalancingv2
- [ ] ElasticsearchService
- [ ] ElasticTranscoder
- [ ] EMR
- [ ] EMRContainers
- [ ] EventBridge
- [ ] finspace
- [ ] FinSpaceData
- [ ] Firehose
- [ ] FIS
- [ ] FMS
- [ ] ForecastQueryService
- [ ] ForecastService
- [ ] FraudDetector
- [ ] FSx
- [ ] GameLift
- [ ] Glacier
- [ ] GlobalAccelerator
- [ ] Glue
- [ ] GlueDataBrew
- [ ] Greengrass
- [ ] GreengrassV2
- [ ] GroundStation
- [ ] GuardDuty
- [ ] Health
- [ ] HealthLake
- [ ] Honeycode
- [x] IAM
- [ ] IdentityStore
- [ ] imagebuilder
- [ ] ImportExport
- [ ] Inspector
- [ ] IoT
- [ ] IoT1ClickDevicesService
- [ ] IoT1ClickProjects
- [ ] IoTAnalytics
- [ ] IoTDataPlane
- [ ] IoTDeviceAdvisor
- [ ] IoTEvents
- [ ] IoTEventsData
- [ ] IoTFleetHub
- [ ] IoTJobsDataPlane
- [ ] IoTSecureTunneling
- [ ] IoTSiteWise
- [ ] IoTThingsGraph
- [ ] IoTWireless
- [ ] IVS
- [ ] Kafka
- [ ] KafkaConnect
- [ ] kendra
- [ ] Kinesis
- [ ] KinesisAnalytics
- [ ] KinesisAnalyticsV2
- [ ] KinesisVideo
- [ ] KinesisVideoArchivedMedia
- [ ] KinesisVideoMedia
- [ ] KinesisVideoSignalingChannels
- [ ] KMS
- [ ] LakeFormation
- [x] Lambda
- [ ] LexModelBuildingService
- [ ] LexModelsV2
- [ ] LexRuntimeService
- [ ] LexRuntimeV2
- [ ] LicenseManager
- [ ] Lightsail
- [ ] LocationService
- [ ] LookoutEquipment
- [ ] LookoutforVision
- [ ] LookoutMetrics
- [ ] MachineLearning
- [ ] Macie
- [ ] Macie2
- [ ] ManagedBlockchain
- [ ] ManagedGrafana
- [ ] MarketplaceCatalog
- [ ] MarketplaceCommerceAnalytics
- [ ] MarketplaceEntitlementService
- [ ] MarketplaceMetering
- [ ] MediaConnect
- [ ] MediaConvert
- [ ] MediaLive
- [ ] MediaPackage
- [ ] MediaPackageVod
- [ ] MediaStore
- [ ] MediaStoreData
- [ ] MediaTailor
- [ ] MemoryDB
- [ ] mgn
- [ ] MigrationHub
- [ ] MigrationHubConfig
- [ ] Mobile
- [ ] MQ
- [ ] MTurk
- [ ] MWAA
- [ ] Neptune
- [ ] NetworkFirewall
- [ ] NetworkManager
- [ ] NimbleStudio
- [ ] OpenSearchService
- [ ] OpsWorks
- [ ] OpsWorksCM
- [ ] Organizations
- [ ] Outposts
- [ ] Panorama
- [ ] Personalize
- [ ] PersonalizeEvents
- [ ] PersonalizeRuntime
- [ ] PI
- [ ] Pinpoint
- [ ] PinpointEmail
- [ ] PinpointSMSVoice
- [ ] Polly
- [ ] Pricing
- [ ] PrometheusService
- [ ] Proton
- [ ] QLDB
- [ ] QLDBSession
- [ ] QuickSight
- [ ] RAM
- [ ] RDS
- [ ] RDSDataService
- [ ] Redshift
- [ ] RedshiftDataAPIService
- [ ] Rekognition
- [ ] ResilienceHub
- [ ] ResourceGroups
- [ ] ResourceGroupsTaggingAPI
- [ ] RoboMaker
- [ ] Route53
- [ ] Route53Domains
- [ ] Route53RecoveryCluster
- [ ] Route53RecoveryControlConfig
- [ ] Route53RecoveryReadiness
- [ ] Route53Resolver
- [x] S3
- [ ] S3Control
- [ ] S3Outposts
- [ ] SageMaker
- [ ] SagemakerEdgeManager
- [ ] SageMakerFeatureStoreRuntime
- [ ] SageMakerRuntime
- [ ] SavingsPlans
- [ ] Schemas
- [ ] SecretsManager
- [ ] SecurityHub
- [ ] ServerlessApplicationRepository
- [ ] ServiceCatalog
- [ ] ServiceDiscovery
- [ ] ServiceQuotas
- [ ] SES
- [ ] SESV2
- [ ] SFN
- [ ] Shield
- [ ] signer
- [ ] SimpleDB
- [ ] SMS
- [ ] Snowball
- [ ] SnowDeviceManagement
- [ ] SNS
- [x] SQS
- [ ] SSF
- [ ] SSM
- [ ] SSMContacts
- [ ] SSMIncidents
- [ ] SSO
- [ ] SSOAdmin
- [ ] SSOOIDC
- [ ] StorageGateway
- [ ] STS
- [ ] Support
- [ ] SWF
- [ ] Synthetics
- [ ] Textract
- [ ] TiAccessAnalyzer
- [ ] TimestreamQuery
- [ ] WAFRegional
- [ ] WAFV2
- [ ] WellArchitected
- [ ] WorkDocs
- [ ] WorkLink
- [ ] WorkMail
- [ ] WorkMailMessageFlow
- [ ] WorkSpaces
- [ ] XRay
