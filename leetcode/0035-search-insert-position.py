class Solution:
    '''
    Perform a binary sort to determine index, if it's not there compare the value at index
    to the target value, and return the index either above or below.
    '''
    def searchInsert(self, nums: list[int], target: int) -> int:
        lower_bound, upper_bound = 0, len(nums)
        while abs(upper_bound - lower_bound) >= 1:
            index = (lower_bound + upper_bound)//2

            # If value at index is the target return the index
            if nums[index] == target:
                return index

            # Otherwise determine partition
            elif nums[index] < target:
                lower_bound = index + 1
            else:
                upper_bound = index

        # If we didn't find the value at the index, then it's either at that position or below it when inserted
        if nums[index] > target:
            return index
        else:
            return index + 1
            

if __name__ == '__main__':
    solution = Solution()
    nums, target = [1, 3, 5 ,6], 2
    print(solution.searchInsert(nums, target))
