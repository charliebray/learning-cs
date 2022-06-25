class binaryTree:
    '''
    Creates a simple BST (binary search tree) with the ability to insert,
    search, and print the BST (in order). Deleteing a node would be interesting... come back later.
    '''

    def __init__(self, value: int) -> None:

        self.value = value
        self.left = None
        self.right = None

    def insertNode(self, value: int) -> None:

        if value <= self.value:
            if self.left == None:
                self.left = binaryTree(value)
            else:
                self.left.insertNode(value)
        else:
            if self.right == None:
                self.right = binaryTree(value)
            else:
                self.right.insertNode(value)

    def contains(self, value: int):

        if value == self.value:
            return True
        elif value < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):

        if self.left != None:
            self.left.printInOrder()
        print(self.value)

        if self.right != None:
            self.right.printInOrder()