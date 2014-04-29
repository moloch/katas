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
