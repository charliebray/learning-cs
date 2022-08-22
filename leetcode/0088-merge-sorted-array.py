class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n == 0:
            return
        if m == 0 and n > 0:
            nums1[:] = nums2
            return

        index1, index2 = 0, 0
        while (index1+index2) < (m+n):
            val1, val2 = nums1[index1], nums2[index2]
            if (val2 < val1) or (val1 == 0):
                nums1[(index1+1):(m+index1+1)] = nums1[index1:(m+index1)]
                nums1[index1] = val2
                index2 += 1
            index1 += 1

        # if we haven't finished nums2, add rest of list to end
        nums1[m+index2:] = nums2[index2:]
        
        return nums1



if __name__ == '__main__':
    solution = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 3, 4]
    m, n = 3, 3

    solution.merge(nums1, m, nums2, n)

    print(nums1)