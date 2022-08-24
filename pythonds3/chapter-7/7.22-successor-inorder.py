from trees.binarysearchtree import *

if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree = BinarySearchTree()
    my_tree["j"] = "jumps"
    my_tree["a"] = "a"
    my_tree["d"] = "dog"
    my_tree["o"] = "over"
    my_tree["f"] = "fox"
    my_tree["b"] = "brown"
    my_tree["q"] = "quick"
    my_tree["t"] = "the"
    my_tree["l"] = "lazy"

    # Expected result
    print('Expected Result:')
    for node in my_tree:
        print(my_tree[node])
    print('----------')

    # Inorder traversal using successor
    # Start at root node
    current_node = my_tree.root

    # Keep going left until we can't no more
    while current_node.left_child != None:
        current_node = current_node.left_child
    
    # jump between successors until we can't no more
    print(current_node.value)
    while current_node.find_successor() != None:
        print(current_node.find_successor().value)
        current_node = current_node.find_successor()