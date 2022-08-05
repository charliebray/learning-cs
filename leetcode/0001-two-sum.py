class Solution:
    '''
    For each value in list, determine required value to reach target,
    if not in list then remove the value and go to next.

    Worst case: n(n-1)/2 computations -> O(n^2) time complexity.

    Memory efficient. But, average time complexity could be better...
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for first_index in range(0, len(nums)):
            first_value = nums[first_index]
            required_value = target - first_value
            for second_index in range(first_index + 1, len(nums)):
                second_value = nums[second_index]
                if second_value == required_value:
                    return [first_index, second_index]


class Solution:
    '''
    Convert list to dictionary such that the if duplicates exist, they
    are mapped to the largest occurring index. But this increases memory required.

    We can then iterate over the list to check if the required value is in the dictionary,
    and then return both indices. Increase average time complexity.
    '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = dict((value, index) for index, value in enumerate(nums))
        for first_index, first_value in enumerate(nums):
            required_value = target - first_value
            if (required_value in nums_dict) and (first_index != nums_dict[required_value]):
                return [first_index, nums_dict[required_value]]

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 5, 4, 3, 5]
    target = 10
    print(solution.twoSum(nums, target))
