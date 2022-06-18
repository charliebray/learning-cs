class MyHashSet:
    '''
    Designing a HashSet
    '''
    
    def __init__(self):
        self.size = 10**4
        self.table = [None] * self.size

    def add(self, key: int):
        hash_value = key % self.size
        if self.table[hash_value] is None:
            self.table[hash_value] = [key]
        else:
            self.table[hash_value].append(key)
        return None

    def remove(self, key: int):
        hash_value = key % self.size
        if self.table[hash_value] != None:
            while key in self.table[hash_value]:
                self.table[hash_value].remove(key)
        return None

    def contains(self, key: int):
        hash_value = key % self.size 
        if self.table[hash_value] != None:
            if key in self.table[hash_value]:
                return True
        return False