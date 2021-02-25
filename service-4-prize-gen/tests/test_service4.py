from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService4(TestCase):
    def get_char_gen(self):
        with patch('requests.post') as g:
            g.return_value.text = "AAA9992123"
            response = self.client.get(url_for('prize'))
            self.assertIn(b'Boat', response.data)
