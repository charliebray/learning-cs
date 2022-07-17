import re

def reverse_string(a_str):
    if a_str == "":
        return a_str
    else:
        return a_str[-1] + reverse_string(a_str[:-1])

def palindrome(a_str):
    if a_str == reverse_string(a_str):
        return True
    return False

def another_palindrome(a_str):
    if len(a_str) <= 1:
        return True
    elif a_str[0] == a_str[-1]:
        return another_palindrome(a_str[1:-1])
    else:
        return False

def main():
    a_str = 'mum mum'
    a_str = re.sub(r'[^a-zA-Z]', '', a_str)
    print(another_palindrome(a_str))

if __name__ == '__main__':
    main()