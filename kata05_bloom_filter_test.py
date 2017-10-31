#kata05_bloom_filter test case
import unittest
from kata05_bloom_filter import BloomChecker

find = raw_input("Enter the word:")

class TestBloomChecker(unittest.TestCase):
    def setUp(self):
        self.n = BloomChecker()
        self.n.hash_word()
    def test_simple_word_is_in(self):
        is_found = self.n.check(find)
        if is_found:
            print "Word found"
        else:
            print "Word not found"

if __name__ == '__main__':
    unittest.main()
