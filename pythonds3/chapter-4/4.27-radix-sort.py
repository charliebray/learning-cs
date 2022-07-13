from basic import *
import random

def radix_sort(a_list):

    # Create a dictionary of digit bins
    bin_dict = {}
    for bin in range(0, 10):
        bin_dict[bin] = Queue()

    # Determine number of digits of largest number in list O(N) complex
    number_of_digits = len(str(max(a_list)))

    # Go through all powers of 10 up until we reach the max number of digits minus 1
    sorted_list = a_list
    for M in range(0, number_of_digits):

        # Bin the numbers in the list O(N) complex
        for x in sorted_list:
            
            if x < M:
                bin_dict[0].enqueue(x)

            else:
                bin_dict[x//(10 ** M) % 10].enqueue(x)

        # Collect numbers from each bin and store in a temporary list
        temp_list = []
        for bin in range(0, 10):
            while bin_dict[bin].size() > 0:
                x = bin_dict[bin].dequeue()
                temp_list.append(x)

        # Take the temp list and make it the new sorted list
        sorted_list = temp_list

    return sorted_list


def main():
    a_list = [random.randrange(1, 100) for i in range(20)]
    print(a_list)
    print(radix_sort(a_list))


if __name__ == '__main__':
    main()