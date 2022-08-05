class Solution:
    def isPalindrome(self, x: int) -> bool:
        a_str = str(x)
        return a_str == a_str[::-1]

if __name__ == '__main__':
    solution = Solution()
    a_int = 1000021
    print(solution.isPalindrome(a_int))
