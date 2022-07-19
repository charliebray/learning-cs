import os
import sys
sys.path.insert(0, 'pythonds3/chapter-4/')

from basic import *

def move_tower(height, from_stack, to_stack, with_stack):
    if height >= 1:
        move_tower(height-1, from_stack, with_stack, to_stack)
        move_disk(from_stack, to_stack)
        print(f'{from_stack}, {to_stack}, {with_stack}')
        move_tower(height-1, with_stack, to_stack, from_stack)

def move_disk(from_stack, to_stack):
    temp = from_stack.pop()
    to_stack.push(temp)


def main():
    stack_one, stack_two, stack_three = Stack(), Stack(), Stack()
    stack_one.push('Big')
    stack_one.push('Medium')
    stack_one.push('Small')
    move_tower(3, stack_one, stack_two, stack_three)

if __name__ == '__main__':
    main()