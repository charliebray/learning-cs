def fib(n):
    '''
    Recursive: O(2^n) time complexity
    '''
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_2(n, collect = {1: 1, 2: 1}):
    '''
    Memoization/caching: O(n) time complexity
    '''
    if n not in collect:
        collect[n] = fib_2(n-1, collect) + fib_2(n-2, collect)
    return collect[n]

def fib_3(n):
    '''
    Dynamic: O(n) time complexity
    '''
    fib_list = [1, 1]
    if n <= 2:
        return fib_list

    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

def main():
    print(fib_3(10))
    # print([fib(n) for n in range(1, 10)])

if __name__ == '__main__':
    main()