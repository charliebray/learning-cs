class Node:

    def __init__(self, node_data):
        self._data = node_data
        self._next = None
        self._prev = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, node_data):
        self._data = node_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node_next):
        self._next = node_next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node_prev):
        self._prev = node_prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        current_node = self.head
        temp_list = []
        while current_node != None:
            temp_list.append(current_node.data)
            current_node = current_node.next
        return f'{temp_list}'

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, item):
        new_node = Node(item)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            next_node = self.head
            new_node.next = next_node
            next_node.prev = new_node
            self.head = new_node
        self.size += 1

    def remove(self, item):
        prev_node = None
        current_node = self.head

        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        while current_node.data != item:
            prev_node = current_node
            current_node = current_node.next

        if prev_node == None:
            self.head = current_node.next
            current_node.next.prev = self.head
        elif current_node.next == None:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = current_node.next
            current_node.next.prev = prev_node

        self.size -= 1

    def search(self, item):
        current_node = self.head
        while current_node != None:
            if current_node.data == item:
                return True
            current_node = current_node.next
        return False

    def append(self, item):
        last_node = self.tail
        new_node = Node(item)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            last_node.next = new_node
            new_node.prev = last_node
            self.tail = new_node

        self.size += 1

    def index(self, item):
        current_node = self.head
        counter = 0
        while current_node.data != item:
            current_node = current_node.next
            counter += 1
        return counter

    def insert(self, pos, item):
        prev_node = None
        current_node = self.head
        new_node = Node(item)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        elif pos == 0:
            new_node.next = current_node
            current_node.prev = new_node
            self.head = new_node
            self.size += 1
            return
        elif pos == self.size:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
            return

        counter = 0
        while counter != pos:
            prev_node = current_node
            current_node = current_node.next
            counter += 1

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = current_node
        current_node.prev = new_node

        self.size += 1
        

def main():
    doublylinkedlist = DoublyLinkedList()
    doublylinkedlist.append(1)
    doublylinkedlist.append(2)
    doublylinkedlist.append(3)
    print(doublylinkedlist)



if __name__ == '__main__':
    main()

    