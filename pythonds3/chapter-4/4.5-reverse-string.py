from basic import *

def rev_string(my_str):
    '''
    Reverse string function using a stack.
    '''

    stack = Stack()
    for char in my_str:
        stack.push(char)

    rev_str = ""
    while stack.is_empty() == False:
        rev_str += stack.pop()

    return rev_str

def main():
    rev_str = rev_string("charles")
    print(rev_str)

if __name__ == '__main__':
    main()