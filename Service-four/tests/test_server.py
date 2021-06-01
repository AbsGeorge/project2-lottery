rom flask import url_for
from flask_testing import TestCase
import requests_mock 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get
            mocker.post
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)