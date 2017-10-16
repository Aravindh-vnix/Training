import unittest
import timeit

from kata05_bloom_filter import NaiveChecker, BloomChecker

find = raw_input("Enter the word:")


class TestNaiveChecker(unittest.TestCase):

    def setUp(self):

        self.n = NaiveChecker()
        self.n.populate()

    def test_simple_word_is_in(self):

        is_found = self.n.check(find)


        if is_found == True:
            print "Word found"
        else:
            print "Word not found"



if __name__ == '__main__':
    unittest.main()
