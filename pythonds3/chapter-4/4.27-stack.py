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
    
    def push(self, item):
        current_node = self.head
        if self.size == 0:
            self.head = Node(item)
        else:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        prev_node = None
        current_node = self.head

        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next

        if prev_node == None:
            self.head = None
        else:
            prev_node.next = None

        self.size -= 1
        return current_node

    def peek(self):
        if self.size == 0:
            return None

        prev_node = None
        current_node = self.head

        while current_node != None:
            prev_node = current_node
            current_node = current_node.next

        return prev_node



def main():
    stack = Stack()
    stack.push(1)
    print(stack.peek())

if __name__ == '__main__':
    main()