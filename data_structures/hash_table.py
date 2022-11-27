# %%
from xxhash import xxh128 as xxhash
from mmh3 import hash128 as mmh3


class hash_table:

    # this table is designed for counting kmers
    # key : kmer
    # value : count

    def __init__(self, size, hashing_flag):
        # set python's default hashing function as the default
        DEFAULT_HASH = self.hasher
        MMH3_FLAG = "mmh"
        XXH_FLAG = "xxh"

        self.size = size
        # a list of keys
        self.keys = [None for i in range(size)]
        # a list of values
        self.values = [0 for i in range(size)]
        self.hash = DEFAULT_HASH
        self.collision_count = 0

        if hashing_flag == XXH_FLAG or hashing_flag == 1:
            self.hash = self.xxhash
        if hashing_flag == MMH3_FLAG or hashing_flag == 2:
            self.hash = self.mmh3

    def __len__(self):
        return self.size

    def insert(self, key):
        hash_index = self.hash(key)
        if self.keys[hash_index] is not None:
            if self.keys[hash_index] == key:
                self.values[hash_index] += 1
            else:
                # different keys have the same hash index
                # this is a collision
                self.collision_count += 1
                self.handle_collision(hash_index, key)
        else:
            self.keys[hash_index] = key
            self.values[hash_index] += 1

    def search(self, key):
        hash_index = self.hash(key)
        # return the value if the key is found
        if self.keys[hash_index] == key:
            return self.values[hash_index]

        return None

    def delete(self, key):
        hash_index = self.hash(key)
        # delete the key value pair if the key is found
        if self.keys[hash_index] == key:
            self.values[hash_index] = 0
            self.keys[hash_index] = None

    def handle_collision(self, hash_index, key):
        def linear_probing(key):
            return (key + 1) % self.size

        while self.keys[hash_index] is not None:
            hash_index = linear_probing(hash_index)
            if hash_index > self.size:
                return

        self.keys[hash_index] = key
        self.values[hash_index] += 1

    def hasher(self, key):
        return hash(key) % self.size

    def xxhash(self, key):
        return xxhash(key).intdigest() % self.size

    def mmh3(self, key):
        return mmh3(key, signed=False) % self.size

    def print(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"{self.keys[i]} : {self.values[i]}")
