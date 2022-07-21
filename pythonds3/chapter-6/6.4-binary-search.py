def binary_search(sorted_list, item):
    '''
    sorted_list (list): A sorted list of integers.
    item (int): A integer we are wanting to search for in the sorted list.

    Returns True if the item exists in the list, otherwise False.
    '''

    # Set our initial bounds, and our initial guess.
    guess = len(sorted_list) // 2

    if len(sorted_list) == 0:
        return False

    while sorted_list[guess] != item:
        if sorted_list[guess] > item:
            return binary_search(sorted_list[:guess], item)
        else:
            return binary_search(sorted_list[guess+1:], item)
    
    return True

print(binary_search([1, 2, 3, 4, 5], -1))