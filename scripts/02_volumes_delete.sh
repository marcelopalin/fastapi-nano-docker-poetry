#!/bin/zsh
# Atencao: somente utilize este script se souber o que esta fazendo
# ele eliminará todos os dados dos seus containers.
echo "Remove VOLUME COM OS DADOS dos BDs, LIMPEZA GERAL!!"
echo "Você deve PARAR (STOP) todos os containers antes!"
docker system prune -af --volumes
