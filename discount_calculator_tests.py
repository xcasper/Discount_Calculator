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

    def test_five_dollar_discount(self):
        discount_calculator = Discount_Calculator()
        result = discount_calculator.calculate(250, 5, 'absolute')
        self.assertEqual(5, result)

    def test_invalid_discount_type(self):
        discount_calculator = Discount_Calculator()
        self.assertRaises(ValueError, discount_calculator.calculate, 250, 5, 'random')
         
    def floating_point_percentage_discount_test(self):
        discount_calculator = Discount_Calculator()
        result = discount_calculator.calculate(100.0, 10.0, 'percent')
        self.assertEqual(10.0, result)
        
    def floating_point_absolute_discount_test(self):
        discount_calculator = Discount_Calculator()
        result = discount_calculator.calculate(250.0, 5.0, 'absolute')
        self.assertEqual(5.0, result)
