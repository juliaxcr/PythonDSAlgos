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

    # O(1)
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # 23 is prime number
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    # O(1)
    def set_item(self, key, value):
        # computes address
        index = self.__hash(key)
        # initialize empty list at address if not already initialized
        if self.data_map[index] == None:
            self.data_map[index] = []
        # append key value pair
        self.data_map[index].append([key, value])

    # Assumed to be O(1) for dictionaries in Python, because
    # distribution of key value pairs is assumed to be pretty even
    def get_item(self, key):
        # find index for key
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    # return value if key is found
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        # for loop that moves through data map list
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
        # for loop that moves through key value pairs at address
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys    


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 10)

print(my_hash_table.keys())

