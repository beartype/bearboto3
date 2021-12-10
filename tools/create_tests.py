#!/usr/bin/env python3

import argparse
import json
import os
import random
from pathlib import Path

import black
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(
    description="Generates test cases from a service class data file"
)
parser.add_argument(
    "--service",
    type=str,
    required=True,
    help="Service to load data from and create tests for",
)
args = parser.parse_args()

DATA_FOLDER = "data"
RESOURCES_KEY = "resources"
DATA_FILE_NAME = f"{args.service}_data.json"
UTF_8 = "utf-8"
READ = "r"
WRITE = "w"
TEMPLATE_FOLDER = "templates"
TEMPLATE_FILE_NAME = "tests.py.j2"
TEST_FOLDER = "tests"
TEST_FILE_NAME_PREFIX = f"test_{args.service}"

here = Path(__file__).parent


def get_random_service():
    # Since the random service may also need to provide a service resource,
    # It's easier to just hard-code the available ones here as they come up.
    services = ["s3", "ec2", "dynamodb"]
    not_this_service = [item for item in services if item != args.service]
    return random.choice(not_this_service)


def map_fixtures(items):
    for item in items:
        not_this_item = [other for other in items if other is not item]
        # Some services (like dynamodb), only have 1 resource. Therefore, we must add the fail fixture by hand from another service.
        random_item = (
            random.choice(not_this_item) if not_this_item else {"fixture_name": ""}
        )
        item["fail_fixture_name"] = random_item["fixture_name"]


def create_tests(category, items, folder):
    output_file = folder.joinpath(f"{TEST_FILE_NAME_PREFIX}_{category}.py")
    with output_file.open(WRITE, encoding=UTF_8) as file:
        template.stream(service=args.service, items=items).dump(file)

    black.format_file_in_place(
        output_file, fast=False, write_back=black.WriteBack.YES, mode=black.FileMode()
    )


templates_folder = here.parent.joinpath(TEMPLATE_FOLDER)
env = Environment(loader=FileSystemLoader(templates_folder))
template = env.get_template(TEMPLATE_FILE_NAME)

data_folder = here.parent.joinpath(DATA_FOLDER)
data_file = data_folder.joinpath(DATA_FILE_NAME)
with data_file.open(READ, encoding=UTF_8) as file:
    data = json.load(file)

HAS_RESOURCES = RESOURCES_KEY in data

output_folder = here.parent.joinpath(TEST_FOLDER).joinpath(args.service)
output_folder.mkdir(parents=True, exist_ok=True)

# Handle clients
random_service = get_random_service()
data["client"]["fail_fixture_name"] = data["client"]["fixture_name"].replace(
    args.service, random_service
)
items = [data["client"]]

if HAS_RESOURCES:
    data["service_resource"]["fail_fixture_name"] = data["service_resource"][
        "fixture_name"
    ].replace(args.service, random_service)
    items.append(data["service_resource"])
create_tests("clients", items, output_folder)

# Handle other classes
categories = ["waiters", "paginators"]
if HAS_RESOURCES:
    categories += ["resources", "collections"]

for category in categories:
    items = data[category]
    map_fixtures(items)
    create_tests(category, items, output_folder)
