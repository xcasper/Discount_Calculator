import unittest
from discount_calculator import Discount_Calculator

class DiscountCalculatorTests(unittest.TestCase):
    def test_10_percentage_discount(self):
        discount_calculator = Discount_Calculator()
        result = discount_calculator.calculate(100, 10, 'percent')
        self.assertEqual(10.0, result)
    def test_15_percentage_discount(self):
        discount_calculator = Discount_Calculator()
        result = discount_calculator.calculate(100, 15, 'percent')
        self.assertEqual(15.0, result)
    
    
