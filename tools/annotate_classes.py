#!/usr/bin/env python3

import argparse
import json
import keyword
from operator import itemgetter
from pathlib import Path

import black
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(
    description="Automatically annotates classes for a given service"
)
parser.add_argument(
    "--service",
    type=str,
    required=True,
    help='Service to load data from and annotate classes"',
)
args = parser.parse_args()

DATA_FOLDER = "data"
DATA_FILE_NAME = f"{args.service}_data.json"
UTF_8 = "utf-8"
READ = "r"
WRITE = "w"
TEMPLATE_FOLDER = "templates"
TEMPLATE_FILE_NAME = "annotations.py.j2"
SAFE_SERVICE_NAME = (
    f"{args.service}_" if keyword.iskeyword(args.service) else args.service
)
CLASSES_FILE_NAME = f"{SAFE_SERVICE_NAME}.py"


here = Path(__file__).parent

templates_folder = here.parent.joinpath(TEMPLATE_FOLDER)
env = Environment(
    loader=FileSystemLoader(templates_folder), trim_blocks=True, lstrip_blocks=True
)
template = env.get_template(TEMPLATE_FILE_NAME)

data_folder = here.parent.joinpath(DATA_FOLDER)
data_file = data_folder.joinpath(DATA_FILE_NAME)
with data_file.open(READ, encoding=UTF_8) as file:
    data = json.load(file)

HAS_RESOURCES = "resources" in data
HAS_WAITERS = "waiters" in data
HAS_PAGINATORS = "paginators" in data


client_types = [data["client"]["stub_class"]]
if HAS_PAGINATORS:
    client_types += [item["stub_class"] for item in data["paginators"]]
if HAS_WAITERS:
    client_types += [item["stub_class"] for item in data["waiters"]]

if HAS_RESOURCES:
    resource_types = (
        [data["service_resource"]["stub_class"]]
        + [item["stub_class"] for item in data["resources"]]
        + [item["stub_class"] for item in data["collections"]]
    )


items = [data["client"]]
if HAS_WAITERS:
    items += data["waiters"]
if HAS_PAGINATORS:
    items += data["paginators"]
if HAS_RESOURCES:
    items += data["resources"]
    items += data["collections"]
    items.append(data["service_resource"])


kwargs = {
    "classes": sorted(items, key=itemgetter("stub_class")),
    "service": args.service,
    "client_types": sorted(client_types),
    "has_resources": HAS_RESOURCES,
}
if HAS_RESOURCES:
    kwargs["resource_types"] = sorted(resource_types)

output_file = here.parent.joinpath("bearboto3").joinpath(CLASSES_FILE_NAME)
with output_file.open(WRITE, encoding=UTF_8) as file:
    template.stream(**kwargs).dump(file)

black.format_file_in_place(
    output_file, fast=False, write_back=black.WriteBack.YES, mode=black.FileMode()
)
