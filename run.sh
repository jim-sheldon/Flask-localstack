#!/bin/bash

set -eou pipefail

if [ "$ENVIRONMENT" == "local" ] ; then
  ./setup_s3.sh
fi

./wsgi.py
