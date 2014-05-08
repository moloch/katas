from collections import OrderedDict

class RomanNumber():

  def __init__(self, value):
    self.value = value
    self.numerals = [(1,'I'),(5,'V')]

  def get_roman_value(self):
    result = ""
    current_value = self.value
    while len(self.numerals) > 0:
      numeral = self.numerals.pop()
      print numeral[0], numeral[1]
      while numeral[0] <= current_value:
        result += numeral[1]
        current_value -= numeral[0] 
    return result 
