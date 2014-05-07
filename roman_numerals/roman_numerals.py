class RomanNumber():

  def __init__(self, value):
    self.value = value

  def get_roman_value(self):
    result = ""
    for i in range(self.value):
      result += "I"
    return result 
