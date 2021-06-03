from flask_testing import TestCase
import requests_mock
from flask import url_for

 


from serviceone.app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY="TEST_SECRET_KEY",
                DEBUG=True, 
                WTF_CSRF_ENABLED=False
            )
        return app

    


class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://lottery_number_api:5000/get_lotterynumbers', text = "67891")
            mocker.get('http://lottery_alpha_api:5000/get_lotteryalpha', text = "cd")
            mocker.post('http://results_api:5000/', text = "You did not win this time")
            
            response = self.client.post(url_for('results'),data=dict(
                lottery_numbers = "12345",
                lottery_alphabets = "ab"
            ))
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"You did not win this time", response.data)
                