class Frame:

  def __init__(self):
    self.rolls = []

  def roll(self, pins):
    if self.get_points() + pins <= 10:
      self.rolls.append(pins)
      return True
    else:
      return False

  def get_points(self):
    return sum(self.rolls)

  def is_gutter(self):
    return sum(self.rolls) == 10 and len(self.rolls) == 2

  def is_strike(self):
    return sum(self.rolls) == 10 and len(self.rolls) == 1

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
