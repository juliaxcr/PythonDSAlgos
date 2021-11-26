# Built-in hash table in Python = dictionary

# Hash (key value pair) produces address

# Two important characteristics:
# 1. One way
# 2. Deterministic
#       - same result every time

# Mutiple key value pairs can be stored at the same address

# Collision: happens when key value pair is placed at address 
# key value pair already exists at

# Seperate chaining: If key value pair is placed in address where
# key value pair already exists, it will go down through memory
# until it finds an empty memory space (linear probing - open addressing)
# This is done so that there is no more than 1 key value pair at a 
# single address.

class HashTable:
    # prime number increases randomness of how key value pairs will be distributed
    # so it reduces the number of collisions
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # 23 is prime number
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()
my_hash_table.print_table()