import os
import sys
import re
import operator
from trees import *
sys.path.insert(0, 'pythonds3/chapter-4/')
from basic import *

def build_parse_tree(fp_expr):
    fp_list = fp_expr.split()
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

        elif char == 'NOT':
            current_tree.root = char
            current_tree.insert_left(None)
            p_stack.push(current_tree)
            current_tree = current_tree.left_child

        # Insert right child and go to right child node/tree
        elif char in ['AND', 'OR']:
            current_tree.root = char
            current_tree.insert_right(current_tree)
            p_stack.push(current_tree)
            current_tree = current_tree.right_child

        # Travel to parent node
        elif char == ')':
            current_tree = p_stack.pop()

        # Assign node a value
        else:
            current_tree.root = char
            current_tree = p_stack.pop()

    return expr_tree

def evaluate(binarytree):
    if binarytree.root == 'AND':
        return (evaluate(binarytree.left_child) and evaluate(binarytree.right_child))
    elif binarytree.root == 'OR':
        return (evaluate(binarytree.left_child) or evaluate(binarytree.right_child))
    elif binarytree.root == 'NOT':
        return (not evaluate(binarytree.left_child))
    elif binarytree.root == 'TRUE':
        return True
    else:
        return False

def main():
    fp_expr = "( NOT ( TRUE OR FALSE ) ) OR FALSE"
    expr_tree = build_parse_tree(fp_expr)
    print(evaluate(expr_tree))

if __name__ == '__main__':
    main()