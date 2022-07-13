from ast import Constant


class ConstantQueue:

    def __init__(self):
        self._items = []
        self._index = 0

    def __str__(self):
        return f'{self._items[self._index:]}'

    def size(self):
        return len(self._items[self._index:])

    def is_empty(self):
        return not self._items[self._index:]

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        temp = self._items[self._index]
        self._items[self._index] = None
        self._index += 1
        return temp

def main():
    const_queue = ConstantQueue()
    const_queue.enqueue(1)
    const_queue.enqueue(2)
    const_queue.enqueue(3)
    print(const_queue.dequeue())
    print(const_queue.size())
    print(const_queue)

if __name__ == '__main__':
    main()