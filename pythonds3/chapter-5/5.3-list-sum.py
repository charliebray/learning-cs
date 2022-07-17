def list_sum(a_list):
    if len(a_list) == 1:
        return a_list[0]
    return a_list[0] + list_sum(a_list[1:])

def main():
    a_list = list(range(0,10))
    print(list_sum(a_list))

if __name__ == '__main__':
    main()