import unittest
from kata09_back_to_checkout import Checkout

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(210, Checkout.calculateTotal("AAABBCD"))
        self.assertEqual(50, Checkout.calculateTotal("A"))
        self.assertEqual(45, Checkout.calculateTotal("BB"))