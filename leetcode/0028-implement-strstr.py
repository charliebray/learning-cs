class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' or haystack == needle:
            return 0
        for index in range(0, len(haystack) - len(needle) + 1):
            if haystack[index:index+len(needle)] == needle:
                return index
        return -1

if __name__ == '__main__':
    solution = Solution()
    haystack, needle = "mississippi", "issip"
    print(solution.strStr(haystack, needle))