class Solution:
    '''
    Convert integer to string, reverse the string, and compare.

    Reversing a string of length k is O(k) time complexity. Hence, our solution is 
    O(log10(x)) where x is the size of the integer.
    '''
    def isPalindrome(self, x: int) -> bool:
        a_str = str(x)
        return a_str == a_str[::-1]

if __name__ == '__main__':
    solution = Solution()
    a_int = 1000021
    print(solution.isPalindrome(a_int))
