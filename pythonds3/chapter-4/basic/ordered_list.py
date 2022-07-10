from node import *

class OrderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        temp_list = []
        current_node = self.head

        while current_node != None:
            temp_list.append(current_node.data)
            current_node = current_node.next

        return f'{temp_list}'

    def add(self, item):
        prev_node = None
        current_node = self.head
        new_node = Node(item)

        while (current_node != None) and (item > current_node.data):
            prev_node = current_node
            current_node = current_node.next

        if prev_node == None:
            self.head = new_node
        else:
            prev_node.next = new_node
            new_node.next = current_node

    def remove(self, item):
        prev_node = None
        current_node = self.head

        try:
            while current_node.data != item:
                prev_node = current_node
                current_node = current_node.next

            if prev_node == None:
                self.head = current_node.next
            else:
                prev_node.next = current_node.next
            
        except:
            raise ValueError(f'Item ({item}) is not in list.')

    def search(self, item):
        current_node = self.head

        while (current_node != None) and (current_node.data < item):
            current_node = current_node.next

        if current_node == None:
            return False
        elif current_node.data == item:
            return True
        return False

    def is_empty(self):
        return self.head == None

    def size(self):
        counter = 0
        current_node = self.head

        while current_node != None:
            current_node = current_node.next
            counter += 1

        return counter

    def index(self, item):
        try:
            counter = 0
            current_node = self.head
            while current_node.data != item:
                current_node = current_node.next
                counter += 1
            return counter

        except:
            return f'Item ({item}) is not in list.'

    def pop(self):
        current_node = self.head

        if current_node.next == None:
            self.head = None
            return current_node

        while current_node.next.next != None:
            current_node = current_node.next

        temp_node = current_node.next
        current_node.next = None

        return temp_node

    def pop_pos(self, pos):
        counter = 0
        prev_node = None
        current_node = self.head

        while counter != pos:
            prev_node = current_node
            current_node = current_node.next
            counter += 1

        if prev_node == None:
            self.head = current_node.next
            return current_node.data
        else:
            prev_node.next = current_node.next
            return current_node.data


    
            

    
def main():
    ordered_list = OrderedList()
    ordered_list.add(1)
    ordered_list.add(2)
    ordered_list.add(3)
    print(ordered_list.pop())
    

if __name__ == '__main__':
    main()

    