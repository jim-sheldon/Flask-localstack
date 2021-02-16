from flask import Blueprint
from flask_api import status


service = Blueprint("service", __name__)


@service.route("/")
def healthcheck():
    return "Healthy", status.HTTP_200_OK
