from basic import Node

class Deque():

    def __init__(self):
        self.head = None
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

    def add_rear(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_front(self, item):
        if self.size == 0:
            self.head = Node(item)
        else:
            prev_node = None
            current_node = self.head
            while current_node != None:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = Node(item)
        
        self.size += 1

    def remove_rear(self):
        if self.size == 0:
            return None
        else:
            temp_node = self.head
            self.head = self.head.next
            self.size -= 1
            return temp_node.data

    def remove_front(self):
        if self.size == 0:
            return None
        if self.size == 1:
            temp_node = self.head
            self.head = None
            self.size -= 1
            return temp_node.data
        else:
            prev_node = None
            current_node = self.head
            while current_node.next != None:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = None
            self.size -= 1
            return current_node.data



def main():
    deque = Deque()
    deque.add_rear(1)
    deque.add_rear(2)
    deque.add_front(3)
    print(deque)
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque.remove_front())
    print(deque)

if __name__ == '__main__':
    main()
    
