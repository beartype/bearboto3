#!/usr/bin/env python3

import argparse
import json
import keyword
from pathlib import Path

import black
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(
    description="Loads service class data and generates pytest fixtures for use in tests"
)
parser.add_argument(
    "--service",
    type=str,
    required=True,
    help="Service to load data from and create test fixtures for",
)
args = parser.parse_args()

DATA_FOLDER = "data"
DATA_FILE_NAME = f"{args.service}_data.json"
UTF_8 = "utf-8"
READ = "r"
WRITE = "w"
TEMPLATE_FOLDER = "templates"
TEMPLATE_FILE_NAME = "fixtures.py.j2"
TEST_FOLDER = "tests"
SAFE_SERVICE_NAME = (
    f"{args.service}_" if keyword.iskeyword(args.service) else args.service
)
FIXTURES_FILE_NAME = f"{args.service}_fixtures.py"

here = Path(__file__).parent

templates_folder = here.parent.joinpath(TEMPLATE_FOLDER)
env = Environment(loader=FileSystemLoader(templates_folder))
template = env.get_template(TEMPLATE_FILE_NAME)

data_folder = here.parent.joinpath(DATA_FOLDER)
data_file = data_folder.joinpath(DATA_FILE_NAME)
with data_file.open(READ, encoding=UTF_8) as file:
    data = json.load(file)

HAS_RESOURCES = "resources" in data
HAS_WAITERS = "waiters" in data
HAS_PAGINATORS = "paginators" in data

kwargs = {
    "has_resources": HAS_RESOURCES,
    "has_waiters": HAS_WAITERS,
    "has_paginators": HAS_PAGINATORS,
    "client_fixture_name": data["client"]["fixture_name"],
    "service": args.service,
}

if HAS_WAITERS:
    kwargs["waiters"] = data["waiters"]
if HAS_PAGINATORS:
    kwargs["paginators"] = data["paginators"]
if HAS_RESOURCES:
    kwargs["service_resource_fixture_name"] = data["service_resource"]["fixture_name"]
    kwargs["resources"] = data["resources"]
    kwargs["collections"] = data["collections"]


output_folder = here.parent.joinpath(TEST_FOLDER).joinpath(SAFE_SERVICE_NAME)
output_folder.mkdir(parents=True, exist_ok=True)
output_file = output_folder.joinpath(FIXTURES_FILE_NAME)

with output_file.open(WRITE, encoding=UTF_8) as file:
    template.stream(**kwargs).dump(file)

black.format_file_in_place(
    output_file, fast=False, write_back=black.WriteBack.YES, mode=black.FileMode()
)
