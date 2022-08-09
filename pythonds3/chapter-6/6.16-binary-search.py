def binary_search(sorted_list, item, lower_bound=None, upper_bound=None):
    '''
    sorted_list (list): A sorted list of integers.
    item (int): A integer we are wanting to search for in the sorted list.

    Returns True if the item exists in the list, otherwise False.
    '''

    if len(sorted_list) == 0:
        return False

    # Set our initial bounds, and our initial guess.
    if lower_bound == None and upper_bound == None:
        lower_bound, upper_bound = 0, len(sorted_list) - 1

    guess = (lower_bound + upper_bound) // 2

    if lower_bound == upper_bound and sorted_list[guess] != item:
        return False

    while sorted_list[guess] != item:
        if sorted_list[guess] > item:
            upper_bound = guess
            return binary_search(sorted_list, item, lower_bound, upper_bound)
        else:
            lower_bound = guess + 1
            return binary_search(sorted_list, item, lower_bound, upper_bound)
    
    return True