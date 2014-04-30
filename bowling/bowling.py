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

  def is_spare(self):
    return self.is_full() and len(self.rolls) == 2

  def is_strike(self):
    return self.is_full() and len(self.rolls) == 1

  def is_full(self):
    return sum(self.rolls) == 10

class Game:

  def __init__(self):
    self.frames = []

  def roll(self, pins):
    if len(self.frames) == 0 or len(self.frames[-1].get_rolls()) > 2 \
      or self.frames[-1].is_full():
      frame = Frame()
      self.add_frame(frame)
    self.frames[-1].roll(pins) 
 
  def get_score(self):
    score = 0
    for i, frame in enumerate(self.frames):
      score += frame.get_points()
      if i > 0:
        if self.frames[i-1].is_strike():
          score += frame.get_points()
        elif self.frames[i-1].is_spare():
          score += frame.rolls[0]
    return score

  def add_frame(self, frame):
    self.frames.append(frame)
  
  def frames_to_list(self):
    l = []
    for f in self.frames:
      l.append(f.rolls)
    return l
      
