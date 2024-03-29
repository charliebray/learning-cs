import os
import sys
import re
import operator
from trees import *
sys.path.insert(0, 'pythonds3/chapter-4/')
from basic import *

def build_parse_tree(fp_expr):
    fp_list = [char for char in re.split('([^0-9])', fp_expr) if char != '']
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for char in fp_list:
        
        # Insert left and go to left child node/tree
        if char == '(':
            current_tree.insert_left(None)
            p_stack.push(current_tree)
            current_tree = current_tree.left_child

        # Insert right child and go to right child node/tree
        elif char in ['+', '*', '/', '-']:
            current_tree.root = char
            current_tree.insert_right(current_tree)
            p_stack.push(current_tree)
            current_tree = current_tree.right_child

        # Travel to parent node
        elif char == ')':
            current_tree = p_stack.pop()

        # Assign node a value
        else:
            current_tree.root = int(char)
            current_tree = p_stack.pop()

    return expr_tree

def evaluate(binarytree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    if binarytree.left_child == None and binarytree.right_child == None:
        return binarytree.root
    else:
        fn = operators[binarytree.root]
        return fn(evaluate(binarytree.left_child), evaluate(binarytree.right_child))

def main():
    import re
    fp_expr = "((10+5)*3)"
    expr_tree = build_parse_tree(fp_expr)
    print(expr_tree.right_child.root)
    print(evaluate(expr_tree))

if __name__ == '__main__':
    main()


