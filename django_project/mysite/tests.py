import os

from django import test
from django.conf import settings


class TestSettings(test.TestCase):

    def test_something(self):
        print(os.getenv('DEBUG'))
        print(os.getenv('SITENAME'))
