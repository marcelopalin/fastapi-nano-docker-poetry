#!/bin/zsh
echo "Parando todos os containers da máquina"
LST_CONTAINER=`$(docker ps --format '{{.Names}}')`
if [ -z "$LST_CONTAINER"]
then
    echo "Nenhum container encontrado!"
fi

for container_name in $(docker ps --format '{{.Names}}')
do
    echo "STOP container: $container_name"
    docker container stop $container_name
done
