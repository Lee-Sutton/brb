eval $(docker-machine env node-1)
docker stack ps -f "desired-state=running" django
docker service logs django_django
