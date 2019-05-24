#! /bin/bash

# docker-compose down --volume
docker-compose down --volumes
rm -rf ./docker/data
mkdir ./docker/data -p
docker-compose up --force-recreate --build
