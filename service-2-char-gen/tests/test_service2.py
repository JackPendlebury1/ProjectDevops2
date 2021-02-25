from unittest.mock import patch
from flask import url_for 
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService2(TestCase):
    def get_char_gen(self):
        with patch('requests.get') as g:
            g.return_value.text = "AAA"
            response = self.client.get(url_for('chargen'))
            self.assertIn(b'AAA', response.data)
