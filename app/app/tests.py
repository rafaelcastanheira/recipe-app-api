"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    Test the calc module
    """

    def test_add_numbers(self):
        """
        Test the add function
        """
        self.assertEqual(calc.add(1, 2), 3)

    def test_subtract_numbers(self):
        """
        Test the subtract function
        """
        self.assertEqual(calc.subtract(1, 2), -1)
