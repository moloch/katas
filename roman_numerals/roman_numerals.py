from collections import OrderedDict

class RomanNumber():

  def __init__(self, value):
    self.value = value
    self.numerals = OrderedDict([(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),
				 (90,'XC'),(50,'L'),(40,'XL'),(10, 'X'),
                                 (9,'IX'),(5, 'V'),(4,'IV'),(1,'I')])

  def get_roman_value(self):
    result = ""
    current_value = self.value
    for decimal_val in self.numerals:
      roman_val = self.numerals[decimal_val]
      while decimal_val <= current_value:
        result += roman_val
        current_value -= decimal_val
    return result
