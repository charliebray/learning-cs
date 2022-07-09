from basic import *

def matches(symbol_left, symbol_right):
    all_lefts = '([{'
    all_rights = ')]}'
    return all_lefts.index(symbol_left) == all_rights.index(symbol_right)

def par_checker(symbol_string):
    stack = Stack()
    for symbol in symbol_string:
        if symbol in '([{':
            stack.push(symbol)
        else:
            if stack.is_empty():
                return False
            else:
                if not matches(stack.pop(), symbol):
                    return False

    return stack.is_empty()
 
def main():
    print(par_checker('()()'))

if __name__ == '__main__':
    main()
