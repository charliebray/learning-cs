class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        remainder, carry = 0, 1
        for index in range(len(digits) - 1, -1, -1):
            digit = digits[index]
            digits[index], carry = (digits[index] + carry) % 10, (digits[index] + carry) // 10
        
        if carry > 0:
            return [carry] + digits
        
        return digits


if __name__ == '__main__':
    digits = [8, 9, 9, 9]
    solution = Solution()
    print(solution.plusOne(digits))