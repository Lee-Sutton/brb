#!/usr/bin/env bash
if [ -z "$TOKEN" ]; then
    echo "Missing required token"
    echo "Set digital ocean token export TOKEN='...'"
else
    echo "Token set"
    echo $TOKEN
    docker-machine create \
    -d digitalocean \
    --digitalocean-access-token=$TOKEN \
    brb-prod
fi

