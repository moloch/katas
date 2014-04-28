import unittest
from bowling import Game

class BowlingGameTest(unittest.TestCase):

  def setUp(self):
    self.g = Game()

  def testGutterGame(self):
    self.__rollMany(0,0)
  
  def testAllOnes(self):
    self.__rollMany(1,20)

  def testSpare(self):
    self.g.roll(4)
    self.g.roll(6)
    self.g.roll(4)
    self.assertEqual(14+4, self.g.get_score())

  def __rollMany(self, pins, expected_score):
    for i in range(20):
      self.g.roll(pins)
    self.assertEqual(expected_score, self.g.get_score()) 


if __name__ == '__main__':
    unittest.main()
