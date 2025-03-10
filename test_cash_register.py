# test_cash_register.py

import unittest
from cash_register import change

class TestCashRegister(unittest.TestCase):

    def test_exact_change(self):
        self.assertEqual(change(2000, 2000), {})  # No change needed

    def test_simple_change(self):
        self.assertEqual(change(1500, 2000), {500: 1})  # 1 x $5

    def test_multiple_denominations(self):
        self.assertEqual(change(1230, 2000), {500: 1, 200: 3, 50: 1})  # 1 x $5, 3 x $2, 1 x $0.50

    def test_large_change(self):
        self.assertEqual(change(1000, 5000), {2000: 2})  # 2 x $20

    def test_invalid_payment(self):
        with self.assertRaises(ValueError):
            change(2000, 1500)  # Should raise an error

    def test_no_change(self):
        self.assertEqual(change(1000, 1000), {})  # No change needed

if __name__ == '__main__':
    unittest.main()