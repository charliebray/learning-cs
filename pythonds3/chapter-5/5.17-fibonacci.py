def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    print([fib(n) for n in range(0, 10)])

if __name__ == '__main__':
    main()