from basic import *

def palindrome_checker(a_str):

    # Store characters of string in a dequeue
    dequeue = Dequeue()
    for char in a_str:
        dequeue.add_rear(char)

    while dequeue.size() > 1:
        if dequeue.remove_rear() == dequeue.remove_front():
            continue
        else:
            return False

    return True

def main():
    print(palindrome_checker("madam"))

if __name__ == '__main__':
    main()