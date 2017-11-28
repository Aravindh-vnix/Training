#Test case for a sorting of balls in kata11. http://codekata.com/kata/kata11-sorting-it-out/
import unittest
from sorting_balls import Rack

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual([],Rack.balls(self))
        Rack.add(20)
        self.assertEqual([20],Rack.balls(self))
        Rack.add(10)
        self.assertEqual([10,20], Rack.balls(self))
        Rack.add(30)
        self.assertEqual([10,20,30], Rack.balls(self))

if __name__ == '__main__':
    unittest.main()
