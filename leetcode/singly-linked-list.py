class ListNode:
    '''
    Defines a node object, a value (data) and next (pointer)
    '''
    
    def __init__(self, val: int) -> None:
        # data
        self.value = val
        # pointer
        self.next = None

class MyLinkedList:
    '''
    Here we define a linked list. Specifically, the creation of
    node objects (ListNode) each having a value, and a pointer.
    '''
    
    def __init__(self) -> None:
        # Initialise a linked list with a head (value of None/Null)
        self.size = 0
        self.head = ListNode(None)
        
    def get(self, index: int) -> int:
        # If index is larger than the size of list (or less than zero), do nothing.
        if index < 0 or index >= self.size:
            return -1
        
        # Start at head, loop through to index desired and return the value
        node = self.head
        for _ in range(0, index+1):
            node = node.next
            
        return node.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # If index is larger than the size of list (or less than zero), do nothing.
        if index < 0 or index > self.size:
            return None
        
        # Increase size of list
        self.size += 1
        
        # Loop through to previous node before index
        prev_node = self.head
        for _ in range(0, index):
            prev_node = prev_node.next
        
        # Create new node using value provided, and point to previous nodes next
        new_node = ListNode(val)
        new_node.next = prev_node.next
        
        # Map previous node to new node
        prev_node.next = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        # If index is tail or larger (or less than zero), do nothing.
        if index < 0 or index >= self.size:
            return None
    
        self.size -= 1
        
        prev = self.head
        for _ in range(0, index):
            prev = prev.next
        
        prev.next = prev.next.next