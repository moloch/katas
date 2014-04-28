class Game:

  def __init__(self):
    self._score = 0

  def roll(self, pins):
    self._score += 1

  def score(self):
    return self._score
