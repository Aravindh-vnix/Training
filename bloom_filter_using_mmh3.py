
#Implementation of kata05 http://codekata.com/kata/kata05-bloom-filters/

from bitarray import bitarray
import mmh3

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return "no"
        return "yes"

bf = BloomFilter(500000, 7)

lines = open("words.txt").read().splitlines()
for line in lines:
    bf.add(line)

print bf.lookup("vels")
