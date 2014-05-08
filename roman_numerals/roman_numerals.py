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
      consecutive_numerals = 0
      while numeral[0] <= current_value:
        if consecutive_numerals < 3:
          result += numeral[1]
          consecutive_numerals += 1
        else:
          result = result.replace('III', 'IV')
          consecutive_numerals = 0
        current_value -= numeral[0]
    return result 
