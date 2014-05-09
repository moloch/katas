import unittest
from roman_numerals import RomanNumber

class RomanNumeralsTest(unittest.TestCase):
  
  def testConvertOneFromDecimalToRoman(self):
    self.__decimalToRoman("I", 1)

  def testConvertTwoFromDecimalToRoman(self):
    self.__decimalToRoman("II", 2)

  def testConvertThreeFromDecimalToRoman(self):
    self.__decimalToRoman("III", 3)

  def testConvertFourFromDecimalToRoman(self):
    self.__decimalToRoman("IV", 4)

  def testConvertFiveFromDecimalToRoman(self):
    self.__decimalToRoman("V", 5)

  def testConvertFromSixToEightFromDecimalToRoman(self):
    self.__decimalToRoman("VI", 6)
    self.__decimalToRoman("VII", 7)
    self.__decimalToRoman("VIII", 8)

  def testConvertNineFromDecimalToRoman(self):
    self.__decimalToRoman("IX", 9)

  def testConvertFromTenToNineteenFromDecimalToRoman(self):
    self.__decimalToRoman("X", 10)
    self.__decimalToRoman("XI", 11)
    self.__decimalToRoman("XII", 12)
    self.__decimalToRoman("XIII", 13)
    self.__decimalToRoman("XIV", 14)
    self.__decimalToRoman("XV", 15)
    self.__decimalToRoman("XVI", 16)
    self.__decimalToRoman("XVII", 17)
    self.__decimalToRoman("XVIII", 18)
    self.__decimalToRoman("XIX",19)

  def testConvertFromTwentyToTwentyNineFromDecimalToRoman(self):
    self.__decimalToRoman("XX", 20)
    self.__decimalToRoman("XXI", 21)
    self.__decimalToRoman("XXII", 22)
    self.__decimalToRoman("XXIII", 23)
    self.__decimalToRoman("XXIV", 24)
    self.__decimalToRoman("XXV", 25)
    self.__decimalToRoman("XXVI", 26)
    self.__decimalToRoman("XXVII", 27)
    self.__decimalToRoman("XXVIII", 28)
    self.__decimalToRoman("XXIX",29)

  def __decimalToRoman(self, roman, decimal):
    self.assertEqual(roman, RomanNumber(decimal).get_roman_value())
    

if __name__ == '__main__':
  unittest.main()
