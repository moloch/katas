class Frame:

  def __init__(self):
    self.rolls = []

  def roll(self, pins):
    if self.get_points() + pins <= 10:
      self.rolls.append(pins)
      return True
    else:
      return False

  def get_rolls(self):
    return self.rolls

  def get_points(self):
    return sum(self.rolls)

  def is_gutter(self):
    return self.is_full() and len(self.rolls) == 2

  def is_strike(self):
    return self.is_full() and len(self.rolls) == 1

  def is_full(self):
    return sum(self.rolls) == 10

class Game:

  def __init__(self):
    self.score = 0
    self.frames = []

  def roll(self, pins):
    if len(self.frames) == 0 or len(self.frames[-1].get_rolls()) > 2:
      frame = Frame()
      self.add_frame(frame)
    self.frames[-1].roll(pins) 
 
  def get_score(self):
    for frame in self.frames:
      self.score += frame.get_points()
    return self.score

  def add_frame(self, frame):
    self.frames.append(frame)
    
