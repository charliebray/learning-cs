class MyHashMap:
    '''
    Create a hash mapping, without buckets.

    Obviously memory expensive, but constant complexity for insert/remove/search.
    Requires knowledge of possible key inputs - here we assume the range 0 to 10**6 inclusive.
    '''

    def __init__(self) -> None:
        self.size = 10**6 + 1
        self.table = [None] * self.size 

    def put(self, key: int, value: int) -> None:
        self.table[key] = [key, value]

    def get(self, key: int):
        if self.table[key] != None:
            return self.table[key][-1]
        return -1

    def remove(self, key: int) -> None:
        if self.table[key] != None:
            self.table[key] = None