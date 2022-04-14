from os import environ

import boto3
from flask import Blueprint, jsonify
from flask_api import status


BUCKET_NAME = environ.get("BUCKET_NAME")
AWS_ENDPOINT = environ.get("AWS_ENDPOINT")

service = Blueprint("service", __name__)


@service.route("/")
def healthcheck():
    return "Healthy", status.HTTP_200_OK


@service.route("/objects")
def list_objects():
    s3_client = boto3.client("s3", endpoint_url=AWS_ENDPOINT)
    try:
        response = s3_client.list_objects(Bucket=BUCKET_NAME)
    except Exception as exc:
        return f"Error: {exc}", status.HTTP_500_INTERNAL_SERVER_ERROR
    return jsonify(response.get("Contents", {})), status.HTTP_200_OK
