#!/usr/bin/env bash
if [ -z "$TOKEN" ]; then
    echo "Missing required token"
    echo "Set digital ocean token export TOKEN='...'"
else
    echo "Token set"
    echo $TOKEN
    for i in 1 2 3 4; do
        docker-machine create \
          --digitalocean-region "nyc1" \
          --driver digitalocean \
          --digitalocean-size "1gb" \
          --digitalocean-access-token $TOKEN \
          node-$i;
    done
fi
