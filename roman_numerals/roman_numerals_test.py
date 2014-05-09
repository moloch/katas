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

  def testConvertFromThirtyToThirtyNineFromDecimalToRoman(self):
    self.__decimalToRoman("XXX", 30)
    self.__decimalToRoman("XXXI", 31)
    self.__decimalToRoman("XXXII", 32)
    self.__decimalToRoman("XXXIII", 33)
    self.__decimalToRoman("XXXIV", 34)
    self.__decimalToRoman("XXXV", 35)
    self.__decimalToRoman("XXXVI", 36)
    self.__decimalToRoman("XXXVII", 37)
    self.__decimalToRoman("XXXVIII", 38)
    self.__decimalToRoman("XXXIX",39)
  
  def testConvertFromFourtyToFourtyNineFromDecimalToRoman(self):
    self.__decimalToRoman("XL", 40)
    self.__decimalToRoman("XLI", 41)
    self.__decimalToRoman("XLII", 42)
    self.__decimalToRoman("XLIII", 43)
    self.__decimalToRoman("XLIV", 44)
    self.__decimalToRoman("XLV", 45)
    self.__decimalToRoman("XLVI", 46)
    self.__decimalToRoman("XLVII", 47)
    self.__decimalToRoman("XLVIII", 48)
    self.__decimalToRoman("XLIX",49)

  def testConvertNumbersBetweenFiftyAndNinetyNine(self):
    self.__decimalToRoman("L", 50)
    self.__decimalToRoman("LIV", 54)
    self.__decimalToRoman("LXXIX", 79)

  def __decimalToRoman(self, roman, decimal):
    self.assertEqual(roman, RomanNumber(decimal).get_roman_value())
    

if __name__ == '__main__':
  unittest.main()
