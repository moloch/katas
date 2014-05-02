class Calculator():

  def add(self, numbers):
    if numbers == "":
      return 0
    else:
      delimiters = ["\n"]
      if numbers.startswith("//"):
        delimiters.append(numbers[2])
        numbers = numbers[4:]
      for d in delimiters:
        numbers = numbers.replace(d, ",")     
      return sum(int(x) for x in numbers.split(",")) 
