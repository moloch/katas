import unittest
from roman_numerals import RomanNumber

class RomanNumeralsTest(unittest.TestCase):
  
  def testConvertOneFromDecimalToRoman(self):
    self.assertEqual("I", RomanNumber(1).get_roman_value())

if __name__ == '__main__':
  unittest.main()
