def merge_sort(a_list, lower_bound=None, upper_bound=None):
    '''
    Trying to perform a merge sort inplace... not sure. Will come back one day.
    Recursive solution, with pointers to each partition.
    '''

    if lower_bound == None and upper_bound == None:
        lower_bound, upper_bound = 0, len(a_list)

    mid = (lower_bound + upper_bound) // 2

    if mid < upper_bound and mid > lower_bound:
        merge_sort(a_list, lower_bound, mid)
        merge_sort(a_list, mid, upper_bound)

        i, j = lower_bound, mid
        while i < mid and j < upper_bound:
            if a_list[i] <= a_list[j]:
                i += 1
            else:
                a_list[j], a_list[i] = a_list[i], a_list[j]
                j += 1

        while i < mid:
            i += 1

        while j < upper_bound:
            j += 1

if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(a_list)
    print(a_list)
