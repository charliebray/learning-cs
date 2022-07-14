from node import *

class UnorderedList:

    def __init__(self):
        self.head = None 
        self._size = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self._size += 1

    def size(self):
        return self._size

    def search(self, item):
        current_node = self.head
        while current_node != None:
            if current_node.data == item:
                return True
            current_node = current_node.next
        return False

    def remove(self, item):
        prev_node = None
        current_node = self.head

        while current_node != None:
            if current_node.data == item:
                break
            prev_node = current_node
            current_node = current_node.next

        if current_node == None:
            raise ValueError(f'{item} is not in the list.')
        if prev_node == None:
            self.head = current_node.next
            self._size -= 1
        else:
            prev_node.next = current_node.next
            self._size -= 1

    def append(self, item):
        current_node = self.head
        new_node = Node(item)

        if self.size() == 0:
            self.head = new_node
        else:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
        
        self._size += 1

    def insert(self, pos, item):
        new_node = Node(item)
        prev_node = None
        current_node = self.head

        if pos > self.size():
            raise ValueError(f'Index ({pos}) exceeds length of list ({self.size()}).')

        counter = 0
        while counter < pos:
            prev_node = current_node
            current_node = current_node.next
            counter += 1

        if prev_node == None:
            self.head = new_node
            new_node.next = current_node
        else:
            prev_node.next = new_node
            new_node.next = current_node

        self._size += 1


    def index(self, item):
        try:
            counter = 0
            current_node = self.head
            while current_node.data != item:
                current_node = current_node.next
                counter += 1
            return counter

        except:
            raise ValueError(f'Item ({item}) is not in list.')

    def pop(self):
        try:
            if self.size() == 1:
                temp_node = self.head
                self.head = None
                self._size -= 1
                return temp_node

            prev_node = None
            current_node = self.head
            while current_node.next != None:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = None
            self._size -= 1
            return current_node.data

        except:
            raise ValueError(f'List is empty.')

    def pop_pos(self, index):
        prev_node = None
        current_node = self.head
        
        counter = 0
        while counter < index:
            prev_node = current_node
            current_node = current_node.next
            counter += 1

        prev_node.next = current_node.next
        return current_node.data

    def slice(self, start, stop):
        sliced_list = UnorderedList()
        counter = 0

        # Find starting node
        current_node = self.head
        while counter < start:
            current_node = current_node.next
            counter += 1

        # Set head of new list to this node
        start_node = Node(current_node.data)
        sliced_list.head = start_node

        # Continue traversing to find end string
        prev_node = sliced_list.head
        while counter < (stop - 1):
            current_node = current_node.next
            new_node = Node(current_node.data)
            prev_node.next = new_node
            prev_node = new_node
            counter += 1
        
        return sliced_list


    def __str__(self):
        current_node = self.head
        a_list = []
        while current_node != None:
            a_list.append(current_node.data)
            current_node = current_node.next
        return f'{a_list}'


def main():
    unordered_list = UnorderedList()

    unordered_list.append(1)
    unordered_list.append(2)
    unordered_list.append(3)
    unordered_list.append(4)
    unordered_list.append(5)
    print(unordered_list)
    
    print(unordered_list.pop_pos(2))
    print(unordered_list)


if __name__ == '__main__':
    main()
