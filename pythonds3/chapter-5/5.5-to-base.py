def to_string(n, base):
    digits = "0123456789ABCDEF"
    if n < base:
        return digits[n]
    else:
        return to_string(n // base, base) + digits[n % base]

def main():
    print(to_string(1453, 16))

if __name__ == '__main__':
    main()
