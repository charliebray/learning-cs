class Solution:
    '''
    We simply add or subtract values based on their value relative to the previous value.

    We reverse the string, O(k) time complexity. Then we iterate through the string, O(n) time complexity.
    If the characters value was less than the previous value we subtract, else add.

    Hence, linear time complexity.
    '''
    def romanToInt(self, s: str):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        a_int = 0
        prev_value = 0
        s = s[::-1]
        for char in s:
            char_value = roman_dict[char]
            if char_value < prev_value:
                a_int -= char_value
            else:
                a_int += char_value
            prev_value = char_value
        return a_int

if __name__ == '__main__':
    solution = Solution()
    s = 'MCMXCIV'
    print(solution.romanToInt(s))