from flask import url_for
from flask_testing import TestCase
from servicethree.app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_alpha(self):
        for i in range(5):
            response = self.client.get(url_for('lotteryalphabets'))
            for char in response.data.decode("utf-8"):
                self.assertIn(str(char), "abcdefghijklmnopqrstuvwxyz")
    
        