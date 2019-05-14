eval $(docker-machine env node-1)
docker stack ps django
docker service logs django_nginx
