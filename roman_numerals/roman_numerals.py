from collections import OrderedDict

class RomanNumber():

  def __init__(self, value):
    self.value = value
    self.numerals = OrderedDict([(50,'L'),(10, 'X'),(5, 'V'),(1,'I')])
    self.numbers = OrderedDict([(v,k) for k, v in self.numerals.items()])

  def get_roman_value(self):
    result = ""
    current_value = self.value
    for decimal_val in self.numerals:
      consecutive_digits = 0
      roman_val = self.numerals[decimal_val]
      while decimal_val <= current_value:
        if consecutive_digits < 3:
          result += roman_val
          consecutive_digits += 1
        else:
          previous = result[-4:]
          if previous[0] in ['L','V','I']:
            actual = previous[1] + self.get_prev_numeral(previous[0])
          else:
            actual = previous[0] + previous[2] + self.get_prev_numeral(previous[1])
          result = result.replace(previous, actual)
          consecutive_digits = 0
        current_value -= decimal_val
    return result

  def get_prev_numeral(self, n):
    numerals = self.numerals.values()
    return numerals[numerals.index(n)-1] 
