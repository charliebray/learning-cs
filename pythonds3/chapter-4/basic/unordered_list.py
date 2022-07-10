from node import *

class UnorderedList:

    def __init__(self):
        self.head = None 

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current_node = self.head
        counter = 0
        while current_node != None:
            counter += 1
            current_node = current_node.next
        return counter

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
        else:
            prev_node.next = current_node.next

    def append(self, item):
        current_node = self.head
        new_node = Node(item)

        if self.size() == 0:
            self.head = new_node
        else:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

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
                return temp_node

            prev_node = None
            current_node = self.head
            while current_node.next != None:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = None
            return current_node.data

        except:
            raise ValueError(f'List is empty.')

    def __str__(self):
        current_node = self.head
        a_list = []
        while current_node != None:
            a_list.append(current_node.data)
            current_node = current_node.next
        return f'{a_list}'


def main():
    unordered_list = UnorderedList()

    unordered_list.add(1)
    unordered_list.add(2)
    unordered_list.add(3)
    print(unordered_list)

    unordered_list.remove(1)
    unordered_list.append(1)

    print(unordered_list)
    print(unordered_list.head)


if __name__ == '__main__':
    main()
