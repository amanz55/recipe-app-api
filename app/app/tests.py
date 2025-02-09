"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    # Test the add function

    def test_add_numbers(self):
        # Test that 3 + 8 = 11
        res = calc.add(3, 8)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        # Test that 5 - 11 = -6
        res = calc.subtract(5, 11)

        self.assertEqual(res, -6)