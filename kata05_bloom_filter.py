dictionay = "words.txt"
default_hash_dime = 32
num_of_hashes = 8

from sys import getsizeof

class SpellChecker(object):
    def populate(self):
        raise NotImplementedError
    def check(self, word):
        raise NotImplementedError
    def get_size(self):
        raise NotImplementedError
    def spell_test(self, words):
        not_found = [w for w in words if not self.check(w)]
        return not_found

class NaiveChecker(SpellChecker):
    def __init__(self):
        self.words = None
        super(NaiveChecker, self).__init__()
    def get_size(self):
        return getsizeof(self.words)
    def populate(self):
        self.words = set(x.strip() for x in open(dictionay).readlines())
    def check(self, word):
        return word in self.words

class BloomChecker(SpellChecker):
    def __init__(self, hash_dim=default_hash_dime, num_hashes=num_of_hashes):
        self.hash_dim = hash_dim
        self.num_hashes = num_hashes
        self.hash = (2 ** self.hash_dim) - 1
        super(BloomChecker, self).__init__()
    def get_size(self):
        return self.hash_dim
    def _hash_word(self, word):
        pass
    def populate(self):
        self.words = set(x.strip() for x in open(dictionay).readlines())
    def check(self, word):
        return word in self.words
