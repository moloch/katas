import unittest
from bowling import Game

class BowlingGameTest(unittest.TestCase):

  def testGutterGame(self):
    g = Game()
    for i in range(20):
      g.roll(0)
    self.assertEqual(0, g.score())  

if __name__ == '__main__':
    unittest.main()
