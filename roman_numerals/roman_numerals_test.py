import unittest
from roman_numerals import RomanNumber

class RomanNumeralsTest(unittest.TestCase):
  
  def testConvertOneFromDecimalToRoman(self):
    self.assertEqual("I", RomanNumber(1).get_roman_value())

  def testConvertTwoFromDecimalToRoman(self):
    self.assertEqual("II", RomanNumber(2).get_roman_value())

  def testConvertThreeFromDecimalToRoman(self):
    self.assertEqual("III", RomanNumber(3).get_roman_value())

  def testConvertFourFromDecimalToRoman(self):
    self.assertEqual("IV", RomanNumber(4).get_roman_value())

if __name__ == '__main__':
  unittest.main()
