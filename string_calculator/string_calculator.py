class Calculator():

  def add(self, numbers):
    if numbers == "":
      return 0
    else:
      return sum(int(x) for x in numbers.split(",")) 
