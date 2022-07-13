class RearQueue:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

def main():
    rear_queue = RearQueue()
    rear_queue.enqueue(1)
    rear_queue.enqueue(2)
    rear_queue.enqueue(3)
    print(rear_queue.dequeue())

if __name__ == '__main__':
    main()