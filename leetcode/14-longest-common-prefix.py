class Solution:
    '''
    We loop through the indices in the first string of the list 
    which corresponds to O(k) time complexity (where k is length of smallest string in list).
    
    We compare the value at the first index with all other words - O(n) time complex. If all match, move to next index.
    This loop breaks when we either exceed the length of a word, or we don't get a match at an index.

    Hence, our time complexity is O(kn).
    '''
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        first_str = strs[0]
        for i in range(0, len(first_str)):
            for a_str in strs:
                # If first word is in every other character, that's the max prefix length
                if i > len(a_str) - 1:
                    return prefix
                # If the index matches, we go to the next word to check.
                if a_str[i] == first_str[i]:
                    continue
                # If the index doesn't match, then return the current prefix
                else:
                    return prefix
            # If the index matches with every other word, we add it to the prefix.
            prefix += first_str[i]
        return prefix

if __name__ == '__main__':
    solution = Solution()
    strs = ["flower","flow","flight"]
    print(solution.longestCommonPrefix(strs))
