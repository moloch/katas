from collections import OrderedDict

class RomanNumber():

  def __init__(self, value):
    self.value = value
    self.numerals = OrderedDict([(10, 'X'),(5, 'V'),(1,'I')])
    self.numbers = {v:k for k, v in self.numerals.items()}

  def get_roman_value(self):
    result = ""
    current_value = self.value
    for i, numeral in enumerate(self.numerals.iteritems()):
      consecutive_numerals = 0
      numerals = self.numerals.values()
      while numeral[0] <= current_value:
        if consecutive_numerals < 3:
          result += numeral[1]
          consecutive_numerals += 1
        else:
          previous = result[:-3] + numeral[1]*3
          if self.numbers[previous[0]] % 10 != 0:
            actual = previous[1] + numerals[numerals.index(previous[0])-1]
          else:
            actual = previous[0] + previous[1] + numerals[numerals.index(previous[1])-1]
          result = result.replace(previous, actual)
          consecutive_numerals = 0
        current_value -= numeral[0]
    return result 
