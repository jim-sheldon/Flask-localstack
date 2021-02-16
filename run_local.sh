#!/bin/bash

set -eo pipefail

function cleanup() {
  docker-compose stop
  docker-compose down -v
}

trap cleanup EXIT

docker-compose up -d --build

read -n1 -rsp $"Press a key to exit\n"
