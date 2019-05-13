#!/usr/bin/env bash
for i in 2 3 4; do
    docker-machine ssh node-$i \
      -- docker swarm join --token SWMTKN-1-35pth04mfabscdg5jdbmxzsgfibkryp1wdknqo0gdvfdcxrnz3-1iumk4jigl6kgfbs1izy58eh6 104.248.49.196:2377
done
