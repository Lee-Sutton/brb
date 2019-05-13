#!/usr/bin/env bash
eval $(docker-machine env node-1)
docker stack deploy --compose-file=production.yml django
