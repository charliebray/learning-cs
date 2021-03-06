class HashTable:

    def __init__(self):
        self.size = 3
        self.slots = [None] * self.size 
        self.data = [None] * self.size 

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def put(self, key, value):
        hash_index = self.hash_function(key)

        if self.slots[hash_index] == None:
            self.slots[hash_index] = key
            self.data[hash_index] = value

        else:
            if self.slots[hash_index] == key:
                self.data[hash_index] = value
            else:
                next_hash_index = self.hash_function(hash_index + 1)
                while self.slots[next_hash_index] != None and self.slots[next_hash_index] != key:
                    next_hash_index = self.hash_function(next_hash_index + 1)

                    # Check if we're back where we started
                    if hash_index == next_hash_index:
                        return print(f'No slots left available.')

                if self.slots[next_hash_index] == None:
                    self.slots[next_hash_index] = key
                    self.data[next_hash_index] = value
                else:
                    self.data[next_hash_index] = value

    def get(self, key):
        start_index = self.hash_function(key)
        next_hash_index = self.hash_function(start_index + 1)

        if self.slots[start_index] == key:
            return self.data[start_index]

        while next_hash_index != start_index:
            if self.slots[next_hash_index] == key:
                return self.data[next_hash_index]
            next_hash_index = self.hash_function(next_hash_index + 1)

        return None

    def hash_function(self, key):
        return key % self.size



def main():
    hashtable = HashTable()
    hashtable[0] = 'zero'
    hashtable[1] = 'one'
    hashtable[2] = 'two'
    hashtable[3] = 'three'
    print(hashtable.get(4))

if __name__ == '__main__':
    main()
