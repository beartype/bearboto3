#!/usr/bin/env python3

import argparse
import inspect
import json
import os
from pathlib import Path
from typing import Dict, List

import boto3
import botocore
from botocore import xform_name

parser = argparse.ArgumentParser(
    description="Gathers data needed for annotating classes and generating test cases by parsing the boto JSON schema."
)
parser.add_argument(
    "--service",
    type=str,
    required=True,
    help="Service name (lowercase) to annotate classes for",
)
args = parser.parse_args()

UTF_8 = "utf-8"
DATA_FOLDER = "data"
COLLECTION_SUFFIX = "Collection"
COLLECTIONS_KEY = "hasMany"
RESOURCE_BASE_CLASS = "ServiceResource"
COLLECTION_BASE_CLASS = "ResourceCollection"
PAGINATOR_BASE_CLASS = "Paginator"
WAITER_BASE_CLASS = "Waiter"
CLIENT_BASE_CLASS = "BaseClient"
RESOURCES_FILE_NAME = "resources-1.json"
PAGINATORS_FILE_NAME = "paginators-1.json"
WAITERS_FILE_NAME = "waiters-2.json"
READ = "r"
WRITE = "w"
SERVICE_MODEL_FILE_NAME = "service-2.json"
CONSTRUCTOR_ARGS_KEY = "identifiers"
DATA_FILE_NAME = f"{args.service}_data.json"


def get_latest_version(folder: Path) -> Path:
    folders = os.listdir(folder.resolve())
    latest_version = max(folders)
    return folder.joinpath(latest_version)


here = Path(__file__).parent
boto3_path = Path(inspect.getfile(boto3)).parent
botocore_path = Path(inspect.getfile(botocore)).parent


resource_data_folder = boto3_path.joinpath(DATA_FOLDER).joinpath(args.service)
client_data_folder = botocore_path.joinpath(DATA_FOLDER).joinpath(args.service)

schema_folder = get_latest_version(client_data_folder)

service_model_file = schema_folder.joinpath(SERVICE_MODEL_FILE_NAME)
with service_model_file.open(READ, encoding=UTF_8) as file:
    service_model = json.load(file)

SERVICE_ABBREVIATION = service_model["metadata"]["serviceId"]
SERVICE_ABBREVIATION_LOWER = SERVICE_ABBREVIATION.lower()


def get_waiters(folder: Path) -> List[Dict[str, str]]:
    waiters_file = folder.joinpath(WAITERS_FILE_NAME)
    with waiters_file.open(READ, encoding=UTF_8) as file:
        waiters_json = json.load(file)

    return [
        {
            "stub_class": f"{waiter}{WAITER_BASE_CLASS}",
            "boto_class": f"{SERVICE_ABBREVIATION}.{WAITER_BASE_CLASS}.{waiter}",
            "base_class": WAITER_BASE_CLASS,
            "fixture_name": f"gen_{xform_name(waiter)}_waiter",
            "snake_name": xform_name(waiter),
        }
        for waiter in waiters_json["waiters"]
    ]


def get_paginators(folder: Path) -> List[Dict[str, str]]:
    paginators_file = folder.joinpath(PAGINATORS_FILE_NAME)
    with paginators_file.open(READ, encoding=UTF_8) as file:
        paginators_json = json.load(file)

    return [
        {
            "stub_class": f"{paginator}{PAGINATOR_BASE_CLASS}",
            "boto_class": f"{SERVICE_ABBREVIATION}.{PAGINATOR_BASE_CLASS}.{paginator}",
            "base_class": PAGINATOR_BASE_CLASS,
            "fixture_name": f"gen_{xform_name(paginator)}_paginator",
            "snake_name": xform_name(paginator),
        }
        for paginator in paginators_json["pagination"]
    ]


def get_collections(
    resource_definition: Dict, parent: Dict[str, str]
) -> List[Dict[str, str]]:
    return [
        {
            "stub_class": f"{parent['stub_class']}{collection}{COLLECTION_SUFFIX}",
            "boto_class": f"{SERVICE_ABBREVIATION_LOWER}.{parent['stub_class']}.{xform_name(collection)}{COLLECTION_SUFFIX}",
            "base_class": COLLECTION_BASE_CLASS,
            "fixture_name": f"gen_{parent['snake_name']}_{xform_name(collection)}_collection",
            "snake_name": xform_name(collection),
            "parent_fixture_name": parent["fixture_name"],
        }
        for collection in resource_definition["hasMany"]
    ]


def get_resource(key: str, resource_definition: Dict) -> tuple:
    num_constructor_args = (
        len(resource_definition[CONSTRUCTOR_ARGS_KEY])
        if CONSTRUCTOR_ARGS_KEY in resource_definition
        else 0
    )

    # Handle the resource object
    item = {
        "stub_class": key,
        "boto_class": f"{SERVICE_ABBREVIATION_LOWER}.{key}",
        "base_class": RESOURCE_BASE_CLASS,
        "fixture_name": f"gen_{xform_name(key)}",
        "snake_name": xform_name(key),
        "constructor_args": ",".join(
            ["random_str()" for _ in range(num_constructor_args)]
        ),
    }

    # Handle any collections that are part of this resource
    collections = []
    if COLLECTIONS_KEY in resource_definition:
        collections = get_collections(resource_definition, item)

    return item, collections


def get_resources(folder: Path) -> Dict:
    resources_file = folder.joinpath(RESOURCES_FILE_NAME)
    with resources_file.open(READ, encoding=UTF_8) as file:
        resources_json = json.load(file)

    # Handle service resource
    result = {
        "service_resource": {
            "stub_class": f"{SERVICE_ABBREVIATION}{RESOURCE_BASE_CLASS}",
            "boto_class": f"{SERVICE_ABBREVIATION_LOWER}.{RESOURCE_BASE_CLASS}",
            "base_class": RESOURCE_BASE_CLASS,
            "fixture_name": f"gen_{SERVICE_ABBREVIATION_LOWER}_resource",
            "snake_name": f"{SERVICE_ABBREVIATION_LOWER}_resource",
        },
        "collections": [],
        "resources": [],
    }

    # Handle any collections that are part of the service resource
    service_resource_definition = resources_json["service"]
    if COLLECTIONS_KEY in service_resource_definition:
        result["collections"] += [
            {
                "stub_class": f"{RESOURCE_BASE_CLASS}{collection}{COLLECTION_SUFFIX}",
                "boto_class": f"{SERVICE_ABBREVIATION_LOWER}.{xform_name(collection)}{COLLECTION_SUFFIX}",
                "base_class": COLLECTION_BASE_CLASS,
                "fixture_name": f"gen_service_resource_{xform_name(collection)}_collection",
                "snake_name": xform_name(collection),
                "parent_fixture_name": result["service_resource"]["fixture_name"],
            }
            for collection in service_resource_definition["hasMany"]
        ]

    # Handle resources and any collections they may have
    for key, val in resources_json["resources"].items():
        item, collections = get_resource(key, val)
        result["resources"].append(item)
        result["collections"] += collections

    return result


HAS_RESOURCES = resource_data_folder.exists()
data = {
    "client": {
        "stub_class": f"{SERVICE_ABBREVIATION}Client",
        "boto_class": SERVICE_ABBREVIATION,
        "base_class": CLIENT_BASE_CLASS,
        "fixture_name": f"gen_{SERVICE_ABBREVIATION_LOWER}_client",
        "snake_name": f"{SERVICE_ABBREVIATION_LOWER}_client",
    },
    "paginators": [],
    "waiters": [],
}


data["paginators"] += get_paginators(schema_folder)
data["waiters"] += get_waiters(schema_folder)

if HAS_RESOURCES:
    schema_folder = get_latest_version(resource_data_folder)
    data.update(get_resources(schema_folder))

output_folder = here.parent.joinpath(DATA_FOLDER)
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder.joinpath(DATA_FILE_NAME)
with output_file.open(WRITE, encoding=UTF_8) as file:
    json.dump(data, file)
