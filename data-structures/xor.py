class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        '''
        Given a list of integers, we must find the value that appears once,
        where all other values appear only twice.

        Using bitwise XOR works is a solution due to commutative nature.
        E.g. [2, 1, 2] = [10, 01, 10], using XOR we have:
            10 XOR 01 XOR 10 
            = 10 XOR 10 XOR 01
            = 00 XOR 01
            = 01

        Linear complexity (loop through array).
        '''

        x = 0
        for i in nums:
            x ^= i # ^= is the XOR operator in python3
        return x