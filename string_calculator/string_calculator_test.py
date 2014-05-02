import unittest

class CalculatorTest(unittest.TestCase):
  
  def setUp(self):
    self.calculator = Calculator()

  def testAddEmptyString(self):
    self.assertEqual(0, self.calculator.add(""));

if __name__ == "__main__":
  unittest.main()
