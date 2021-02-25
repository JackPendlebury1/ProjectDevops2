from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService3(TestCase):
    def get_char_gen(self):
        with patch('requests.get') as g:
            g.return_value.text = "9992123"
            response = self.client.get(url_for('numgen'))
            self.assertIn(b'9992123', response.data)
