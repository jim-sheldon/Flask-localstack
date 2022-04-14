#!/bin/bash

set -eou pipefail

echo "Waiting for S3 at ${AWS_ENDPOINT}/health, checking every 5s"
until $(curl --silent --fail ${AWS_ENDPOINT}/health | grep "\"s3\": \"available\"" > /dev/null); do
  echo "Waiting 5s"
  sleep 5
done

echo "S3 ready"
echo "Creating bucket"
aws --endpoint-url=${AWS_ENDPOINT} configure set default.s3.addressing_style path
aws --endpoint-url=${AWS_ENDPOINT} s3 mb s3://${BUCKET_NAME}
aws --endpoint-url=${AWS_ENDPOINT} s3api put-bucket-acl --bucket ${BUCKET_NAME} --acl public-read

echo "Done creating S3 bucket"


echo "Uploading files to S3 bucket"

aws --endpoint-url=${AWS_ENDPOINT} s3 cp buckethead.jpg s3://${BUCKET_NAME}
aws --endpoint-url=${AWS_ENDPOINT} s3 cp nunchucks.gif s3://${BUCKET_NAME}
aws --endpoint-url=${AWS_ENDPOINT} s3 cp robot.gif s3://${BUCKET_NAME}

echo "Done uploading files to bucket"