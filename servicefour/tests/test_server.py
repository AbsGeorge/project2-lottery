from flask.helpers import url_for
from flask_testing import TestCase
import requests
import json

from servicefour.app import app, db, WinningNumbers

class TestBase(TestCase):
    def create_app(self):
        return app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                DEBUG=True,        
            )
        return app

    def setUp(self):
        db.create_all()
        

    def tearDown(self):
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        info = dict(number="12345", alphabet="ab", entry="12345ab")
        response = self.client.post(url_for('home'), json=info)       
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "You have won £5 million")