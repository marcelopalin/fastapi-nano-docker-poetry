#!/bin/sh

set -e

CURRENT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
BASE_DIR="$(dirname "$CURRENT_DIR")"

echo "CURRENT_DIR: $CURRENT_DIR"
echo "BASE_DIR: $BASE_DIR"
cd $CURRENT_DIR

docker run -d -p 5000:8000 --rm fastapi-nano
echo "Acesse: http://localhost:5000"