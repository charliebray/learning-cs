class Solution:
    def __init__(self):
        self.a_dict = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.a_dict:
            return self.a_dict[n]
        else:
            self.a_dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.a_dict[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(6))