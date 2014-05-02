import unittest
from string_calculator import Calculator

class CalculatorTest(unittest.TestCase):
  
  def setUp(self):
    self.calculator = Calculator()

  def testAddEmptyString(self):
    self.assertEqual(0, self.calculator.add(""))

  def testAddOne(self):
    self.assertEqual(1, self.calculator.add("1"))

  def testAddTwoNumbers(self):
    self.assertEqual(5, self.calculator.add("3,2"))

if __name__ == "__main__":
  unittest.main()