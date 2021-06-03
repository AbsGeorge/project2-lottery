from flask import url_for
from flask_testing import TestCase
from servicetwo.app import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_number(self):
        for i in range(1,6):
            response = self.client.get(url_for('lotterynumbers'))
            for number in response.data.decode():
                self.assertIn(int(number), range(0,10))

            

    
        