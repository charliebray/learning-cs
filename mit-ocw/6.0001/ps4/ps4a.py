# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Base case
    if len(sequence) == 1:
        return [sequence]
    
    # Call self (recursion)
    else:
        permutation_list = []
        for index in range(0, len(sequence)):
            char = sequence[index]
            for word in get_permutations(sequence[0:index] + sequence[index+1:]):
                permutation_list.append(char + word)

        return permutation_list

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    print('------')

    example_input = 'ab'
    print('Input:', example_input)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input))

    print('------')

    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input))

