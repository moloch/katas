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
    if len(self.frames) == 0 or len(self.frames[-1].get_rolls()) == 2 \
      or self.frames[-1].is_full():
      frame = Frame()
      self.add_frame(frame)
    self.frames[-1].roll(pins) 

  def get_score(self):
    score = 0
    for i, frame in enumerate(self.frames):
      score += frame.get_points()
      if i < len(self.frames)-1:
        if frame.is_strike():
          score += self.frames[i+1].get_points()
          if i < len(self.frames)-2 and self.frames[i+1].is_strike():
            score += self.frames[i+2].rolls[0]
        elif frame.is_spare():
          score += self.frames[i+1].rolls[0]
    return score

  def add_frame(self, frame):
    if len(self.frames) < 10 or len(self.frames) == 10 and \
      (self.frames[-1].is_strike() or self.frames[-1].is_spare()):
      self.frames.append(frame)
      return True
    else:
      return False
  
  def frames_to_list(self):
    l = []
    for f in self.frames:
      l.append(f.rolls)
    return l
      
