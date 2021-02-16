#!/bin/bash

set -eou pipefail

if [ "$ENVIRONMENT" == "local" ] ; then
  ./setup_s3.sh
fi

coverage run -m unittest -v
coverage report -m
python -m pycodestyle ./service/
python -m flake8 ./service/
lizard -C 5 -a 3 -w ./service/
echo "Tests and code quality checks passed"
