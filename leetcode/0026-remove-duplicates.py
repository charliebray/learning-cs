class Solution:
    '''
    Use pointers to replace duplicates and traverse the list.
    
    O(n) time complexity.
    '''
    def removeDuplicates(self, nums: list[int]) -> int:
        index_1 = 0
        for index_2 in range(1, len(nums)):
            if nums[index_1] != nums[index_2]:
                index_1 += 1
                nums[index_1] = nums[index_2]

        return index_1 + 1



if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,0,0,0,3,3]
    print(solution.removeDuplicates(nums))
            