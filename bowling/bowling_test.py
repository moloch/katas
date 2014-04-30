import unittest
from bowling import Frame,Game


class FrameTest(unittest.TestCase):

  def setUp(self):
    self.f = Frame()

  def testShouldAddPins(self):
    for i in range(10):
      self.assertEqual(True, self.f.roll(1))

  def testShouldNotAddPins(self):
      self.assertEqual(False, self.f.roll(11))

  def testGetPointsForCurrentFrame(self):
    self.f.roll(8)
    self.f.roll(1)
    self.assertEqual(9, self.f.get_points())

class BowlingGameTest(unittest.TestCase):

  def setUp(self):
    self.g = Game()

  def testGutterGame(self):
    self.__rollMany(0,0)
  
  def testAllOnes(self):
    self.__rollMany(1,20)

#  def testSpare(self):
#    self.g.roll(4)
#    self.g.roll(6)
#    self.g.roll(4)
#    self.assertEqual(14+4, self.g.get_score())

  def __rollMany(self, pins, expected_score):
    for i in range(20):
      self.g.roll(pins)
    self.assertEqual(expected_score, self.g.get_score()) 


if __name__ == '__main__':
    unittest.main()
