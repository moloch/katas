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

  def testIsSpare(self):
    self.f.roll(4)
    self.f.roll(6)
    self.assertTrue(self.f.is_spare())

  def testIsStrike(self):
    self.f.roll(10)
    self.assertTrue(self.f.is_strike())
  
class BowlingGameTest(unittest.TestCase):

  def setUp(self):
    self.g = Game()

  def testGutterGame(self):
    self.__rollMany(0,0)
  
  def testAllOnes(self):
    self.__rollMany(1,20)

  def testAddFrame(self):
    self.g.add_frame(Frame())
    self.assertEquals(1, len(self.g.frames))

  def testBuildFramesWhileRolling(self):
    self.g.roll(10)
    self.assertEqual([[10]], self.g.frames_to_list())
    self.g.roll(2)
    self.assertEqual([[10], [2]], self.g.frames_to_list())
    self.g.roll(4)
    self.assertEqual([[10], [2,4]], self.g.frames_to_list())
    self.g.roll(10)
    self.assertEqual([[10], [2,4], [10]], self.g.frames_to_list())

  def testSpare(self):
    self.g.roll(4)
    self.g.roll(6)
    self.g.roll(4)
    self.assertEqual(14+4, self.g.get_score())

  def testStrike(self):
    self.g.roll(10)
    self.g.roll(2)
    self.g.roll(4)
    self.assertEqual(10+6+6, self.g.get_score())

  def testShouldNotAddMoreThenTenFrames(self):
    for i in range(10):
      self.g.add_frame(Frame())
    self.assertFalse(self.g.add_frame(Frame()))
    self.assertEqual(10, len(self.g.frames))

  def __rollMany(self, pins, expected_score):
    for i in range(20):
      self.g.roll(pins)
    self.assertEqual(expected_score, self.g.get_score()) 

if __name__ == '__main__':
    unittest.main()
