import unittest
import timeit

from kata5 import NaiveChecker, BloomChecker

find = raw_input("Enter the word:")


class TestNaiveChecker(unittest.TestCase):

    def setUp(self):

        self.n = NaiveChecker()
        self.n.populate()

    def test_simple_word_is_in(self):

        self.assertTrue(self.n.check(find))
        print "Word Found"




if __name__ == '__main__':
    unittest.main()
