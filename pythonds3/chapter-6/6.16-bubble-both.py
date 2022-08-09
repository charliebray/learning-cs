def bubbleboth(a_list):
    '''
    Bubble sort, but exchanges in both directions.

    a_list (list): a list of integers (int)
    
    returns: list in sorted order
    '''
    
    lower_bound = 0

    for upper_bound in range(len(a_list) - 1, 0, -1):

        # Bubble up
        swap = False
        for index in range(lower_bound, upper_bound):
            if a_list[index] > a_list[index + 1]:
                a_list[index], a_list[index + 1] = a_list[index + 1], a_list[index]
                swap = True
        if swap == False:
            break

        # Bubble down
        swap = False
        for index in range(upper_bound, lower_bound, -1):
            if a_list[index] < a_list[index - 1]:
                a_list[index], a_list[index - 1] = a_list[index - 1], a_list[index]
                swap = True
        if swap == False:
            break

        lower_bound += 1

        # Once these reach each other, the list is definitely sorted.
        if lower_bound >= upper_bound:
            break
    
    return a_list

if __name__ == '__main__':
    a_list = [1, 2, 5, 3, 10]
    print(a_list)
    print(bubbleboth(a_list))