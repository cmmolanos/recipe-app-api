from django.test import SimpleTestCase

from app import calc


class ClassTests(SimpleTestCase):
    """class"""
    def test_add_numbers(self):
        """test numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
