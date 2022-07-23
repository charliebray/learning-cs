def selection_sort(a_list):
    '''
    a_list (list): A list of integers/floats.

    Returns the list sorted using the selection sort method O(n^2).
    '''
    for last_index in range(len(a_list) - 1, 0, -1):
        max_item = a_list[last_index]
        max_index = last_index
        for index in range(0, last_index):
            if a_list[index] > max_item:
                max_item = a_list[index]
                max_index = index
        
        a_list[last_index], a_list[max_index] = a_list[max_index], a_list[last_index]

    return

def main():
    a_list = [-1,1,-2,5,4,3,2,1]
    selection_sort(a_list)
    print(a_list)

if __name__ == '__main__':
    main()

