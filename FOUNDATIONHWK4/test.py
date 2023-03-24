import unittest
from shop import shop_simulator, InsufficientFundsError, MaxPurchaseAttemptsError

class TestShop(unittest.TestCase):
    def test_valid_item_purchase(self):
        result = shop_simulator(110)
        self.assertEqual(result, "Here's your item3!")

     def test_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            shop_simulator(50)

    def test_max_attempts(self):
        with self.assertRaises(MaxPurchaseAttemptsError):
            shop_simulator(300)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            shop_simulator('abc')

    def test_add_balance(self):
        result = shop_simulator(120, add_balance=50)
        self.assertEqual(result, "Here's your item3!")
