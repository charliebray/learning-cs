class MyHashSet:
    '''
    Designing a HashSet using a very simple hash function.

    It appears that its a game of balance. You can create a large array and minimise
    collisions, but might be using more memory than is required. Too few buckets and
    the search becomes linear complexity.

    Here we're technically using dynamic arrays, but treating it as a static array.
    '''
    
    def __init__(self):
        # Number of buckets in our array.
        self.size = 10**4
        # Fill our array full of empty values.
        self.table = [None] * self.size

    def add(self, key: int):
        # A very basic hashing function.
        hash_value = key % self.size
        # If key doesn't exist then add it at index, otherwise append to dynamic array at index.
        if self.table[hash_value] is None:
            self.table[hash_value] = [key]
        else:
            self.table[hash_value].append(key)
        return None

    def remove(self, key: int):
        # If key exists in hash set, remove all keys at index.
        hash_value = key % self.size
        if self.table[hash_value] != None:
            while key in self.table[hash_value]:
                self.table[hash_value].remove(key)
        return None

    def contains(self, key: int):
        # If key exists in hash set return true, else false.
        hash_value = key % self.size 
        if self.table[hash_value] != None:
            if key in self.table[hash_value]:
                return True
        return False