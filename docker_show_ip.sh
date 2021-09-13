#!/bin/zsh
echo "Mostrando o IP do Containers"
for container_name in $(docker ps --format '{{.Names}}')
do
IPCONTAINER=`docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container_name`
echo "Docker Container IP from \"$container_name\" is $IPCONTAINER."
done
