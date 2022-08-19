class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_str = ""
        carry = 0
        for index in range(1, min(len(a), len(b)) + 1):
            a_val, b_val = int(a[-index]), int(b[-index])
            carry, remainder = (a_val + b_val + carry) // 2, (a_val + b_val + carry) % 2
            sum_str = str(remainder) + sum_str

        if len(a) > len(b):
            for index in range(len(b) + 1, len(a) + 1):
                a_val = int(a[-index])
                carry, remainder = (a_val + carry) // 2, (a_val + carry) % 2
                sum_str = str(remainder) + sum_str
        elif len(b) > len(a):
            for index in range(len(a)+ 1, len(b) + 1):
                a_val = int(b[-index])
                carry, remainder = (a_val + carry) // 2, (a_val + carry) % 2
                sum_str = str(remainder) + sum_str

        if carry > 0:
            sum_str = str(carry) + sum_str

        return sum_str


if __name__ == '__main__':
    solution = Solution()

    a, b = "11111", "111"

    print(solution.addBinary(a,b))