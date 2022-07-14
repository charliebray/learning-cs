from basic import *

def palindrome_checker(a_str):

    # Remove spaces before
    a_str = ''.join(a_str.strip(' ').split(' '))

    # Store characters of string in a dequeue
    deque = Deque()
    for char in a_str:
        deque.add_rear(char)

    while deque.size() > 1:
        if deque.remove_rear() == deque.remove_front():
            continue
        else:
            return False

    return True

def main():
    print(palindrome_checker("m  a   dam   "))

if __name__ == '__main__':
    main()