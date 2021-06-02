from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch 

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_number(self):
        with patch('random.randint') as r:
            r.return_value = 'cow'

#def test_number_is_between_1 _and_50(self):
#self.assertTrue(self.a >=1 and self.a <= 50)


            response = self.client.get(url_for('get_lotterynumbers'))
            self.assertEqual(response.status_code, 200)
    
        