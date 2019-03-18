#!/usr/bin/env bash
make clean

set -e
echo "Running test scripts"
eval $(docker-machine env -u)
make test

echo "deploying"
eval $(docker-machine env brb-prod)
echo "docker machine configured"
echo "building"
docker-compose -f production.yml up --build -d

echo "deployed successfully"
echo "resetting docker-machine config"
eval $(docker-machine env -u)
