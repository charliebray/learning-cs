def reverse(a_list):
    if a_list == []:
        return []
    else:
        return [a_list.pop()] + reverse(a_list)

def main():
    a_list = list(range(0,10))
    print(reverse(a_list))

if __name__ == '__main__':
    main()
    