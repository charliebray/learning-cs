class BinaryTree:

    def __init__(self, val):
        self.root = val
        self.left_child = None
        self.right_child = None

    def insert_left(self, val):
        new_node = BinaryTree(val)
        if self.left_child == None:
            self.left_child = new_node
        else:
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, val):
        new_node = BinaryTree(val)
        if self.right_child == None:
            self.right_child = new_node
        else:
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_root_val(self):
        return self.root

    def set_root_val(self, val):
        self.root = val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

def main():
    binarytree = BinaryTree("a")
    binarytree.insert_left("b")
    binarytree.insert_right("c")
    binarytree.get_left_child().insert_right("d")
    binarytree.get_right_child().insert_left("e")
    binarytree.get_right_child().insert_right("f")

if __name__ == '__main__':
    main()