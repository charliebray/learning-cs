class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        val_pointer = 0
        for index in range(0, len(nums)):
            if nums[index] != val:
                nums[val_pointer] = nums[index]
                val_pointer += 1

        return nums
            
if __name__ == '__main__':
    nums = [3,2,2,3]
    solution = Solution()
    print(solution.removeElement(nums, 3))