import unittest
from bowling import Game

class BowlingGameTest(unittest.TestCase):

  def setUp(self):
    self.g = Game()

  def testGutterGame(self):
    for i in range(20):
      self.g.roll(0)
    self.assertEqual(0, self.g.score())
  
  def testAllOnes(self):
    for i in range(20):
      self.g.roll(1)
    self.assertEqual(20, self.g.score())  

if __name__ == '__main__':
    unittest.main()
