class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        lower, upper = 0, x/2
        while int(upper) != int(lower):
            mid = (lower + upper) / 2
            if int(mid**2) == x:
                return int(mid)
            elif (mid**2) > x:
                upper = mid
            else:
                lower = mid

        return int(lower)

if __name__ == '__main__':
    solution = Solution()
    
    x = 123321
    print(solution.mySqrt(x))