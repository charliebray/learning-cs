class Stack:
    '''
    Define a stack using primitive python data collections (i.e. list).
    '''

    def __init__(self) -> None:
        self._items = []

    def __str__(self) -> str:
        return f'{self._items}'

    def is_empty(self) -> bool:
        return not (self._items)

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self) -> int:
        return len(self._items)

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

if __name__ == '__main__':
    rev_str = rev_string("charles")
    print(rev_str)
