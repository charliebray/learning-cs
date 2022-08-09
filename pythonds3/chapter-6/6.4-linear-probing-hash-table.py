class HashTable:

    def __init__(self):
        self.size = 3
        self.slots = [None] * self.size 
        self.data = [None] * self.size 

    def __str__(self):
        return str(self.data)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        counter = 0
        for index in range(0, self.size):
            if self.slots[index] != None:
                counter += 1
        return counter

    def __contains__(self, key):
        for another_key in self.slots:
            if key == another_key:
                return True
        return False

    def __delitem__(self, key):
        self.data[self.hash_function(key)] = None

    def get_size(self):
        return self.size

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
    print(hashtable)
    hashtable[2] = 'two'
    print(hashtable)
    hashtable[5] = 'five'
    print(hashtable.slots)
    print(Hashtable.data)
    print(hashtable[2])
    print(hashtable[5])

if __name__ == '__main__':
    main()
