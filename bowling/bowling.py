class Frame:

  def __init__(self):
    self.rolls = []

  def add(self, pins):
    if pins <= 10:
      self.rolls.append(pins)
      return True
    else:
      return False

  def get_points(self):
    return sum(self.rolls)

class Game:

  def __init__(self):
    self.score = 0
    self.rolls = []

  def roll(self, pins):
    self.rolls.append(pins)

  def get_score(self):
    for roll in self.rolls:
      self.score += roll
    return self.score
