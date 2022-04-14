from unittest import TestCase

from flask import Flask
from flask_api import status

from service import create_app


EXPECTED_OBJECTS = ["buckethead.jpg", "nunchucks.gif", "robot.gif"]


class TestHandlers(TestCase):

    def test_health_check(self):
        app = create_app()
        app.config["TESTING"] = True
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
        
    def test_list_objects(self):
        app = create_app()
        app.config["TESTING"] = True
        with app.test_client() as client:
            resp = client.get("/objects")
            s3_objects = [obj["Key"] for obj in resp.json]
            for obj in EXPECTED_OBJECTS:
                self.assertIn(obj, s3_objects)
