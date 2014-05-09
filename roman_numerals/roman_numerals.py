from collections import OrderedDict

class RomanNumber():

  def __init__(self, value):
    self.value = value
    self.numerals = OrderedDict([(10, 'X'),(5, 'V'),(1,'I')])

  def get_roman_value(self):
    result = ""
    current_value = self.value
    for i, numeral in enumerate(self.numerals.iteritems()):
      consecutive_numerals = 0
      while numeral[0] <= current_value:
        if consecutive_numerals < 3:
          result += numeral[1]
          consecutive_numerals += 1
        else:
          previous = result[:-3] + numeral[1]*3
          actual = previous[1] + self.numerals.values()[self.numerals.values().index(previous[0])-1]
          result = result.replace(previous, actual)
          consecutive_numerals = 0
        current_value -= numeral[0]
    return result 
