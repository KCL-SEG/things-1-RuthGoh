from django.test import TestCase
from .models import Thing
from django.core.exceptions import ValidationError

class ThingTestCase(TestCase):
    def setUp(self):
        self.t1 = Thing(
            name='t1',
            description='the first thing',
            quantity=3,
        )
        self.t1.full_clean()

    def test_description_at_120_chars(self):
        self.t1.description='x' * 120
        try:
            self.t1.full_clean()
        except ValidationError:
            self.fail('Test user is invalid.')

    def test_description_max_120_chars(self):
        self.t1.description='x' * 121
        with self.assertRaises(ValidationError):
                self.t1.full_clean()
