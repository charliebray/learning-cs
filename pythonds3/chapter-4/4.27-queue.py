from basic import Node

class Stack:
    
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

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def enqueue(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def dequeue(self):
        prev_node = None
        current_node = self.head

        if self.size == 0:
            return None

        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next

        self.size -= 1

        if prev_node == None:
            self.head = None
            return current_node.data
        else:
            prev_node.next = None
            return current_node.data


def main():
    stack = Stack()
    print(stack)
    print(stack.dequeue())
    print(stack)
    print(stack.size)

if __name__ == '__main__':
    main()
    