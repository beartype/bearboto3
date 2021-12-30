#!/bin/bash

versions=('3.7' '3.8' '3.9' '3.10')

for version in "${versions[@]}"; do
image_name="wuubb/bearboto3:$version"
docker build --tag "$image_name" --build-arg PYTHON_VERSION="$version" .
docker push "$image_name"
done