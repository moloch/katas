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
      roman_val = self.numerals[decimal_val]
      while decimal_val <= current_value:
        result += roman_val
        current_value -= decimal_val
    return result

  def get_prev_numeral(self, n):
    numerals = self.numerals.values()
    return numerals[numerals.index(n)-1] 
