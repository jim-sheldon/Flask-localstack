from unittest import TestCase

from flask import Flask
from flask_api import status

from service import create_app


class TestWSGI(TestCase):

    def test_health_check(self):
        app = create_app()
        app.config["TESTING"] = True
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(status.HTTP_200_OK, resp.status_code)
        
