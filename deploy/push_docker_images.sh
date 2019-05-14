#!/usr/bin/env bash
# Django
docker build . -f ./compose/production/django/Dockerfile -t lmsutton/brb_swarm_django:latest
docker push lmsutton/brb_swarm_django:latest

# Postgres
docker build . -f ./compose/production/postgres/Dockerfile -t lmsutton/brb_swarm_db:latest
docker push lmsutton/brb_swarm_db:latest

# nginx
docker build . -f ./compose/production/nginx/Dockerfile -t lmsutton/brb_swarm_nginx:latest
docker push lmsutton/brb_swarm_nginx:latest
