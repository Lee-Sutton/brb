#!/usr/bin/env bash
eval $(docker-machine env brb-prod)
docker-compose -f production.yml logs
