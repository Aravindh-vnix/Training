#Test case for a sorting of balls in kata11. http://codekata.com/kata/kata11-sorting-it-out/
import unittest
from sorting_balls import Rack

class MyTestCase(unittest.TestCase):
    def test(self):
        rack=Rack.new(self)
        self.assertEqual([],rack.balls)
        rack.add(20)
        self.assertEqual([20],rack.balls)
        rack.add(10)
        self.assertEqual([10,20],rack.balls)
        rack.add(30)
        self.assertEqual([10,20,30],rack.balls)


if __name__ == '__main__':
    unittest.main()
