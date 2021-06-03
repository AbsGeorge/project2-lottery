from flask import url_for
from flask_testing import TestCase
import requests_mock 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        
        response = self.client.post(url_for('/'))
        self.assertEqual(response.data.decode(), entry = ["entry"],
        lotterynumber = ["number"],
        lotteryalpha = ["alphabet"])