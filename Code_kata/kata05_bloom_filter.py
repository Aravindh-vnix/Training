dictionay = "words.txt"
default_hash_dime = 32
num_of_hashes = 16

from sys import getsizeof

class SpellChecker(object):
    def check(self, word):
        raise NotImplementedError
    def get_size(self):
        raise NotImplementedError
    def spell_test(self, words):
        not_found = [w for w in words if not self.check(w)]
        return not_found

class BloomChecker(SpellChecker):
    def __init__(self, hash_dim=default_hash_dime, num_hashes=num_of_hashes):
        self.hash_dim = hash_dim
        self.num_hashes = num_hashes
        self.hash = (2 ** self.hash_dim)-1
        super(BloomChecker, self).__init__()
    def get_size(self):
        return self.hash_dim
    def hash_word(self):
        self.words = set(x.strip() for x in open(dictionay).readlines())
    def check(self, word):
        return word in self.words